from datetime import datetime, timedelta
from typing import Annotated
from zoneinfo import ZoneInfo

from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from pydantic import Field, BaseModel
from tzlocal import get_localzone_name

mcp = FastMCP("Time MCP Server")


class TimeResult(BaseModel):
    timezone: str
    datetime: str
    is_dst: bool


class TimeConversionResult(BaseModel):
    source: TimeResult
    target: TimeResult
    time_difference: str


def get_zoneinfo(timezone_name: str) -> ZoneInfo:
    try:
        return ZoneInfo(timezone_name)
    except Exception as e:
        raise ToolError(f"Invalid timezone: {str(e)}")


@mcp.tool(description="Get current time in specified timezone")
def get_current_time(
    timezone_name: Annotated[
        str,
        Field(
            description="IANA timezone name (e.g., 'Asia/Shanghai', 'America/New_York', 'Europe/London'). "
            "Use '{local_tz}' as local timezone if no timezone provided by the user.",
            json_schema_extra={"example": "Asia/Shanghai"},
            default=get_localzone_name(),
        ),
    ],
) -> TimeResult:
    timezone = get_zoneinfo(timezone_name)
    current_time = datetime.now(timezone)

    return TimeResult(
        timezone=timezone_name,
        datetime=current_time.isoformat(timespec="seconds"),
        is_dst=bool(current_time.dst()),
    )


@mcp.tool(description="Convert time between timezones")
def convert_time(
    time_str: Annotated[
        str, Field(description="Time to convert in 24-hour format (HH:MM)")
    ],
    source_tz: Annotated[
        str,
        Field(
            description="IANA timezone name (e.g., 'Asia/Shanghai', 'America/New_York', 'Europe/London'). "
            "Use '{local_tz}' as local timezone if no timezone provided by the user.",
            json_schema_extra={"example": "Asia/Shanghai"},
            default=get_localzone_name(),
        ),
    ],
    target_tz: Annotated[
        str,
        Field(
            description="IANA timezone name (e.g., 'Asia/Shanghai', 'America/New_York', 'Europe/London'). "
            "Use '{local_tz}' as local timezone if no timezone provided by the user.",
            json_schema_extra={"example": "Europe/London"},
            default=get_localzone_name(),
        ),
    ],
) -> TimeConversionResult:
    source_timezone = get_zoneinfo(source_tz)
    target_timezone = get_zoneinfo(target_tz)

    try:
        parsed_time = datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        raise ValueError("Invalid time format. Expected HH:MM [24-hour format]")

    now = datetime.now(source_timezone)
    source_time = datetime(
        now.year,
        now.month,
        now.day,
        parsed_time.hour,
        parsed_time.minute,
        tzinfo=source_timezone,
    )

    target_time = source_time.astimezone(target_timezone)
    source_offset = source_time.utcoffset() or timedelta()
    target_offset = target_time.utcoffset() or timedelta()
    hours_difference = (target_offset - source_offset).total_seconds() / 3600

    if hours_difference.is_integer():
        time_diff_str = f"{hours_difference:+.1f}h"
    else:
        time_diff_str = f"{hours_difference:+.2f}".rstrip("0").rstrip(".") + "h"

    return TimeConversionResult(
        source=TimeResult(
            timezone=source_tz,
            datetime=source_time.isoformat(timespec="seconds"),
            is_dst=bool(source_time.dst()),
        ),
        target=TimeResult(
            timezone=target_tz,
            datetime=target_time.isoformat(timespec="seconds"),
            is_dst=bool(target_time.dst()),
        ),
        time_difference=time_diff_str,
    )

# GEIP MCP Server 


## Version
v0.1.0

## Overview

GEIP MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GEIP. Full-chain management of GEIP resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="1">Job相关接口</td>
                    <td>ShowJobs</td>
                    <td>查询Job详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Region限制</td>
                    <td>ListTenantGeipSupportInstances</td>
                    <td>console通过此接口获取指定pop点的全域弹性公网IP允许绑定的region实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">任务中心API</td>
                    <td>ListJobs</td>
                    <td>查询管理面任务中心。当前创建图、关闭图、启动图、删除图、增加备份、导入图、导出图、升级图等操作为异步任务,该API用于查询这些任务的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">免责条款签署</td>
                    <td>CreateUserDisclaimer</td>
                    <td>创建租户签署免责条款</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserDisclaimer</td>
                    <td>查询租户签署免责条款详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserDisclaimer</td>
                    <td>删除租户撤销免责条款</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">全域公网带宽</td>
                    <td>CountInternetBandwidth</td>
                    <td>查询全域公网带宽个数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInternetBandwidth</td>
                    <td>查询全域公网带宽详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInternetBandwidth</td>
                    <td>创建全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInternetBandwidth</td>
                    <td>删除全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInternetBandwidth</td>
                    <td>批量创建全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInternetBandwidth</td>
                    <td>更新全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInternetBandwidths</td>
                    <td>查询全域公网带宽列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">全域公网带宽标签</td>
                    <td>ListInternetBandwidthCountFilterTags</td>
                    <td>查询资源实例列表数目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInternetBandwidthTags</td>
                    <td>查询全域公网带宽标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddInternetBandwidthTags</td>
                    <td>添加全域公网带宽标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteInternetBandwidthTags</td>
                    <td>批量删除全域公网带宽标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInternetBandwidthTag</td>
                    <td>删除全域公网带宽标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInternetBandwidthDomainTags</td>
                    <td>查询全域公网带宽项目标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateInternetBandwidthTags</td>
                    <td>批量添加全域公网带宽标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInternetBandwidthFilterTags</td>
                    <td>查询资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">全域公网带宽限制</td>
                    <td>ListInternetBandwidthLimits</td>
                    <td>查询全域公网带宽限制列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">全域弹性公网IP</td>
                    <td>CreateGlobalEip</td>
                    <td>创建全域弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountGlobalEips</td>
                    <td>查询全域弹性公网IP个数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateInstance</td>
                    <td>绑定后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachInternetBandwidth</td>
                    <td>解绑全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAttachInternetBandwidth</td>
                    <td>批量绑定全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalEip</td>
                    <td>删除全域弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachInternetBandwidth</td>
                    <td>绑定全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEips</td>
                    <td>查询全域弹性公网IP列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateGlobalEip</td>
                    <td>批量创建全域弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGlobalEip</td>
                    <td>查询全域弹性公网IP详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDetachInternetBandwidth</td>
                    <td>批量解绑全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGlobalEip</td>
                    <td>更新全域弹性公网IP信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateInstance</td>
                    <td>解绑后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">全域弹性公网IP标签</td>
                    <td>ListGlobalEipDomainTags</td>
                    <td>查询全域弹性公网IP的项目标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteGlobalEipTags</td>
                    <td>批量删除全域弹性公网IP的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGlobalEipTags</td>
                    <td>添加全域弹性公网IP的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEipCountFilterTags</td>
                    <td>查询资源实例列表数目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalEipTag</td>
                    <td>删除全域弹性公网IP的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGlobalEipTags</td>
                    <td>查询全域弹性公网IP的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEipFilterTags</td>
                    <td>查询资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateGlobalEipTags</td>
                    <td>批量添加全域弹性公网IP的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">全域弹性公网IP段</td>
                    <td>CreateGlobalEipSegment</td>
                    <td>创建全域弹性公网IP段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateGeipSegmentInstance</td>
                    <td>全域弹性公网IP段解绑后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountGlobalEipSegment</td>
                    <td>查询全域弹性公网IP段个数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEipSegments</td>
                    <td>查询全域弹性公网IP段列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalEipSegment</td>
                    <td>删除全域弹性公网IP段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDetachGeipSegmentInternetBandwidth</td>
                    <td>全域弹性公网IP段批量解绑全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGlobalEipSegment</td>
                    <td>更新全域弹性公网IP段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateGeipSegmentInstance</td>
                    <td>全域弹性公网IP段绑定后端实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGlobalEipSegment</td>
                    <td>查询全域弹性公网IP段详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAttachGeipSegmentInternetBandwidth</td>
                    <td>全域弹性公网IP段批量绑定全域公网带宽</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">全域弹性公网IP段标签</td>
                    <td>BatchDeleteGeipSegmentTags</td>
                    <td>批量删除全域弹性公网IP段的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGeipSegmentTags</td>
                    <td>添加全域弹性公网IP段的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeipSegmentCountFilterTags</td>
                    <td>查询资源实例列表的数目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeipSegmentDomainTags</td>
                    <td>查询全域弹性公网IP段的项目标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGeipSegmentTag</td>
                    <td>删除全域弹性公网IP段的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeipSegmentFilterTags</td>
                    <td>查询资源实例的列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGeipSegmentTags</td>
                    <td>查询全域弹性公网IP段的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateGeipSegmentTags</td>
                    <td>批量添加全域弹性公网IP段的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">全域弹性公网IP池</td>
                    <td>ListGeipPools</td>
                    <td>查询全域弹性公网IP池列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">多区域密钥</td>
                    <td>ListSupportRegions</td>
                    <td>- 功能介绍:查询跨区域密钥所支持的区域。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">接入点</td>
                    <td>ListAccessSites</td>
                    <td>查询接入点列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">掩码限制</td>
                    <td>ListSupportMasks</td>
                    <td>查询全域弹性公网IP段支持的掩码列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额</td>
                    <td>ListGeipResourceQuotas</td>
                    <td>查询租户全域弹性公网IP配额</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

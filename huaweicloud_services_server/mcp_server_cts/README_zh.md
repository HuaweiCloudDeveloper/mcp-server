# CTS MCP Server 


## Version
v0.1.0

## Overview

CTS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CTS. Full-chain management of CTS resources can be carried out based on natural language.

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
                    <td rowspan="2">Tags</td>
                    <td>BatchCreateResourceTags</td>
                    <td>为指定实例批量添加标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteResourceTags</td>
                    <td>为指定实例批量删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">事件管理</td>
                    <td>ListTraces</td>
                    <td>通过事件列表查询接口,可以查出系统记录的7天内资源操作记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">关键操作通知管理</td>
                    <td>ListNotifications</td>
                    <td>查询创建的关键操作通知规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">其它接口</td>
                    <td>ListUserResources</td>
                    <td>查询30天事件的操作用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOperations</td>
                    <td>查询云服务的全量操作列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckObsBuckets</td>
                    <td>检查已经配置OBS桶是否可以成功转储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTraceResources</td>
                    <td>查询事件的资源类型列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">订阅管理操作</td>
                    <td>DeleteNotification</td>
                    <td>该接口用于删除指定订阅管理</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotification</td>
                    <td>该接口用于修改指定的订阅管理</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotification</td>
                    <td>该接口用于创建指定实例下对应的应用下的设备操作,订阅到指定的topic</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">追踪器管理</td>
                    <td>CreateTracker</td>
                    <td>云审计服务开通后系统会自动创建一个追踪器,用来关联系统记录的所有操作。目前,一个云账户在一个Region下支持创建一个管理类追踪器和多个数据类追踪器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTracker</td>
                    <td>云审计服务目前仅支持删除已创建的数据类追踪器。删除追踪器对已有的操作记录没有影响,当您重新开通云审计服务后,依旧可以查看已有的操作记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTracker</td>
                    <td>云审计服务支持修改已创建追踪器的配置项,包括OBS桶转储、关键事件通知、事件转储加密、通过LTS对管理类事件进行检索、事件文件完整性校验以及追踪器启停状态等相关参数,修改追踪器对已有的操作记录没有影响。修改追踪器完成后,系统立即以新的规则开始记录操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrackers</td>
                    <td>开通云审计服务成功后,您可以在追踪器信息页面查看追踪器的详细信息。详细信息主要包括追踪器名称,用于存储操作事件的OBS桶名称和OBS桶中的事件文件前缀。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ListQuotas</td>
                    <td>获取配额信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

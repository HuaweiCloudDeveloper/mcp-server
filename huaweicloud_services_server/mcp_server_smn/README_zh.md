# SMN MCP Server 


## Version
v0.1.0

## Overview

SMN MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SMN. Full-chain management of SMN resources can be carried out based on natural language.

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
                    <td rowspan="5">Application endpoint操作</td>
                    <td>CreateApplicationEndpoint</td>
                    <td>创建应用平台的endpoint终端。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationEndpoints</td>
                    <td>查询平台的endpoint列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplicationEndpoint</td>
                    <td>删除设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApplicationEndpoint</td>
                    <td>更新设备属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationEndpointAttributes</td>
                    <td>获取endpoint的属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Application操作</td>
                    <td>CreateApplication</td>
                    <td>创建平台应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApplication</td>
                    <td>更新应用平台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplications</td>
                    <td>查询应用平台列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplicationAttributes</td>
                    <td>获取应用平台属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplication</td>
                    <td>删除平台应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Application直发消息操作</td>
                    <td>PublishAppMessage</td>
                    <td>将消息直发给endpoint设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">TAG功能</td>
                    <td>ListResourceInstances</td>
                    <td>使用标签过滤查询租户下资源的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Tags</td>
                    <td>ListProjectTags</td>
                    <td>查询租户在指定项目中指定资源类型下的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">主题操作</td>
                    <td>DeleteTopic</td>
                    <td>删除主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicDetails</td>
                    <td>查询Topic的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTopicAttribute</td>
                    <td>更新主题的策略信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopics</td>
                    <td>分页查询Topic列表,Topic列表按照Topic创建时间进行降序排列。分页查询可以指定offset以及limit。如果不存在Topic,则返回空列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTopicAttributeByName</td>
                    <td>删除指定名称的主题策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTopicAttributes</td>
                    <td>删除所有主题策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTopic</td>
                    <td>更新显示名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTopicAttributes</td>
                    <td>查询主题的策略信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTopic</td>
                    <td>创建Topic,单用户默认配额为3000。高并发场景下,可能会出现Topic数量超过3000仍创建成功的情况,此为正常现象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">云日志操作</td>
                    <td>CreateLogtank</td>
                    <td>为指定Topic绑定一个云日志,用于记录主题消息发送状态等信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogtank</td>
                    <td>更新指定Topic绑定的云日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogtank</td>
                    <td>解绑指定Topic绑定的云日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogtank</td>
                    <td>查询指定Topic绑定的云日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">使用标签管理服务</td>
                    <td>BatchCreateOrDeleteResourceTags</td>
                    <td>为指定实例批量添加或删除标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceTags</td>
                    <td>查询指定实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">发布消息操作</td>
                    <td>ShowHttpDetectResult</td>
                    <td>根据http探测发送返回的task_id查询探测结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishMessage</td>
                    <td>将消息发送给Topic的所有订阅端点。当返回消息ID时,该消息已被保存并开始尝试将其推送给Topic的订阅者。为确保您的消息能够成功推送到各个订阅者,请确保您的消息内容符合当地法律法规要求。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishHttpDetect</td>
                    <td>基于主题发送http/https探测消息,探测当前http/https 终端是否可用,SMN出口是否能够正常访问该终端。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">服务开通管理</td>
                    <td>ListSubscriptions</td>
                    <td>该接口用于获取服务开通信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询版本操作</td>
                    <td>ListVersion</td>
                    <td>查询SMN API V2版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVersions</td>
                    <td>查询SMN开放API支持的版本号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">模板操作</td>
                    <td>ListMessageTemplateDetails</td>
                    <td>查询模板详情,包括模板内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMessageTemplate</td>
                    <td>创建一个模板,用户可以按照模板去发送消息,这样可以减少请求的数据量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMessageTemplate</td>
                    <td>修改消息模板的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessageTemplates</td>
                    <td>分页查询模板列表,模板列表按照创建时间进行升序排列。分页查询可以指定offset以及limit。如果不存在模板,则返回空列表。额外的查询参数分别有message_template_name和protocol。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMessageTemplate</td>
                    <td>删除消息模板。删除模板之前的消息请求都可以使用该模板发送,删除之后无法再使用该模板发送消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">订阅操作</td>
                    <td>AddSubscriptionFromSubscriptionUser</td>
                    <td>为指定的Topic添加订阅者,订阅者信息来源为订阅用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubscriptionsByTopic</td>
                    <td>分页获取特定Topic的订阅列表,订阅列表按照订阅创建时间进行升序排列。分页查询可以指定offset以及limit。如果指定Topic不存在订阅者,返回空列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelSubscription</td>
                    <td>删除指定的订阅者。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSubscription</td>
                    <td>为指定Topic添加一个订阅者,如果订阅者的状态为未确认,则向订阅者发送一个确认的消息。待订阅者进行ConfirmSubscription确认后,该订阅者才能收到Topic发布的消息。单Topic默认可添加10000个订阅者,高并发场景下,可能会出现订阅者数量超过10000仍添加成功的情况,此为正常现象。接口是幂等的,如果添加已存在的订阅者,则返回成功,且status code为200,否则status code为201。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubscription</td>
                    <td>更新订阅者备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">订阅过滤策略操作</td>
                    <td>BatchCreateSubscriptionsFilterPolices</td>
                    <td>创建订阅者的消息过滤策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateSubscriptionsFilterPolices</td>
                    <td>更新订阅者的消息过滤策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSubscriptionsFilterPolices</td>
                    <td>删除订阅者的消息过滤策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资源标签</td>
                    <td>CreateResourceTag</td>
                    <td>用于给云服务的多个资源添加标签,每个资源最多可添加10个标签,每次最多支持批量操作20个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceTag</td>
                    <td>用于批量移除云服务多个资源的标签,每个资源最多支持移除10个标签,每次最多支持批量操作20个资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">通知策略</td>
                    <td>ShowNotifyPolicy</td>
                    <td>查询通知策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotifyPolicy</td>
                    <td>创建通知策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotifyPolicy</td>
                    <td>修改通知策略,该接口仅支持全量修改,不支持部分修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotifyPolicy</td>
                    <td>删除通知策略</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

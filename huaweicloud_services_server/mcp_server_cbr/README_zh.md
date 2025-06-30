# CBR MCP Server 


## Version
v0.1.0

## Overview

CBR MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CBR. Full-chain management of CBR resources can be carried out based on natural language.

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
                    <td rowspan="1">Checkpoint管理</td>
                    <td>ShowCheckpoint</td>
                    <td>本接口用于查询Checkpoint详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">主机管理</td>
                    <td>ListPolicies</td>
                    <td>查询主机策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">任务</td>
                    <td>ListOpLogs</td>
                    <td>查询任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOpLog</td>
                    <td>根据指定任务ID查询任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">可保护性</td>
                    <td>ShowReplicationCapabilities</td>
                    <td>查询本区域的复制能力</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProtectable</td>
                    <td>查询可保护性资源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckAgent</td>
                    <td>检查应用一致性Agent状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProtectable</td>
                    <td>根据ID查询可保护性资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">后端云服务器</td>
                    <td>DeleteMember</td>
                    <td>删除后端云服务器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">备份</td>
                    <td>ShowBackup</td>
                    <td>根据指定id查询单个副本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportBackup</td>
                    <td>同步线下混合云VMware备份副本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyBackup</td>
                    <td>跨区域复制备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackup</td>
                    <td>根据备份id更改备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreBackup</td>
                    <td>恢复备份数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">备份与恢复</td>
                    <td>ListBackups</td>
                    <td>获取备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">备份共享</td>
                    <td>AddMember</td>
                    <td>添加备份可共享的成员,只有云服务器备份可以添加备份共享成员,且仅支持在同一区域的不同用户间共享。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMembersDetail</td>
                    <td>获取备份共享成员的列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMemberStatus</td>
                    <td>更新备份共享成员的状态,需要接收方执行此API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMemberDetail</td>
                    <td>获取备份成员的详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">备份管理API</td>
                    <td>DeleteBackup</td>
                    <td>删除备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">存储库</td>
                    <td>ShowVault</td>
                    <td>根据ID查询指定存储库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVault</td>
                    <td>根据存储库ID修改存储库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVault</td>
                    <td>查询存储库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateVaultPolicy</td>
                    <td>存储库解除策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateVaultResource</td>
                    <td>支持资源迁移到另一个存储库,不删除备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateVault</td>
                    <td>批量修改项目下所有存储库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVault</td>
                    <td>删除存储库。若删除储存库,将一并删除存储库中的所有备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExternalVault</td>
                    <td>查询其他区域的存储库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateVaultPolicy</td>
                    <td>存储库设置策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPaidVault</td>
                    <td>创建包周期存储库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetVaultResource</td>
                    <td>设置存储库资源是否自动备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSummary</td>
                    <td>查询项目下所有存储库的总容量和总使用量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveVaultResource</td>
                    <td>移除存储库中的资源,若移除资源,将一并删除该资源在保管库中的备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVault</td>
                    <td>创建存储库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddVaultResource</td>
                    <td>存储库添加资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">文件应用备份</td>
                    <td>UpdateAgent</td>
                    <td>修改客户端状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnregisterAgent</td>
                    <td>移除客户端,移除客户端时将会删除该客户端所有备份,请谨慎操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterAgent</td>
                    <td>注册客户端,安装时候由Agent调用,无需手动注册。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgent</td>
                    <td>查询客户端列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveAgentPath</td>
                    <td>移除已添加的文件备份路径。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgent</td>
                    <td>查询指定客户端</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAgentPath</td>
                    <td>对客户端新增备份路径,新增的路径不会校验是否存在。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">标签</td>
                    <td>DeleteVaultTag</td>
                    <td>幂等接口:删除时,如果删除的标签不存在,返回404。Key不能为空或者空字符串。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVaultTag</td>
                    <td>查询指定实例的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVaultTags</td>
                    <td>一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVaultResourceInstances</td>
                    <td>使用标签过滤实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVaultProjectTag</td>
                    <td>查询租户在指定Region和实例类型的所有标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateAndDeleteVaultTags</td>
                    <td>为指定实例批量添加或删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">组织策略</td>
                    <td>DeleteOrganizationPolicy</td>
                    <td>删除组织策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrganizationPolicyDetail</td>
                    <td>查询组织策略每个账号下策略部署状态列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationPolicy</td>
                    <td>查询指定组织策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOrganizationPolicy</td>
                    <td>更新组织策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrganizationPolicies</td>
                    <td>查询组织策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrganizationPolicy</td>
                    <td>创建组织策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">联邦身份认证管理</td>
                    <td>ShowMetadata</td>
                    <td>该接口可以用于[管理员](https://support.huaweicloud.com/usermanual-iam/iam_01_0001.html)查询身份提供商导入到IAM中的Metadata文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">计量</td>
                    <td>ShowStorageUsage</td>
                    <td>查询容量统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">运营</td>
                    <td>ChangeVaultChargeMode</td>
                    <td>修改资源的付费模式,暂时只支持按需资源转包周期资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOrder</td>
                    <td>订单更新,支付cbc订单后,调用该接口更新包周期产品订单信息。该接口已废弃。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeOrder</td>
                    <td>订单更新,调用该接口更新包周期产品订单信息,返回待支付订单信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">还原点</td>
                    <td>CreateCheckpoint</td>
                    <td>对存储库执行备份,生成备份还原点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportCheckpoint</td>
                    <td>针对vault同步备份副本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyCheckpoint</td>
                    <td>执行复制</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">防护策略管理</td>
                    <td>DeletePolicy</td>
                    <td>删除防护策略,若策略正在使用,则需要先接解除域名与策略的绑定关系才能删除策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicy</td>
                    <td>根据Id查询防护策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicy</td>
                    <td>更新防护策略,请求体可只传需要更新的部分</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicy</td>
                    <td>创建防护策略,系统会在生成策略时配置一些默认的配置项,如果需要修改策略的默认配置项需要通过调用更新防护策略接口实现</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">项目</td>
                    <td>ListDomainProjects</td>
                    <td>根据指定租户名称查询项目列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMigrateStatus</td>
                    <td>查询迁移结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomain</td>
                    <td>由控制台调用的内部接口,用于仅在查询共享备份时获取源project_id的域名信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateDomain</td>
                    <td>将CSBS/VBS资源迁移到CBR。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjects</td>
                    <td>查询租户的企业项目信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

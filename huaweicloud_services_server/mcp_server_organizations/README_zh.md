# Organizations MCP Server 

## 版本信息
v0.1.0

## 产品描述

Organizations MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务Organizations交互的能力。可以基于自然语言对Organizations资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

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
                    <td rowspan="11">Account</td>
                    <td>ListCloseAccountStatuses</td>
                    <td>列出组织中指定状态的账号关闭请求。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MoveAccount</td>
                    <td>将账号从其当前源位置(根或组织单元)移动到指定的目标位置(根或组织单元)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCreateAccountStatus</td>
                    <td>检索创建账号的异步请求的当前状态。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCreateAccountStatuses</td>
                    <td>列出组织中指定状态的账号创建请求。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InviteAccount</td>
                    <td>向另一个账号发送邀请,受邀账号将以成员账号加入您的组织。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveAccount</td>
                    <td>从组织中移除指定的账号。移除的账号将成为一个独立账号,该账号不是任何组织的成员。此操作只能由组织的管理账号调用。只有当账号配置了作为独立账号运行所需的信息时,您才能从组织中移除账号。注意,要移除的账号不能是组织启用的任何服务的委托管理员账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccount</td>
                    <td>创建一个账号,生成的账号将自动成为调用此接口的账号所属组织的成员。此操作只能由组织的管理账号调用。组织云服务将在新账号中创建所需的服务关联委托和账号访问委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccounts</td>
                    <td>列出组织中的账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。如果指定父级组织单元,则将获得作为父级直系子级的所有账号的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAccount</td>
                    <td>更新指定的账号信息。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CloseAccount</td>
                    <td>关闭账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccount</td>
                    <td>查询有关指定账号的信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DelegatedAdministrator</td>
                    <td>ListDelegatedAdministrators</td>
                    <td>列出在此组织中指定为委派管理员的账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDelegatedServices</td>
                    <td>列出指定账号是其委托管理员的服务。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeregisterDelegatedAdministrator</td>
                    <td>删除指定成员账号作为指定服务的委托管理员。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterDelegatedAdministrator</td>
                    <td>指定成员账号能够管理指定服务的组织功能。此接口授予委托管理员对组织服务数据的只读访问权限。委托管理员账号中的IAM用户仍需要IAM权限才能访问和管理服务。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Handshake</td>
                    <td>ShowHandshake</td>
                    <td>查询组织中已有账号邀请的相关信息。此接口可以由组织中的任何账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReceivedHandshakes</td>
                    <td>列出账号收到的所有邀请。此操作可以由任何账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeclineHandshake</td>
                    <td>拒绝邀请请求。受邀账号拒绝邀请,此时当前邀请状态将设置为拒绝,邀请停止。此接口只能由受邀账号调用。邀请发起者无法再次激活被拒绝的邀请,但可以重新发送新的邀请。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptHandshake</td>
                    <td>向邀请的发起方发送应答,接受加入组织邀请。在您接受邀请后,此邀请信息将继续保留并出现在相关API的返回结果中,保留期限为30天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHandshakes</td>
                    <td>列出所属组织发送的邀请。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelHandshake</td>
                    <td>取消邀请,此时邀请状态将设置为已取消。此接口只能由发起邀请的账号调用。取消邀请后,此邀请信息将继续保留并出现在相关API的返回结果中,保留期限为30天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Misc</td>
                    <td>ShowEffectivePolicies</td>
                    <td>查询指定策略类型和账号的有效策略信息。当前此接口不支持查询服务控制策略(service_control_policy)。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServices</td>
                    <td>列出所有可以与组织服务集成的云服务。集成后云服务将成为组织的可信服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagPolicyServices</td>
                    <td>列出被添加到标签策略强制执行的资源类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQuotas</td>
                    <td>列出租户的组织配额。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEntities</td>
                    <td>列出组织中包含的所有根、组织单元和账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。您可以通过指定父ID和子ID参数来过滤实体。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Organization</td>
                    <td>ShowOrganization</td>
                    <td>查询账号所属组织的信息。此操作可以由组织中的任何账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LeaveOrganization</td>
                    <td>此操作只能由组织的成员账号调用。只有当组织账号配置了作为独立账号运行所需的信息时,您才能作为成员账号离开组织。要离开的账号不能是组织启用的任何服务的委托管理员账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrganization</td>
                    <td>创建组织。调用此接口的账号将自动成为新组织的管理账号,调用此接口的账号凭证必须是新组织管理账号的账号凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOrganization</td>
                    <td>删除组织。您必须使用管理账号才能删除组织,并且先移除组织中的所有账号、组织单元和策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoots</td>
                    <td>列出当前组织的根。此接口只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">OrganizationalUnit</td>
                    <td>DeleteOrganizationalUnit</td>
                    <td>从根或其他组织单元中删除组织单元。前提是您必须先移除该组织单元中的所有成员账号或将成员账号移动至其他组织单元,必须删除该组织单元中的所有子组织单元。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrganizationalUnit</td>
                    <td>查询有关组织单元的信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrganizationalUnit</td>
                    <td>在根或父组织单元中创建组织单元。组织单元是账号的容器,使您能够对账号进行分组管理,并根据业务要求应用策略。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrganizationalUnits</td>
                    <td>列出组织中的所有组织单元。如果指定父级组织单元,则将获得父级直系子级的组织单元列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOrganizationalUnit</td>
                    <td>重命名指定的组织单元。重命名后组织单元ID不变,下属子组织单元和下属账号不变,组织单元绑定的策略不变。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Policy</td>
                    <td>ListPolicies</td>
                    <td>列出组织中的所有策略。如果指定了资源ID,例如组织单元ID或账号ID,则将获得该资源已绑定的策略列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicy</td>
                    <td>创建指定类型的策略。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicy</td>
                    <td>检索策略的相关信息。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicy</td>
                    <td>从组织中删除指定的策略。在执行此操作之前,必须首先将策略跟所有组织单元、根和账号解绑。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicy</td>
                    <td>更新策略,可以更新策略的名称、描述或内容。如果不提供任何参数,则策略将保持不变。您不能更改策略的类型。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisablePolicyType</td>
                    <td>禁用根中的策略类型。只有在根中启用了特定类型的策略,才能将该类型的策略绑定到根中的实体。执行此操作后,您不能再将指定类型的策略绑定到该根或该根中的任何组织单元或账号。这是在后台执行的异步请求。您可以使用ListRoots查看指定根的策略类型的状态。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnablePolicyType</td>
                    <td>在根中启用策略类型。在根中启用策略类型后,您可以将该类型的策略绑定到根、或该根中的任何组织单元和账号。这是在后台执行的异步请求。您可以使用ListRoots查看指定根的策略类型的状态。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachPolicy</td>
                    <td>从根、组织单元或账号解绑策略。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachPolicy</td>
                    <td>绑定策略到根、组织单元或个人账号。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEntitiesForPolicy</td>
                    <td>列出跟指定策略绑定的所有根、组织单元和账号。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Tag</td>
                    <td>ListResourceInstances</td>
                    <td>根据资源类型及标签信息查询实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TagResource</td>
                    <td>向指定的资源添加一个或多个标签。目前,您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceInstancesCount</td>
                    <td>根据资源类型及标签信息查询实例数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UntagResource</td>
                    <td>从指定资源中删除具有指定主键的任何标签。您可以将标签绑定到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagsForResource</td>
                    <td>列出绑定到指定资源的标签。您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagResources</td>
                    <td>列出绑定到指定资源类型的标签。您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTagResource</td>
                    <td>从指定资源类型中删除具有指定主键的任何标签。您可以将标签绑定到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTagResource</td>
                    <td>向指定的资源类型添加一个或多个标签。目前,您可以将标签附加到组织中的账号、组织单元、根和策略。此操作只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceTags</td>
                    <td>查询资源标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TrustedService</td>
                    <td>EnableTrustedService</td>
                    <td>启用服务(由service_principal指定的服务)与组织的集成。启用可信服务后,允许指定的可信服务对组织中的所有账号创建服务关联委托。这允许可信服务代表您在组织及其账号中执行操作。此接口只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableTrustedService</td>
                    <td>禁用服务(由service_principal指定的服务)与组织的集成。禁用可信服务后,指定服务将不可以在组织中的新账号中创建服务关联委托。这意味着该服务无法代表您对组织中的任何新账号执行操作。在服务完成从组织中的清理之前,服务仍可以在旧账号中执行操作。此接口只能由组织的管理账号调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrustedServices</td>
                    <td>返回启用与组织集成的可信服务列表。此操作只能由组织的管理账号或作为服务委托管理员的成员账号调用。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
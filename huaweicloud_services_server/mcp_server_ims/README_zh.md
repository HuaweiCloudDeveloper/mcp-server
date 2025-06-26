# IMS MCP Server 


## Version
v0.1.0

## Overview

IMS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IMS. Full-chain management of IMS resources can be carried out based on natural language.

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
                    <td rowspan="1">查询密钥API版本信息</td>
                    <td>ShowVersion</td>
                    <td>- 功能介绍:查指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询版本操作</td>
                    <td>ListVersions</td>
                    <td>查询SMN开放API支持的版本号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">标签管理</td>
                    <td>BatchDeleteTags</td>
                    <td>为指定保护实例批量删除标签。一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">镜像</td>
                    <td>UpdateImage</td>
                    <td>更新镜像信息接口,主要用于镜像属性的修改。当前仅支持可用(active)状态的镜像更新相关信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOsVersions</td>
                    <td>查询当前区域弹性云服务器的OS兼容性列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataImage</td>
                    <td>使用上传至OBS桶中的外部数据卷镜像文件制作数据镜像。作为异步接口,调用成功,只是说明后台收到了制作请求,镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态。具体请参考异步任务查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterImage</td>
                    <td>该接口用于将镜像文件注册为云平台未初始化的私有镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWholeImage</td>
                    <td>使用云服务器或者云服务器备份制作整机镜像。作为异步接口,调用成功,只是说明后台收到了制作整机镜像的请求,镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态,具体请参考异步任务查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportImage</td>
                    <td>该接口为扩展接口,用于用户将自己的私有镜像导出到指定的OBS桶中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImages</td>
                    <td>根据不同条件查询镜像列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImage</td>
                    <td>本接口用于制作私有镜像,支持:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportImageQuick</td>
                    <td>使用上传至OBS桶中的超大外部镜像文件制作私有镜像,目前仅支持RAW或ZVHD2格式镜像文件。且要求镜像文件大小不能超过1TB。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">镜像(OpenStack原生)</td>
                    <td>GlanceShowImage</td>
                    <td>查询单个镜像详情,用户可以通过该接口查询单个私有或者公共镜像的详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceUpdateImage</td>
                    <td>修改镜像信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceCreateImageMetadata</td>
                    <td>创建镜像元数据。调用创建镜像元数据接口成功后,只是创建了镜像的元数据,镜像对应的实际镜像文件并不存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceDeleteImage</td>
                    <td>该接口主要用于删除镜像,用户可以通过该接口将自己的私有镜像删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceListImages</td>
                    <td>获取镜像列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">镜像任务</td>
                    <td>ShowJob</td>
                    <td>该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobProgress</td>
                    <td>该接口为扩展接口,主要用于查询异步任务进度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">镜像共享</td>
                    <td>BatchUpdateMembers</td>
                    <td>该接口为扩展接口,主要用于用户接受或者拒绝多个共享镜像时批量更新镜像成员的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddMembers</td>
                    <td>该接口为扩展接口,主要用于镜像共享时用户将多个镜像共享给多个用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageMembers</td>
                    <td>该接口用于共享镜像过程中,获取接受该镜像的成员列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageMember</td>
                    <td>该接口主要用于镜像共享中查询某个镜像成员的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMembers</td>
                    <td>该接口为扩展接口,主要用于取消镜像共享。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">镜像共享(OpenStack原生)</td>
                    <td>GlanceShowImageMember</td>
                    <td>该接口主要用于镜像共享中查询某个镜像成员的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceAddImageMember</td>
                    <td>用户共享镜像给其他用户时,使用该接口向该镜像成员中添加接受镜像用户的项目ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceDeleteImageMember</td>
                    <td>该接口用于取消对某个用户的镜像共享。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceListImageMembers</td>
                    <td>该接口用于共享镜像过程中,获取接受该镜像的成员列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceUpdateImageMember</td>
                    <td>用户接受或者拒绝共享镜像时,使用该接口更新镜像成员的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">镜像复制</td>
                    <td>CopyImageCrossRegion</td>
                    <td>该接口为扩展接口,用户在一个区域制作的私有镜像,可以通过跨Region复制镜像将镜像复制到其他区域,在其他区域发放相同类型的云服务器,帮助用户实现区域间的业务迁移。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyImageInRegion</td>
                    <td>该接口为扩展接口,主要用于用户将一个已有镜像复制为另一个镜像。复制镜像时,可以更改镜像的加密等属性,以满足不同的场景。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">镜像标签</td>
                    <td>ListTags</td>
                    <td>根据不同条件查询镜像标签列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddOrDeleteTags</td>
                    <td>该接口用于为指定镜像批量添加/更新、删除标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddImageTag</td>
                    <td>该接口用于为指定镜像添加或更新指定的单个标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImagesTags</td>
                    <td>该接口用于为查询租户的所有镜像上的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageTags</td>
                    <td>该接口用于为查询指定镜像上的所有标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageByTags</td>
                    <td>该接口用于按标签或其他条件对镜像进行过滤或者计数使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrUpdateTags</td>
                    <td>该接口主要用于为某个镜像增加或修改一个自定义标签。通过自定义标签,用户可以将镜像进行分类。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImageTag</td>
                    <td>该接口用于为镜像删除指定的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">镜像标签(OpenStack原生)</td>
                    <td>GlanceDeleteTag</td>
                    <td>该接口主要用于删除某个镜像的自定义标签,通过该接口,用户可以将私有镜像中一些不用的标签删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceCreateTag</td>
                    <td>该接口主要用于为某个镜像添加一个自定义标签。通过自定义标签,用户可以将镜像进行分类。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">镜像视图(OpenStack原生)</td>
                    <td>GlanceListImageSchemas</td>
                    <td>该接口主要用于查询镜像列表视图,通过该接口用户可以了解到镜像列表的详细情况和数据结构。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceListImageMemberSchemas</td>
                    <td>该接口主要用于查询镜像成员列表视图,通过视图,用户可以了解到镜像成员包含哪些属性,同时也可以了解每个属性的数据类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceShowImageMemberSchemas</td>
                    <td>该接口主要用于查询镜像成员视图,通过视图,用户可以了解到镜像成员包含哪些属性,同时也可以了解每个属性的数据类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GlanceShowImageSchemas</td>
                    <td>该接口主要用于查询镜像视图,通过视图,用户可以了解到镜像包含哪些属性,同时也可以了解每个属性的数据类型等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">镜像配额</td>
                    <td>ShowImageQuota</td>
                    <td>该接口为扩展接口,主要用于查询租户在当前Region的私有镜像的配额数量。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

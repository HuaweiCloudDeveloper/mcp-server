# IMS MCP Server 

## 版本信息
v0.1.0

## 产品描述

IMS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IMS交互的能力。可以基于自然语言对IMS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 查询API版本信息(OpenStack原生) | ShowVersion | 查询API的版本信息列表,包括API的版本兼容性、域名信息等。 | To be tested |
|  | ListVersions | 查询API的版本信息列表,包括API的版本兼容性、域名信息等。 | To be tested |
| 镜像 | UpdateImage | 更新镜像信息接口,主要用于镜像属性的修改。当前仅支持可用(active)状态的镜像更新相关信息。 | To be tested |
|  | ListOsVersions | 查询当前区域弹性云服务器的OS兼容性列表。 | To be tested |
|  | CreateDataImage | 使用上传至OBS桶中的外部数据卷镜像文件制作数据镜像。作为异步接口,调用成功,只是说明后台收到了制作请求,镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态。具体请参考异步任务查询。 | To be tested |
|  | RegisterImage | 该接口用于将镜像文件注册为云平台未初始化的私有镜像。 | To be tested |
|  | CreateWholeImage | 使用云服务器或者云服务器备份制作整机镜像。作为异步接口,调用成功,只是说明后台收到了制作整机镜像的请求,镜像是否制作成功需要通过异步任务查询接口查询该任务的执行状态,具体请参考异步任务查询。 | To be tested |
|  | ExportImage | 该接口为扩展接口,用于用户将自己的私有镜像导出到指定的OBS桶中。 | To be tested |
|  | ListImages | 根据不同条件查询镜像列表信息。 | To be tested |
|  | CreateImage | 本接口用于制作私有镜像,支持: | To be tested |
|  | ImportImageQuick | 使用上传至OBS桶中的超大外部镜像文件制作私有镜像,目前仅支持RAW或ZVHD2格式镜像文件。且要求镜像文件大小不能超过1TB。 | To be tested |
| 镜像(OpenStack原生) | GlanceShowImage | 查询单个镜像详情,用户可以通过该接口查询单个私有或者公共镜像的详情 | To be tested |
|  | GlanceUpdateImage | 修改镜像信息 | To be tested |
|  | GlanceCreateImageMetadata | 创建镜像元数据。调用创建镜像元数据接口成功后,只是创建了镜像的元数据,镜像对应的实际镜像文件并不存在 | To be tested |
|  | GlanceDeleteImage | 该接口主要用于删除镜像,用户可以通过该接口将自己的私有镜像删除。 | To be tested |
|  | GlanceListImages | 获取镜像列表。 | To be tested |
| 镜像任务 | ShowJob | 该接口为扩展接口,主要用于查询异步接口执行情况,比如查询导出镜像任务的执行状态。 | To be tested |
|  | ShowJobProgress | 该接口为扩展接口,主要用于查询异步任务进度。 | To be tested |
| 镜像共享 | BatchUpdateMembers | 该接口为扩展接口,主要用于用户接受或者拒绝多个共享镜像时批量更新镜像成员的状态。 | To be tested |
|  | BatchAddMembers | 该接口为扩展接口,主要用于镜像共享时用户将多个镜像共享给多个用户。 | To be tested |
|  | ListImageMembers | 该接口用于共享镜像过程中,获取接受该镜像的成员列表。 | To be tested |
|  | ShowImageMember | 该接口主要用于镜像共享中查询某个镜像成员的详情。 | To be tested |
|  | BatchDeleteMembers | 该接口为扩展接口,主要用于取消镜像共享。 | To be tested |
| 镜像共享(OpenStack原生) | GlanceShowImageMember | 该接口主要用于镜像共享中查询某个镜像成员的详情。 | To be tested |
|  | GlanceAddImageMember | 用户共享镜像给其他用户时,使用该接口向该镜像成员中添加接受镜像用户的项目ID。 | To be tested |
|  | GlanceDeleteImageMember | 该接口用于取消对某个用户的镜像共享。 | To be tested |
|  | GlanceListImageMembers | 该接口用于共享镜像过程中,获取接受该镜像的成员列表。 | To be tested |
|  | GlanceUpdateImageMember | 用户接受或者拒绝共享镜像时,使用该接口更新镜像成员的状态。 | To be tested |
| 镜像复制 | CopyImageCrossRegion | 该接口为扩展接口,用户在一个区域制作的私有镜像,可以通过跨Region复制镜像将镜像复制到其他区域,在其他区域发放相同类型的云服务器,帮助用户实现区域间的业务迁移。 | To be tested |
|  | CopyImageInRegion | 该接口为扩展接口,主要用于用户将一个已有镜像复制为另一个镜像。复制镜像时,可以更改镜像的加密等属性,以满足不同的场景。 | To be tested |
| 镜像标签 | ListTags | 根据不同条件查询镜像标签列表信息。 | To be tested |
|  | BatchAddOrDeleteTags | 该接口用于为指定镜像批量添加/更新、删除标签。 | To be tested |
|  | AddImageTag | 该接口用于为指定镜像添加或更新指定的单个标签 | To be tested |
|  | BatchDeleteTags | 该接口用于为指定镜像批量删除标签。 | To be tested |
|  | ListImagesTags | 该接口用于为查询租户的所有镜像上的标签。 | To be tested |
|  | ListImageTags | 该接口用于为查询指定镜像上的所有标签 | To be tested |
|  | ListImageByTags | 该接口用于按标签或其他条件对镜像进行过滤或者计数使用。 | To be tested |
|  | CreateOrUpdateTags | 该接口主要用于为某个镜像增加或修改一个自定义标签。通过自定义标签,用户可以将镜像进行分类。 | To be tested |
|  | DeleteImageTag | 该接口用于为镜像删除指定的标签 | To be tested |
| 镜像标签(OpenStack原生) | GlanceDeleteTag | 该接口主要用于删除某个镜像的自定义标签,通过该接口,用户可以将私有镜像中一些不用的标签删除。 | To be tested |
|  | GlanceCreateTag | 该接口主要用于为某个镜像添加一个自定义标签。通过自定义标签,用户可以将镜像进行分类。 | To be tested |
| 镜像视图(OpenStack原生) | GlanceListImageSchemas | 该接口主要用于查询镜像列表视图,通过该接口用户可以了解到镜像列表的详细情况和数据结构。 | To be tested |
|  | GlanceListImageMemberSchemas | 该接口主要用于查询镜像成员列表视图,通过视图,用户可以了解到镜像成员包含哪些属性,同时也可以了解每个属性的数据类型。 | To be tested |
|  | GlanceShowImageMemberSchemas | 该接口主要用于查询镜像成员视图,通过视图,用户可以了解到镜像成员包含哪些属性,同时也可以了解每个属性的数据类型。 | To be tested |
|  | GlanceShowImageSchemas | 该接口主要用于查询镜像视图,通过视图,用户可以了解到镜像包含哪些属性,同时也可以了解每个属性的数据类型等。 | To be tested |
| 镜像配额 | ShowImageQuota | 该接口为扩展接口,主要用于查询租户在当前Region的私有镜像的配额数量。 | To be tested |

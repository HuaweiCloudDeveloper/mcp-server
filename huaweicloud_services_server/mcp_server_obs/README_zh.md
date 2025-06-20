# OBS MCP Server 

## 版本信息
v0.1.0

## 产品描述

OBS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务OBS交互的能力。可以基于自然语言对OBS资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

| 类别 | 工具名称 | 功能描述 | 状态 |
| --- | --- | --- | --- |
| 多段操作 | ListParts | 列举已上传的段 | To be tested |
|  | CopyPart | 拷贝段 | To be tested |
|  | CompleteMultipartUpload | 如果用户上传完所有的段,就可以调用合并段接口,系统将在服务端将用户指定的段合并成一个完整的对象。在执行“合并段”操作以前,用户不能下载已经上传的数据。在合并段时需要将多段上传任务初始化时记录的附加消息头信息拷贝到对象元数据中,其处理过程和普通上传对象带这些消息头的处理过程相同。在并发合并段的情况下,仍然遵循Last Write Win策略,但“Last Write”的时间定义为段任务的初始化时间。 | To be tested |
|  | AbortMultipartUpload | 取消多段上传任务 | To be tested |
|  | ListMultipartUploads | 列举桶中已初始化多段任务 | To be tested |
|  | UploadPart | 上传段 | To be tested |
|  | InitiateMultipartUpload | 初始化上传段任务 | To be tested |
| 对象操作 | DeleteObjects | 批量删除对象特性用于将一个桶内的部分对象一次性删除,删除后不可恢复。批量删除对象要求返回结果里包含每个对象的删除结果。OBS的批量删除对象使用同步删除对象的方式,每个对象的删除结果返回给请求用户。 | To be tested |
|  | UploadModifyObject | 修改写对象操作是指将指定文件桶内的一个对象从指定位置起修改为其他内容。 | To be tested |
|  | PutObject | 用户在OBS系统中创建了桶之后,可以采用PUT操作的方式将对象上传到桶中。上传对象操作是指在指定的桶内增加一个对象,执行该操作需要用户拥有桶的写权限。 | To be tested |
|  | SetObjectMetadata | 用户可以通过本接口添加、修改或删除桶中已经上传的对象的元数据。 | To be tested |
|  | SetObjectAcl | OBS支持对对象的操作进行权限控制。默认情况下,只有对象的创建者才有该对象的读写权限。用户也可以设置其他的访问策略,比如对一个对象可以设置公共访问策略,允许所有人对其都有读权限。SSE-KMS方式加密的对象即使设置了ACL,跨租户也不生效。 | To be tested |
|  | DeleteObject | 删除对象的操作。如果要删除的对象不存在,则仍然返回成功信息。 | To be tested |
|  | GetObjectMetadata | 拥有对象读权限的用户可以执行HEAD操作命令获取对象元数据,返回信息包含对象的元数据信息。 | To be tested |
|  | TruncateObject | 截断对象操作是指将指定文件桶内的一个对象截断到指定大小。 | To be tested |
|  | RestoreObject | 如果要获取归档存储对象的内容,需要先将对象取回,然后再执行下载数据的操作。对象取回后,会产生一个标准存储类型的对象副本,也就是说会同时存在标准存储类型的对象副本和归档存储类型的对象,在取回对象的保存时间到期后标准存储类型的对象副本会自动删除。 | To be tested |
|  | UploadObject | 上传对象操作是指在指定的桶内增加一个对象,执行该操作需要用户拥有桶的写权限。 | To be tested |
|  | GetObjectAcl | 用户执行获取对象ACL的操作,返回信息包含指定对象的权限控制列表信息。用户必须拥有对指定对象读ACP(access control policy)的权限,才能执行获取对象ACL的操作。 | To be tested |
|  | GetObject | GET操作从对象存储下载对象。使用GET接口前,请确认必须拥有对象的READ权限。如果对象Owner向匿名用户授予READ访问权限,则可以在不使用鉴权头域的情况下访问该对象。 | To be tested |
|  | RenameObject | 重命名对象操作是指将指定文件桶内的一个对象重命名为其他对象名。 | To be tested |
|  | AppendObject | 追加写对象操作是指在指定桶内的一个对象尾追加上传数据,不存在相同对象键值的对象则创建新对象。 | To be tested |
|  | CopyObject | 复制对象(Copy Object)特性用来为OBS上已经存在的对象创建一个副本。 | To be tested |
| 桶的基础操作 | GetBucketLocation | 对桶拥有读权限的用户可以执行获取桶区域位置信息的操作。 | To be tested |
|  | DeleteBucket | 删除桶操作用于删除用户指定的桶。只有桶的所有者或者拥有桶的删桶policy权限的用户可以执行删除桶的操作,要删除的桶必须是空桶。如果桶中有对象或者有多段任务则认为桶不为空,可以使用列举桶内对象和列举出多段上传任务接口来确认桶是否为空。 | To be tested |
|  | ListBuckets | OBS用户可以通过请求查询自己创建的桶列表。 | To be tested |
|  | CreateBucket | 创建桶是指按照用户指定的桶名创建一个新桶的操作。 | To be tested |
|  | ListVersions | 对桶拥有读权限的用户可以执行获取桶内多版本对象列表的操作。 | To be tested |
|  | ListObjects | 对桶拥有读权限的用户可以执行获取桶内对象列表的操作。 | To be tested |
|  | GetBucketMetadata | 对桶拥有读权限的用户可以执行查询桶元数据是否存在的操作。 | To be tested |
| 桶的高级配置 | DeleteDirectcoldaccess | 删除指定桶的归档对象直读配置信息。 | To be tested |
|  | SetBucketEncryption | OBS使用PUT操作为桶创建或更新默认服务端加密配置信息。 | To be tested |
|  | GetBucketPolicy | 该接口的实现使用policy子资源来将指定桶的策略返回给客户端。 | To be tested |
|  | SetBucketObsCompressPolicy | 本接口用于为指定桶配置ZIP文件解压策略。接口是幂等的,若桶上已存在相同策略内容,则返回成功,status code返回值为200;否则status code返回值为201。 | To be tested |
|  | SetDirectcoldaccess | 归档对象直读是指用户可以不用取回归档对象,便能直接对其进行操作。 | To be tested |
|  | GetBucketQuota | 桶的拥有者可以执行获取桶配额信息的操作。桶的拥有者的状态是inactive状态不可以查询桶配额信息。桶空间配额值的单位为Byte(字节),0代表不设上限。 | To be tested |
|  | DeleteBucketObsCompressPolicy | 本接口用于删除指定桶中配置的ZIP文件解压策略。删除成功,status code返回值为204。 | To be tested |
|  | DeleteBucketLifecycle | 删除指定桶的生命周期配置信息。删除后桶中的对象不会过期,OBS不会自动删除桶中对象。 | To be tested |
|  | SetBucketLifecycle | OBS系统支持指定规则来实现定时删除或迁移桶中对象,这就是生命周期配置。典型的应用场景如: | To be tested |
|  | SetBucketMirrorBackToSource | 本接口用于为指定桶配置镜像回源策略。接口是幂等的,若桶上已存在相同策略内容,则返回成功,status code返回值为200;否则status code返回值为201。 | To be tested |
|  | GetBucketLifecycle | 获取该桶设置的生命周期配置信息。 | To be tested |
|  | DeleteBucketEncryption | OBS使用DELETE操作来删除指定桶的加密配置。 | To be tested |
|  | SetBucketPolicy | 该接口的实现使用policy子资源创建或者修改一个桶的策略。如果桶已经存在一个策略,那么当前请求中的策略将完全覆盖桶中现存的策略。单个桶的桶策略条数(statement)没有限制,但一个桶中所有桶策略的JSON描述总大小不能超过20KB。 | To be tested |
|  | SetBucketReplication | 跨区域复制是指跨不同区域中的桶自动、异步地复制对象。通过激活跨区域复制,OBS可将新创建的对象及修改的对象从一个源桶复制到不同区域中的目标桶。 | To be tested |
|  | GetBucketStorageInfo |  | To be tested |
|  | ListBucketInventory | OBS使用不带清单id的GET操作来获取指定桶的所有清单配置,获取到的清单配置一次性返回,不分页。 | To be tested |
|  | GetBucketReplication | 获取指定桶的复制配置信息。执行该配置操作前需要确保执行者拥有GetReplicationConfiguration权限。 | To be tested |
|  | GetBucketMirrorBackToSource | 本接口用于查询指定桶的镜像回源策略。若策略存在,则返回成功,status code返回值为200。 | To be tested |
|  | DeleteBucketReplication | 删除桶的复制配置。执行该配置操作前需要确保执行者拥有DeleteReplicationConfiguration权限。 | To be tested |
|  | GetBucketInventory | OBS使用GET操作来获取指定桶的某个清单配置。 | To be tested |
|  | SetBucketInventory | OBS使用PUT操作为一个桶配置清单规则,每个桶最多可以配置10条清单规则,有关更多桶清单的介绍和使用限制,请参考《对象存储服务开发指南》的[桶清单](https://support.huaweicloud.com/ugobs-obs/obs_41_0044.html)章节。 | To be tested |
|  | GetBucketCustomdomain | OBS使用GET操作来获取桶的自定义域名。 | To be tested |
|  | DeleteBucketInventory | OBS使用DELETE操作来删除指定桶的清单配置(通过清单id来指定清单配置)。 | To be tested |
|  | SetBucketTagging | OBS使用PUT操作为一个已经存在的桶添加标签。 | To be tested |
|  | GetBucketVersioning | 桶的所有者可以获取指定桶的多版本状态。 | To be tested |
|  | DeleteBucketCustomdomain | OBS使用DELETE操作来删除指定桶的标签。 | To be tested |
|  | SetBucketVersioning | 多版本功能可在用户意外覆盖或删除对象的情况下提供一种恢复手段。用户可以使用多版本功能来保存、检索和还原对象的各个版本,这样用户能够从意外操作或应用程序故障中轻松恢复数据。多版本功能还可用于数据保留和存档。 | To be tested |
|  | SetBucketQuota | 桶空间配额值必须为非负整数,单位为Byte(字节),能设的最大值为2^63 -1。桶的默认配额为0,表示没有限制桶配额。 | To be tested |
|  | GetBucketAcl | 用户执行获取桶ACL的操作,返回信息包含指定桶的权限控制列表信息。用户必须拥有对指定桶READ_ACP的权限或FULL_CONTROL权限,才能执行获取桶ACL的操作。 | To be tested |
|  | SetBucketStoragePolicy | 本接口实现为桶创建或更新桶的默认存储类型配置信息。 | To be tested |
|  | SetBucketCustomedomain | OBS使用PUT操作为桶设置自定义域名,设置成功之后,用户访问桶的自定义域名就能访问到桶。 | To be tested |
|  | SetBucketNotification | OBS消息通知功能能够帮助您对桶的重要的操作及时通知到您,确保您安全、及时知道发生在桶上的关键事件。 | To be tested |
|  | GetBucketNotification | 获取指定桶的消息通知配置信息。 | To be tested |
|  | GetBucketEncryption | OBS使用GET操作来获取指定桶的加密配置。 | To be tested |
|  | DeleteBucketMirrorBackToSource | 本接口用于删除指定桶中配置的镜像回源策略。删除成功,status code返回值为204。 | To be tested |
|  | GetBucketObsCompressPolicy | 本接口用于查询指定桶的ZIP文件解压策略。若策略存在,则返回成功,status code返回值为200。 | To be tested |
|  | SetBucketLogging | 创建桶时,默认是不生成桶的日志的,如果需要生成桶的日志,该桶需要打开日志配置管理的开关。桶日志功能开启后,桶的每次操作将会产生一条日志,并将多条日志打包成一个日志文件。日志文件存放位置需要在开启桶日志功能时指定,可以存放到开启日志功能的桶中,也可以存放到其他你有权限的桶中,但需要和开启日志功能的桶在同一个region中。 | To be tested |
|  | GetBucketStoragePolicy | 获取该桶设置的默认存储类型信息。 | To be tested |
|  | GetDirectcoldaccess | 桶的所有者可以获取指定桶的归档对象直读状态。 | To be tested |
|  | GetBucketLogging | 该接口的目的是查询当前桶的日志管理配置情况。其实现是通过使用http的get方法再加入logging子资源来返回当前桶的日志配置情况。 | To be tested |
|  | GetBucketTagging | OBS使用GET操作来获取指定桶的标签。 | To be tested |
|  | DeleteBucketTagging |  | To be tested |
|  | SetBucketAcl | OBS支持对桶操作进行权限控制。默认情况下,只有桶的创建者才有该桶的读写权限。用户也可以设置其他的访问策略,比如对一个桶可以设置公共访问策略,允许所有人对其都有读权限。 | To be tested |
|  | DeleteBucketPolicy | 该接口的实现是通过使用policy子资源来删除一个指定桶上的策略。 | To be tested |
| 静态网站托管 | SetBucketCors | CORS(Cross Origin Resource Sharing),即跨域资源共享,是W3C标准化组织提出的一种规范机制,允许客户端的跨域请求的配置。在通常的网页请求中,由于安全策略SOP(Same Origin Policy)的存在,一个网站的脚本和内容是不能与另一个网站的脚本和内容发生交互的。 | To be tested |
|  | DeleteBucketWebsite | 删除指定桶的网站配置信息。 | To be tested |
|  | DeleteBucketCors | 删除指定桶的CORS配置信息。删除后桶以及桶中的对象将不能再被其他网址发送的请求访问。 | To be tested |
|  | GetBucketWebsite | 获取该桶设置的网站配置信息。 | To be tested |
|  | SetBucketWebsite | OBS允许在桶内保存静态的网页资源,如.html网页文件、flash文件、音视频文件等,当客户端通过桶的Website接入点访问这些对象资源时,浏览器可以直接解析出这些支持的网页资源,呈现给最终用户。典型的应用场景有: | To be tested |
|  | CheckBucketOptions | OPTIONS,称为预请求,是客户端发送给服务端的一种请求,通常被用于检测客户端是否具有对服务端进行操作的权限。只有当预请求成功返回,客户端才开始执行后续的请求。 | To be tested |
|  | CheckObjectOptions | OPTIONS,称为预请求,是客户端发送给服务端的一种请求,通常被用于检测客户端是否具有对服务端进行操作的权限。只有当预请求成功返回,客户端才开始执行后续的请求。 | To be tested |
|  | GetBucketCors | 获取指定桶的CORS配置信息。 | To be tested |

# 给某个华为云产品开发相应MCP服务
本文以云硬盘EVS产品开发MCP服务为例进行介绍，面向开源开发者。
基于产品对外提供的API接口，用 HuaweiCloud SDK 进行开发

## 了解业务功能
从华为云首页找到相应产品，进入文档学习[业务功能](https://support.huaweicloud.com/productdesc-evs/evs_01_0127.html) 以及 [API接口规格](https://support.huaweicloud.com/api-evs/evs_04_0001.html)。<br>

![alt text](images/20250522_103123.png) <br>

![alt text](images/20250522_103200.png)

## 调试API接口
华为云的产品提供有在线API调用体验和多语言的SDK代码。 
进入[API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/EVS/doc?api=CreateVolume)选择相应产品，根据输入参数会生成相应的代码， 调试可以看到运行效果。 <br>
如下图所示的代码是可以用来开放后续MCP服务的。
<br>
![alt text](images/20250522_103734.png)


## 开放MCP服务
### 构建开发环境
- 下载VSCode + Cline
- 下载当前项目代码根据ReadMe配置开发环境
- 具体编码参考已有evs_tools的代码
- ak/sk、log等功能复用已有代码 <br>
![alt text](images/20250522_104923.png)


## 验证MCP服务
### 通过Inspector进行代码级验证
[参考文档](https://modelcontextprotocol.io/docs/tools/inspector)
```shell
    npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```
![alt text](images/20250523_092603.png)

### 通过Cline进行自然语言级验证
[参考文档](https://docs.cline.bot/mcp/configuring-mcp-servers) <br>
![alt text](images/20250523_092726.png) <br>
![alt text](images/20250523_092806.png)

## 提交代码
### 创建类别为Feature的Issue描述开发内容
[创建Issue](https://github.com/HuaweiCloudDeveloper/mcp-server/issues)<br>
![alt text](images/20250523_095152.png)


### 创建PR提交代码给管理员检视合并
[创建PR](https://github.com/HuaweiCloudDeveloper/mcp-server/pulls)
<br>
![alt text](images/20250523_094838.png)

##
## 恭喜您完成MCP开发，谢谢你对华为云开源生态付出！！

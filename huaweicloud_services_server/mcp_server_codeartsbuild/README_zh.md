# CodeArtsBuild MCP Server 


## Version
v0.1.0

## Overview

CodeArtsBuild MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsBuild. Full-chain management of CodeArtsBuild resources can be carried out based on natural language.

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
                    <td rowspan="56">CodeArtsBuild</td>
                    <td>ListOfficialTemplate</td>
                    <td>查询官方模版</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobListByProjectId</td>
                    <td>查看项目下用户的构建任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadBuildLog</td>
                    <td>下载全量构建日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKeystorePermission</td>
                    <td>文件管理查询权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildRecord</td>
                    <td>查询指定构建记录详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBuildJob</td>
                    <td>创建构建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobConfig</td>
                    <td>获取构建任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildParamsList</td>
                    <td>编辑页获取参数类型的接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableBuildJob</td>
                    <td>恢复构建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListHistory</td>
                    <td>查看构建任务的构建历史列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBuildJob</td>
                    <td>停止构建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectJobs</td>
                    <td>查询项目任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobConfigDiff</td>
                    <td>获取构建任务配置的对比差异</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBuildJob</td>
                    <td>更新构建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDefaultBuildParameters</td>
                    <td>获取编译构建默认参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotice</td>
                    <td>查询通知</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplates</td>
                    <td>创建构建模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageTemplateList</td>
                    <td>获取镜像模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowListPeriodHistory</td>
                    <td>根据开始时间和结束时间查看构建任务的构建历史列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecyclingJob</td>
                    <td>查看回收站中删除的构建任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobConfig</td>
                    <td>获取构建任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRelatedProjectInfo</td>
                    <td>获取项目列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadTaskLog</td>
                    <td>下载构建步骤日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDockerfileTemplate</td>
                    <td>获取dockerfileTemplate</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBuildInfoRecordByJobId</td>
                    <td>获取任务构建记录列表v1</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectPermission</td>
                    <td>获取用户权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBuildInfoRecord</td>
                    <td>获取任务构建记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobBuildSuccessRatio</td>
                    <td>查询构建成功率</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadRealTimeLog</td>
                    <td>下载构建实时日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobSystemParameters</td>
                    <td>查看系统预定义参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckJobNameIsExists</td>
                    <td>查看项目下任务名是否存在</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadKeystoreByName</td>
                    <td>文件管理文件下载</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildRecordBuildScript</td>
                    <td>获取构建记录的构建脚本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableBuildJob</td>
                    <td>禁用构建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRunningStatus</td>
                    <td>查看任务是否在构建</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobSuccessRatio</td>
                    <td>根据开始时间和结束时间查看构建任务的构建成功率</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLastHistory</td>
                    <td>查询指定代码仓库最近一次成功的构建历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunJob</td>
                    <td>执行构建任务,可传自定义参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordDetail</td>
                    <td>获取构建记录信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplates</td>
                    <td>删除构建模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobBuildTime</td>
                    <td>洞察构建时长</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBuildJob</td>
                    <td>删除构建任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecords</td>
                    <td>获取指定工程的构建记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowReportSummary</td>
                    <td>获取覆盖率接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKeystore</td>
                    <td>查询用户可使用文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildRecordFullStages</td>
                    <td>获取任务各阶段信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRelatedProject</td>
                    <td>获取当前用户的项目信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOutputInfo</td>
                    <td>获取构建产物详情信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowYamlTemplate</td>
                    <td>获取代码化构建默认模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableNotice</td>
                    <td>取消通知</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHistoryDetails</td>
                    <td>获取构建历史详情信息接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobNoticeConfigInfo</td>
                    <td>获取通知信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadKeystore</td>
                    <td>下载指定租户下的KeyStore文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBuildInfoRecord</td>
                    <td>获取任务构建记录列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobRolePermission</td>
                    <td>获取构建任务的角色权限矩阵信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotice</td>
                    <td>更新通知</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job管理</td>
                    <td>ShowJobStatus</td>
                    <td>查询job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Offline</td>
                    <td>ShowRecordInfo</td>
                    <td>获取构建记录信息(待下线)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadLogByRecordId</td>
                    <td>下载构建日志(待下线)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlowGraph</td>
                    <td>获取构建记录的有向无环图(待下线)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">作业管理接口</td>
                    <td>StopJob</td>
                    <td>在MRS集群中终止指定作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">后台任务管理</td>
                    <td>ShowJobInfo</td>
                    <td>查询租户Job执行结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">项目信息</td>
                    <td>ListTemplates</td>
                    <td>查询项目模板</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

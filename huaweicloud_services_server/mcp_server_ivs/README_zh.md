# IVS MCP Server 


## Version
v0.1.0

## Overview

IVS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IVS. Full-chain management of IVS resources can be carried out based on natural language.

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
                    <td rowspan="4">人证核身标准版(三要素)</td>
                    <td>DetectStandardByNameAndId</td>
                    <td>使用姓名、身份证号文本和人脸图片进行三要素身份审核。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectStandardByIdCardImage</td>
                    <td>使用身份证正反面图片提取姓名和身份证号码,与人脸图片进行三要素身份审核。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectStandardByVideoAndIdCardImage</td>
                    <td>从身份证正反面图片中提取姓名和身份证号码,并对视频做活体检测后提取人脸图片,以此进行三要素身份审核。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectStandardByVideoAndNameAndId</td>
                    <td>使用姓名、身份证号文本,并对视频做活体检测后提取人脸图片,以此进行三要素身份审核。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">人证核身证件版(二要素)</td>
                    <td>DetectExtentionByNameAndId</td>
                    <td>使用姓名、身份证号码二要素进行身份审核。身份验证时,传入的数据为身份证信息。提取身份证信息时,可以使用身份证正反面图片,也可以直接输入姓名、身份证号文本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetectExtentionByIdCardImage</td>
                    <td>使用姓名、身份证号码二要素进行身份审核。身份验证时,传入的数据为身份证信息。提取身份证信息时,可以使用身份证正反面图片,也可以直接输入姓名、身份证号文本。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>

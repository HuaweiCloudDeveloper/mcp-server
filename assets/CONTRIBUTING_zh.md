# 贡献

欢迎为 mcp-server 项目贡献力量！请先阅读本指南，了解贡献流程和规范。

## 贡献流程

### 1. Fork 仓库

- 点击 GitHub 仓库页面的右上角 `Fork` 按钮，创建属于你的副本。

### 2. 克隆仓库到本地

```bash
git clone https://github.com/your-username/mcp-server.git
cd mcp-server
```

### 3. 添加上游仓库（可选，便于后续同步）

```bash
git remote add upstream https://github.com/HuaweiCloudDeveloper/mcp-server.git
```

### 4. 创建新分支

- **分支命名建议**：`add-xxx`（新增功能）、`fix-xxx`（修复问题）

```bash
git checkout -b add-new-feature
```

### 5. 提交代码

```bash
git commit -s -m "This is my commit message"  
```

### 6. 推送分支到你的仓库

```bash
git push origin add-new-feature
```

### 7. 创建 Pull Request (PR)

- 访问原仓库的 GitHub 页面，点击 `New pull request`，选择开发的分支。
- 按照PR模板提供信息。
- 如果有相关 Issue,需要关联 Issue 编号，如 `#123`

### 8.审核并合并

- 维护团队将对您的 PR 进行审核，期间可能会提出改进意见或要求补充说明。审核通过后，您的代码将被合并至项目主仓库。

## 反馈与问题

如果您遇到任何问题或有改进的想法，建议使用 GitHub Issues 来提交问题和反馈，因为 GitHub Issues 是可追踪的：

- 首先通过现有的 GitHub Issues 中搜索答案。如果找到相关主题，请在 Issues 上发表评论。
- 如果所有问题都不相关，请将问题添加到GitHub Issue。请根据问题模板提供任何相关信息。

感谢您的贡献！

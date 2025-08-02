# Contributing

Welcome to contribute to the mcp-server project! Please read this guide carefully to understand the contribution process
and standards.

## Contribution Process

### 1. Fork the Repository

- Click the `Fork` button at the top-right corner of the GitHub repository page to create your own copy.

### 2. Clone the Repository Locally

```bash  
git clone https://github.com/your-username/mcp-server.git  
cd mcp-server  
```  

### 3. Add Upstream Repository (Optional, for syncing updates)

```bash  
git remote add upstream https://github.com/HuaweiCloudDeveloper/mcp-server.git 
git remote set-url --push upstream no-pushing 
```  

### 4. Create a New Branch

- **Branch Naming Convention**: `add-xxx` (new feature), `fix-xxx` (bug fix)

```bash  
git checkout -b add-new-feature  
```  

### 5. Commit Code Changes

```bash  
git commit -s -m "This is my commit message"  
```  

### 6. Push Branch to Your Forked Repository

```bash  
git push origin add-new-feature  
```  

### 7. Create a Pull Request (PR)
PR is the only way to make change to mcp-server project. Before submitting a pull request, ensure your local Git repository is synchronized with the mcp-server repository to avoid merge conflicts.
- Go to the original repository's GitHub page, click `New pull request`, and select your development branch.
- Follow the PR template to provide necessary details.
- If related to an existing Issue, reference the Issue number (e.g., `#123`).

### 8. Review and Merge

- Your pull request will be reviewed by the maintainers. They may suggest changes or ask for clarification. Once the
  review is complete, your changes will be merged into the main project.

## Feedback & Issues

If you encounter issues or have suggestions, please use GitHub Issues for tracking:

- Search through existing open and closed GitHub Issues for the answer first. If you find a relevant topic, please
  comment on the issue.
- If none of the issues are relevant, please add an issue to GitHub issues. Please provide any relevant information as
  suggested by the Issue template.

Thank you for your contributions! 
@echo off
chcp 65001 >nul
echo ========================================
echo    Git 初始化并推送到 GitHub
echo ========================================
echo.

set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

REM 检查是否在git仓库中
if not exist ".git" (
    echo [1/4] 初始化 Git 仓库...
    git init
    git branch -M main
)

REM 检查远程仓库
git remote -v | findstr "origin" >nul
if errorlevel 1 (
    echo.
    echo 请先在 GitHub 上创建仓库，然后运行:
    echo   git remote add origin https://github.com/你的用户名/ollama-web.git
    echo.
    echo 或者直接在下面输入仓库地址:
    set /p repo_url=仓库地址: 
    git remote add origin !repo_url!
)

echo [2/4] 添加文件...
git add .

echo [3/4] 提交文件...
git status | findstr "No commits yet" >nul
if not errorlevel 1 (
    git commit -m "Initial commit: Ollama Web 界面工具"
) else (
    git commit -m "Update: Ollama Web 界面工具"
)

echo [4/4] 推送到 GitHub...
echo.
echo 如果是第一次推送，可能需要输入 GitHub 用户名和令牌
echo.
git push -u origin main

echo.
echo ========================================
echo   推送完成！
echo ========================================
echo.
pause

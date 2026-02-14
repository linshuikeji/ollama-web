@echo off
chcp 65001 >nul
echo ========================================
echo    推送到 GitHub
echo ========================================
echo.

cd /d "%~dp0"

echo 正在推送到 GitHub...
echo.

git push -u origin main

if errorlevel 1 (
    echo.
    echo 推送失败！请检查:
    echo 1. GitHub 账号是否已登录
    echo 2. 是否有仓库访问权限
    echo.
    echo 可以尝试运行:
    echo   git remote -v
    echo   查看远程仓库地址是否正确
    echo.
) else (
    echo.
    echo ========================================
    echo   推送成功！
    echo ========================================
    echo.
    echo 仓库地址: https://github.com/linshuikeji/ollama-web
    echo.
)

pause

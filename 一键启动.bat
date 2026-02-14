@echo off
chcp 65001 >nul
echo ========================================
echo    Ollama 本地模型工具 - 一键启动
echo ========================================
echo.

set PROJECT_DIR=%~dp0
cd /d "%PROJECT_DIR%"

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python，请先安装 Python 3.8+
    pause
    exit /b 1
)

REM 创建虚拟环境
if not exist "venv" (
    echo [1/4] 创建虚拟环境...
    python -m venv venv
    if errorlevel 1 (
        echo [错误] 创建虚拟环境失败
        pause
        exit /b 1
    )
)

REM 激活虚拟环境
echo [2/4] 激活虚拟环境...
call venv\Scripts\activate.bat

REM 安装依赖
echo [3/4] 安装依赖...
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo [错误] 安装依赖失败
    pause
    exit /b 1
)

REM 检查 Ollama
echo [4/4] 检查 Ollama 服务...
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo.
    echo [警告] Ollama 服务未运行
    echo 请先运行: ollama serve
    echo (如果没有安装 Ollama，请先下载安装)
    echo.
    choice /C YN /M "是否继续启动？(不保证能正常工作)"
    if errorlevel 2 goto :eof
)

echo.
echo ========================================
echo   启动成功！
echo ========================================
echo.
echo 访问地址: http://localhost:5000
echo.
echo 按 Ctrl+C 停止服务
echo.

python app.py

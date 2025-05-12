@echo off
echo Cleaning previous builds...
rmdir /s /q dist
rmdir /s /q build
for /d %%d in (*.egg-info) do rmdir /s /q "%%d"

echo Building distribution...
python -m build
if %errorlevel% neq 0 (
    echo Build failed
    exit /b %errorlevel%
)

echo Uploading to TestPyPI...
python -m twine upload --repository testpypi dist/*
if %errorlevel% neq 0 (
    echo Upload failed
    exit /b %errorlevel%
)

echo Done! Now you can test it with:
python setup.py --version

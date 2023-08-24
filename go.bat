@echo off
py .\version\update_version.py update
@echo on
::<cmd>start go.bat
git add .
git commit -m "check now"
git push line_bot main
@echo off
py .\version\update_version.py now

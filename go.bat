@echo off
py .\version\update_version.py update
@echo on
::<cmd>start go.bat
git add .
git commit -m "first push"
git push origin second
@echo off
py .\version\update_version.py now

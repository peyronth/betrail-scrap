@echo off

rem Ask for commit message
set /p commit_message="Entrez votre message de commit : "

rem Getting dev...
git fetch origin dev
git checkout dev
git pull origin dev

rem Getting master...
git fetch origin master
git checkout master
git pull origin master

rem Merge dev into master...
git merge dev

rem Build the app...
pyinstaller main.spec --noconfirm

rem Compress the app...
powershell Compress-Archive -Path .\dist\main\ -DestinationPath .\dist\race-scrap.zip

rem Run tests...
python test.py

rem Update master...
git add .
git commit -m "%commit_message%"
git push origin master

rem Create tag...
git tag -a "%commit_message%" -m "%commit_message%"
git push origin "%commit_message%"

rem Checkout dev...
git checkout dev

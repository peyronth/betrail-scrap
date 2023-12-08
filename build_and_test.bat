@echo on

rem Fetch, checkout et pull la branche git dev
git fetch origin dev
git checkout dev
git pull origin dev

rem Fetch, checkout et pull main
git fetch origin master
git checkout master
git pull origin master

rem Merge dev dans main
git merge dev

rem Build l'app avec PyInstaller
pyinstaller main.spec --noconfirm

rem Créer le dossier /dist/main/ dans un zip app.zip
powershell Compress-Archive -Path .\dist\main\ -DestinationPath .\app.zip

rem Run test.py
python test.py

rem Git add, commit et push sur master
set /p commit_message="Entrez votre message de commit : "
git add .
git commit -m "%commit_message%"
git push origin master

rem Créer un tag avec le message de commit
git tag -a "%commit_message%" -m "%commit_message%"
git push origin "%commit_message%"

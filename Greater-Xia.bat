@echo off
setlocal enabledelayedexpansion
:: AI Generative Code I don't use Winslops

if not exist "Novels" mkdir Novels
if not exist "Original_Novels" mkdir Original_Novels

del script.log 2>nul
echo Starting script... > script.log

for %%f in (*.epub) do (
    set "epub_file=%%f"
    set "folder_name=%%~nf"
    set "novel_path=Novels\!folder_name!"

    echo ------------------------------------------------
    echo Processing: !epub_file!
    echo Processing: !epub_file! >> script.log

    if exist "!folder_name!" rd /s /q "!folder_name!"
    if exist "!novel_path!" rd /s /q "!novel_path!"
    if exist "!folder_name!.epub" del /q "!folder_name!.epub"

    echo Unzipping...
    powershell -Command "Expand-Archive -LiteralPath '!epub_file!' -DestinationPath '!folder_name!' -Force"

    echo Moving to Novels folder...
    move "!folder_name!" "Novels\"

    echo Running Great-Xia.py...
    python "Great-Xia.py" "!novel_path!" >> script.log 2>&1

    echo Zipping back up...
    pushd "!novel_path!"
        powershell -Command "Compress-Archive -Path * -DestinationPath '..\!folder_name!.epub' -Force"
    popd

    echo Moving original...
    move "!epub_file!" "Original_Novels\"
)

echo ------------------------------------------------
echo All done.
pause

run, %A_ScriptDir%\programs\splash\splash.exe
SetWorkingDir, %A_ScriptDir%
IfNotExist "%a_windir%\fonts\Angsima.ttf"
	filecopy %A_ScriptDir%\programs\fonts\*.ttf, %windir%\fonts
run, %A_ScriptDir%\programs\GoogleChromePortable\GoogleChromePortable.exe 
run, %A_ScriptDir%\programs\GoldenDictPortable\GoldenDictPortable.exe
run, %comspec% /c  "%A_ScriptDir%\programs\PythonPortable\App\Python\python.exe" "%A_ScriptDir%\server.py",,hide

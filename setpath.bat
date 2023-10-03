@echo off <br>
setlocal<br>
setlocal enabledelayedexpansion<br>
@echo off<br>
:: search for Scripts folder that resides in : C:\Users\User Name\AppData\Roaming\Python\Python*\Scripts<br><br><br>
for /d /r "%USERPROFILE%" %%j in (Python) do (<br>
    for /D %%i in ("%%j\Python*") do (<br>
      for /D %%d in ("%%i\Scripts") do (<br>
                @if exist "%%d" (<br>
                    @set _variable=%%d<br>
                    @echo !_variable!<br>
                    ::SET Path here<br>
                    setx path %%d<br>
                )<br>
      )<br>
    )<br>
)<br>
<br><br><br>
endlocal<br>
pause<br>
for /f "tokens=5" %%a in ('netstat -aon ^| find ":27017" ^| find "LISTENING"') do taskkill /f /pid %%a
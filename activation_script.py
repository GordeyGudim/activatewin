import ctypes

def run_as_admin(command):
    ctypes.windll.shell32.ShellExecuteW(
        None, 
        "runas",
        "powershell.exe", 
        f"-NoExit -Command {command}",  # Добавлен -NoExit
        None, 
        5
    )

try:
    run_as_admin("irm https://get.activated.win | iex")

except:    
    run_as_admin("iex (curl.exe -s --doh-url https://1.1.1.1/dns-query https://get.activated.win | Out-String)")
import subprocess
import platform

# ----------------- EXPERIMENTAL ----------------- #
# ------------- USE AT YOUR OWN RISK ------------- #

def linuxMode():
    getArgs = ['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme']

    currentTheme = subprocess.run(
        getArgs, capture_output=True
    ).stdout.decode("utf-8").strip().strip("'")

    darkIndicator = '-dark'
    if currentTheme.endswith(darkIndicator):
        return True
    return False

def macMode():
    cmd = 'defaults read -g AppleInterfaceStyle'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
    return bool(p.communicate()[0])

def windowsMode(): 
    try:
        import winreg
    except ImportError:
        return False
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    reg_keypath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError:
        return False

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == 'AppsUseLightTheme':
                return value == 0
        except OSError:
            break
    return False

if platform.system() == 'Darwin':
    if macMode():
        print('Mac - Dark Mode')
    if not macMode():
        print('Mac - Light Mode')

if platform.system() == 'Windows':
    if windowsMode():
        print('Windows - Dark Mode')
    if not windowsMode():
        print('Windows - Light Mode')

if platform.system() == 'Linux':
	if linuxMode():
		print('Linux - Dark Mode')
	if not linuxMode():
		print('Linux - Light Mode')
        
import platform
import requests
import zipfile

if platform.system() == "Linux":
    print("running on linux... downloading platform-tools")
    r = requests.get('https://dl.google.com/android/repository/platform-tools-latest-linux.zip', allow_redirects=True)
    open('platform-tools.zip', 'wb').write(r.content)

elif platform.system() == "Windows":
    print("running on linux... downloading platform-tools")
    r = requests.get('https://dl.google.com/android/repository/platform-tools-latest-windows.zip', allow_redirects=True)
    open('platform-tools.zip', 'wb').write(r.content)

elif platform.system() == "Darwin":
    print("running on linux... downloading platform-tools")
    r = requests.get('https://dl.google.com/android/repository/platform-tools-latest-darwin.zip', allow_redirects=True)
    open('platform-tools.zip', 'wb').write(r.content)

with zipfile.ZipFile("platform-tools.zip","r") as zip_ref:
    zip_ref.extractall(".")

print("extracted platform-tools\n")

print("getting latest magisk")
r = requests.get("https://magiskmanager.com/go/download", allow_redirects=True)
open("magisk.apk", 'wb').write(r.content)
open("magisk.zip", 'wb').write(r.content)


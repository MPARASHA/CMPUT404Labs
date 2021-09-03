import requests 

print("Version of Library: "+ requests.__version__)
url = "https://google.com"
res = requests.get(url)

print("\nHTML Status Code: "+ str(res.status_code))
print("\nBody of Request: \n\n" + res.text)
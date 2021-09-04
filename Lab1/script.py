import requests 

print("\nVersion of Requests Library: "+ requests.__version__)
urlGoogle = "https://google.com"
resGoogle = requests.get(urlGoogle)

urlScript = "https://raw.githubusercontent.com/MPARASHA/CMPUT404Labs/master/Lab1/script.py"
resScript = requests.get(urlScript)

print("\nHTML Status Code: "+ str(resScript.status_code))
print("\nBody of Request: \n\n" + resScript.text)
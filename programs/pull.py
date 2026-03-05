import requests
response = requests.get("https://api.github.com/repos/Kubernetes/Kubernetes/pulls")
completeDetail= response.json()
for i in range(len(completeDetail)):
    print(completeDetail[i]["user"]["login"])


import requests, sys

if len(sys.argv) <= 1:
    print(f"python3 {sys.argv[0]} http[s]://url")
    sys.exit(1)

burp = {"http": "http://127.0.0.1:8080"}

#ports = {21,22,23,25,139,445,443,80,8080,3306,5432,8000,8888,8443,3389,5985}
#You can change the ports below to common ports set above.
ports = range(65536)

for port in ports:
        url = f'{sys.argv[1]}:{port}'
        try:
            req = requests.get(url, timeout=1, proxies=burp)
            if req.text:
                print("Porta aberta:", url)
                print()
                print(req.text)
        except requests.exceptions.RequestException:
            continue


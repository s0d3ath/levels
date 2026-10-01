import requests

codes = [200,301,404,403,500]

for code in codes:
    url = f"https://httpbin.org/status/{code}"
    response = requests.get(url, allow_redirects=False)
    status = response.status_code

    if status == 200:
        msg = "ok"
    elif 400 < status < 500:
        msg = "Error client"
    elif status == 500:
        msg = "Error server"
    else:
        msg = "hz"

    print(f"Запросили {code} -> получили {status} -> {msg}")
import requests
response = requests.get("https://example.com")
if response.status_code != 200:
    print(f"Ошибка при запросе:{response.status_code}")
    print(f"Ответ сервера:{response.text[:500]}")
    exit()
print(f"Статус-код: {response.status_code}")
print(f"Длина HTML: {len(response.text)} символов")
print(f"Первые 300 символов: {response.text[:300]}")
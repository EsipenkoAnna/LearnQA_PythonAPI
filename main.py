import requests
print("123")

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)


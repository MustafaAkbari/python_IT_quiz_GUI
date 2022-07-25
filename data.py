import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
# response_text = response.text
# print(response_text)
question_data = response.json()["results"]
# print(question_data)


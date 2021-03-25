
import requests
import json

try:
    request_url = "https://api.victoriassecret.com/settings/v1/languages?activeCountry=US"
    response = requests.get(request_url)
    response_result = response.json()

    print(response_result)

    status_one = response_result
    print(status_one)

    for item in status_one:
        print(str(item))


except AssertionError as e:
    print(e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('main')



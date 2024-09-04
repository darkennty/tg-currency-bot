import requests

JOKES_API_BASE_URL = 'https://v2.jokeapi.dev/joke/Any'

def get_joke(joke_type: str | None = None): # may be any value of type 'str' or may be None, and by default it is initialized to None
    url = JOKES_API_BASE_URL

    if joke_type is not None:
        params: dict = {'type': joke_type}
    else:
        params = {'type': 'single'}

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None
    json_data: dict = response.json()
    if json_data.get("error"):
        return # return None

    if params['type'] == 'single':
        return json_data["joke"]
    else:
        return json_data["setup"], json_data["delivery"]

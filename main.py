import requests
import json
import praw

from Infra.api_wrapper import APIWrapper




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_wrapper = APIWrapper()
    token = api_wrapper.get_token()
    headers = api_wrapper.get_auth_header(token)
    res = requests.get('https://oauth.reddit.com/api/v1/me',headers=headers).json()
    # print(res)
    request_test = api_wrapper.api_get_request('https://oauth.reddit.com/api/v1/me')
    print(headers)

    subreddit_info_url = 'https://www.reddit.com/r/QAutomation/about.json'
    create_collection_url = 'https://oauth.reddit.com/api/v1/collections/create'

    collections_list= 'https://oauth.reddit.com/api/v1/collections/1biuyuz'
    col_res = requests.get(collections_list, headers=headers)
    print(col_res.json())

    # Fetching subreddit information to get the fullname
    response = requests.get(subreddit_info_url, headers=headers)


    # Checking the response
    if response.status_code == 200:
        subreddit_info = response.json()
        subreddit_fullname = subreddit_info['data']['name']

        # Data for creating a collection
        collection_data = {
            'title': 'My Collection',  # Title of your collection
            'sr_fullname': 't5_b1hwji',  # Subreddit fullname where you want to create the collection
            'visibility': 'hidden'  # 'hidden' or 'private' or 'public'
        }

        # Making the request to create the collection
        response = requests.post(create_collection_url, headers=headers, data=collection_data)

        # Checking the response
        if response.status_code == 200:
            print("Collection created successfully!")
            print(json.dumps(response.json(), indent=4))  # Printing response data
        else:
            print("Failed to create collection. Status code:", response.status_code)
            print("Error response:", response.text)
    else:
        print("Failed to fetch subreddit information. Status code:", response.status_code)
        print("Error response:", response.text)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

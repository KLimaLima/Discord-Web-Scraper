import requests
import json

# get this in typing
auth_id: str = ''

# get this in message limit when refreshing
channel_link = ''

def retrieve_messages():#channel_id):

    headers = {
        'authorization': auth_id
    }

    response = requests.get(
        channel_link,
        headers= headers
    )

    result = json.loads(response.text)

    for message in result:
        print(message['content'], '\n')

retrieve_messages()
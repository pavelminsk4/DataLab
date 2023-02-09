import requests

def get_publications(report_id, auth_token):
    url = "https://api2.tweetbinder.com/reports/" + report_id + "/output"

    payload={}
    headers = {
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

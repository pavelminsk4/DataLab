import requests

def get_report_state(report_id, auth_token):
    url = "https://api2.tweetbinder.com/reports/" + report_id

    payload={}
    headers = {
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

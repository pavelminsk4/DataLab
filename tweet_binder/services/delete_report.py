import requests
import json

def delete_report(auth_token, report_id):
    url = "https://api2.tweetbinder.com/reports/" + report_id

    payload = json.dumps({
    "$set": {
        "status": "deleted"
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

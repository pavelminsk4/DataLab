import requests

def get_report_stats(report_code):
    url = "https://s3.eu-west-1.amazonaws.com/stats.tweetbinder.com/{report_code}/stats.json"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

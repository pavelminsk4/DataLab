import requests

def get_report_new_tweets(report_id, auth_token, start_date):
    url = f'https://api2.tweetbinder.com/reports/{report_id}/transcript/tweets?updatedAt=gt|{start_date}'
    
    payload = {}
    headers = {
                'Authorization': 'Bearer ' + auth_token
              }

    response = requests.request('GET', url, headers=headers, data=payload)
    return response.text

def get_report_new_tweets_next_page(report_id, auth_token, next_results, start_date):
    url = f'https://api2.tweetbinder.com/reports/{report_id}/transcript/tweets?updatedAt=gt|{start_date}{next_results}'

    payload = {}
    headers = {
                'Authorization': 'Bearer ' + auth_token
              }

    response = requests.request('GET', url, headers=headers, data=payload)
    return response.text

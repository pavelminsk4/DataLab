import requests

def get_user_tracker_stats(user_tracker_id, start_date, end_date, auth_token):
    url = f"https://api2.tweetbinder.com/user-trackers/{user_tracker_id}/stats?startDate={start_date}&endDate={end_date}"

    payload={}
    headers = {
    'Authorization': 'Bearer ' + auth_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

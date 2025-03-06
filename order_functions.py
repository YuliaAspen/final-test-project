import requests
import configuration
import data

def post_new_order():
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.order_body,
        headers=data.headers
    )

def get_order_by_track(track_number):
    return requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params={'t': track_number},
        headers=data.headers
    )

response = post_new_order()
response_json = response.json()
new_oreder_track = response_json.get("track")
response2 = get_order_by_track(new_oreder_track)

print("Status Code:", response.status_code)
print("Response JSON:", response_json)
print("New order track:", new_oreder_track)
print("Status Code:", response2.status_code)
print("Order Details:", response2.json())
import requests
from datetime import datetime

# TODO 1 UPDATE KEYES
NUT_APP_ID = "XXX"
NUT_APP_KEY = "XXX"
NUT_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# TODO 2 UPDATE SHEETY ENDPOINT
SHEET_ENDPOINT = "XXX"
QUERY = input("What exercises have you done? ")
time_now = datetime.now()
time = str(time_now.strftime("%X"))
headers = {
    "x-app-id": NUT_APP_ID,
    "x-app-key": NUT_APP_KEY,
}
sheet_header = {
    # TODO 3 UPDATE BEARER TOKEN
    "Authorization": "Bearer XXX",
    "Content-Type": "application/json",
}
nut_params = {
    "query": QUERY,
    # TODO 4 UPDATE INFO
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 187,
    "age": 23,
}


post = requests.post(url=NUT_ENDPOINT, headers=headers, data=nut_params)
sheet_dict = {}
for i in range(0, len(post.json()["exercises"])):
    item = post.json()["exercises"][i]
    sheet_params = {
        "workout": {
            "date": str(time_now.date()),
            "time": time,
            "exercise": item["name"],
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    sheet_post = requests.post(url=SHEET_ENDPOINT, headers=sheet_header, json=sheet_params)
    print(sheet_post.json())


# sheet_dict["Exercise"] = item["name"]
# sheet_dict["Duration"] = item["duration_min"]

# item = post.json()["exercises"][0]
# sheet_params = {
#     "workout": {
#         "date": str(time_now.date()),
#         "time": str(time_now.time()),
#         "exercise": item["name"],
#         "duration": item["duration_min"],
#         "calories": item["nf_calories"],
#     }
# }
# sheet_post = requests.post(url=SHEET_ENDPOINT, headers=sheet_header, json=sheet_params)
# print(sheet_post.json())

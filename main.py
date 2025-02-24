import requests
from datetime import datetime
USERNAME = YOUR_USERNAME
TOKEN = YOUR_TOKEN
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph3"
#------STEP 1: CREATION OF THE USERNAME, TOKEN UNCOMMENT THE RESPONSE AND PRINT THEN IN NEXT STEP COMMENT AGAIN STEP1 RESPONSE AND PRINT-------------#
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
    
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#------STEP 2 :GENERATING GRAPH UNCOMMENT THE RESPONSE AND PRINT THEN IN NEXT STEP COMMENT AGAIN STEP1 RESPONSE AND PRINT-------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Time spent in gym",
    "unit" : "Hours",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#------STEP 3 :POLTTING OF THE PXELS ONTO THE GRAPH THE RESPONSE AND PRINT THEN IN NEXT STEP COMMENT AGAIN STEP2 RESPONSE AND PRINT-------------#
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today= datetime.today()
# print(today.strftime("%Y%m%d"))
pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : float(input("How many hours you spent learning ? \n"))
}

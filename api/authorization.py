#These functions are for the polarAccesslink api authentication.
#Polar uses Oauth2 protocol for authorization
#More info at https://www.polar.com/accesslink-api/#authentication

import requests

def getToken():
    #This function prints access token and user id, which are needed to get users data from Polars api

    url = "https://polarremote.com/v2/oauth2/token"

    payload='grant_type=authorization_code&code=[code from https://flow.polar.com/oauth2/authorization?response_type=code&client_id=your_client_id]'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json',
      'Authorization': 'Basic [put here "client_id:client_secret" on base64 encoded]',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def registerUser():
    #Before request could be done, user must be registered 

    payload = "<register>\r\n  <member-id>User_id_[your_user_id]</member-id>\r\n</register>"
    
    headers = {
      'Content-Type': 'application/xml',  'Accept': 'application/json',  'Authorization': 'Bearer [token from authorization.getToken()]'
    }

    r = requests.post('https://www.polaraccesslink.com/v3/users', headers = headers, data=payload)

    if r.status_code >= 200 and r.status_code < 400:
        print(r.text)
    else:
        print(r.text)
import requests
import json




def getTransactionId():
    url = "https://www.polaraccesslink.com/v3/users/{your-user-id}/exercise-transactions"

    headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer [token from authorization.getToken()]'
    }

    response = requests.request("POST", url, headers=headers)

    print(response)
    print(response.text)

    if response.status_code == 201:
        transactionid = int(response.json()["transaction-id"])
    elif response.status_code == 204:
        transactionid = 0     # 0 means that there is no new training data.

    return transactionid

    



def listExercisesAndFindKilometers(transactionid):
    combinedDistance = 0
    url = "https://www.polaraccesslink.com/v3/users/{your-user-id}/exercise-transactions/{transaction_id}".format(transaction_id=transactionid)

    headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer [token from authorization.getToken()]'
    }

    response = requests.get(url, headers=headers)

    print(response)
    print(response.text)

    
    if response.status_code == 200:
        exercisesList = response.json()["exercises"]
        for exerciseURL in exercisesList:
            exerciseSummary = getExerciseSummary(exerciseURL)
            if exerciseSummary["detailed-sport-info"] == "E_BIKE":
                combinedDistance = combinedDistance + exerciseSummary["distance"]
        return combinedDistance




def getExerciseSummary(exerciseURL):
    url = exerciseURL
    headers = {
        'Accept': 'application/json',  'Authorization': 'Bearer [token from authorization.getToken()]'
    }
    response = requests.get(url, headers=headers)

    print(response)
    print(response.text)

    return response.json()

def collectKilometers(transactionid):
    distanceInMeters = listExercisesAndFindKilometers(transactionid)
    kilometers = distanceInMeters/1000   #m → km
    return kilometers

def commitTransaction(transactionid):
    #This function is for that program ends transaction with polaracceslink api.
    #When we are done with data, we run this and waiting for new training data coming from user.

    url = "https://www.polaraccesslink.com/v3/users/{your-user-id}/exercise-transactions/{transaction_id}".format(transaction_id=transactionid)

    headers = {'Authorization': 'Bearer [token from authorization.getToken()]'}
    response = requests.put(url, headers=headers)
    print(response)




def updateKilometers():
    TRANSACTION_ID = getTransactionId()
    if TRANSACTION_ID == 0:
        #dont add anything to kilometers and returns 0
        return 0
    else:
        kilometers = collectKilometers(TRANSACTION_ID)
        commitTransaction()             #Finally, stop transaction.
        print(kilometers)
        return kilometers




if __name__ == "__main__":
    updateKilometers()
    






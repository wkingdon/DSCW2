import requests

DATA_WRITE_URL = "https://distsysdatafunction.azurewebsites.net/api/writetodatabase"

def main():
    inputData = {
        "sID": 1,
        "temp": 12,
        "wind": 17,
        "humidity": 60,
        "co2": 700
    }
    response = requests.post(DATA_WRITE_URL, json = inputData)
    
    print(response)
    print(response.text)

if __name__ == "__main__":
    main()

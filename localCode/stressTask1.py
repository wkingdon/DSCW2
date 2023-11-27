import requests
import time
import matplotlib.pyplot as plt
import random

DATA_WRITE_URL = "https://distsysdatafunction.azurewebsites.net/api/writetodatabase"

def test(numberOfBatches):
    inputData = []
    for i in range(numberOfBatches):
        for i in range(1,21):
            inputData.append({
                "sID": i,
                "temp": random.uniform(8,15),
                "wind": random.uniform(15,25),
                "humidity": random.uniform(40,70),
                "co2": random.uniform(500,1500)
            })
            
    startTime = time.time()
    for data in inputData:
        requests.post(DATA_WRITE_URL, json = data)
    endTime = time.time()
    return endTime - startTime

def main():
    noOfValues = []
    time = []
    for i in range (1,10):
        noOfValues.append(i*20)
        time.append(test(i))
    
    plt.plot(noOfValues, time)
    plt.savefig('graph.png')


if __name__ == "__main__":
    main()
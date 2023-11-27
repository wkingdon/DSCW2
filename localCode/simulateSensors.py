import requests
import random
import time 
import aiohttp
import asyncio


DATA_WRITE_URL_DEPLOYED = "https://distsysdatafunction.azurewebsites.net/api/writetodatabase"

# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp
# asynchronous requests

async def main():
    async with aiohttp.ClientSession() as session:
    
        while True:
            for i in range(1,21):
                inputData = {
                    "sID": i,
                    "temp": random.uniform(8,15),
                    "wind": random.uniform(15,25),
                    "humidity": random.uniform(40,70),
                    "co2": random.uniform(500,1500)
                }
                async with session.post(DATA_WRITE_URL_DEPLOYED, json = inputData) as resp:
                    print(resp)
            print("waiting")
            time.sleep(5)

asyncio.run(main())
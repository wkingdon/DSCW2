import logging
import json
import azure.functions as func

# https://stackoverflow.com/questions/4391697/find-the-index-of-a-dict-within-a-list-by-matching-the-dicts-value
def findStatsIndex(rows, sensorId):
    for index, row in enumerate(rows):
        if row['sensorId'] == sensorId:
            return index
    return -1

def main(sensorDataChange, sensorStatsInput: func.SqlRowList, sensorStatsOutput: func.Out[func.SqlRow]):
    # dump database data into rows
    statsRows = list(map(lambda r: json.loads(r.to_json()), sensorStatsInput)) 
    
    rowsToUpdate  = []
    
    # logging.info(json.dumps(statsRows))
    for item in json.loads(sensorDataChange):
        sensor = item['Item']
        sensorId = sensor['sensorId']
        sensorIndex = findStatsIndex(statsRows, sensorId)
        
        
        logging.info(f"SQL Changes from sensor: {sensorId}: {sensorIndex}")
        # logging.info(json.dumps(statsRows))
        
        if( sensorIndex == -1):
            rowsToUpdate.append({
                "sensorId": sensorId, "count": 1,
                "temperatureMin": sensor['temperature'],
                "windMin": sensor['wind'],
                "humidityMin": sensor['humidity'], 
                "co2Min": sensor['co2'],
                "temperatureMax": sensor['temperature'], 
                "windMax": sensor['wind'], 
                "humidityMax": sensor['humidity'], 
                "co2Max": sensor['co2'], 
                "temperatureAvg": sensor['temperature'], 
                "windAvg": sensor['wind'], 
                "humidityAvg": sensor['humidity'], 
                "co2Avg": sensor['co2']
            })
            continue
        else:
            stat = statsRows[sensorIndex]
            rowsToUpdate.append({
                "sensorId": sensorId, "count": stat['count'] + 1,
                "temperatureMin": min(stat['temperatureMin'], sensor['temperature']),
                "windMin": min(stat['windMin'], sensor['wind']),
                "humidityMin": min(stat['humidityMin'], sensor['humidity']), 
                "co2Min": min(stat['co2Min'], sensor['co2']),
                "temperatureMax": max(stat['temperatureMax'], sensor['temperature']), 
                "windMax": max(stat['windMax'], sensor['wind']), 
                "humidityMax": max(stat['humidityMax'], sensor['humidity']), 
                "co2Max": max(stat['co2Max'], sensor['co2']), 
                "temperatureAvg": ((stat['temperatureAvg'] * stat['count']) + sensor['temperature']) / (stat['count'] + 1), 
                "windAvg": ((stat['windAvg'] * stat['count']) + sensor['wind']) / (stat['count'] + 1), 
                "humidityAvg": ((stat['humidityAvg'] * stat['count']) + sensor['humidity']) / (stat['count'] + 1), 
                "co2Avg": ((stat['co2Avg'] * stat['count']) + sensor['co2']) / (stat['count'] + 1)
            })
            continue
    
    sensorStatsOutput.set(func.SqlRowList(rowsToUpdate))
        
    

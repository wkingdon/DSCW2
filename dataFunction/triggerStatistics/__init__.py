import logging
import json
import azure.functions as func


def main(sensorDataChange, sensorDataItems: func.SqlRowList):
    # dump database data into rows
    rows = list(map(lambda r: json.loads(r.to_json()), sensorDataItems)) 
    
    logging.info(json.dumps(rows))
    for item in json.loads(sensorDataChange):
        sensorId = item['Item']['sensorId']
        logging.info("SQL Changes from sensor: %s", sensorId)
    

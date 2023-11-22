import logging
import uuid
import azure.functions as func


def main(req: func.HttpRequest, sensorDataItems: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info(f"POST:")
    inputData = {}
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse("Data not found in request body",  status_code = 400)
    else:
        inputData = {
            "sensorId": req_body.get('sID'),
            "temperature": req_body.get('temp'),
            "wind": req_body.get('wind'),
            "humidity": req_body.get('humidity'),
            "co2": req_body.get('co2')
        }
        
    if None in inputData.values():
        return func.HttpResponse("Incomplete data in request body", status_code = 400)

                
    sensorDataItems.set(func.SqlRow(inputData))
    
    return func.HttpResponse("Data Written successfully")
    # if name:
    # else:
    #     return func.HttpResponse(
    #         "Please pass a name on the query string or in the request body",
    #         status_code=400
    #     )

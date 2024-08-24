import azure.functions as func
import datetime
import json
import logging
import json

from models.medication import Medication
import services.data_access as data_access

app = func.FunctionApp()


@app.route(route="new_medication", auth_level=func.AuthLevel.ANONYMOUS)
def new_medication(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function (new_medication) processed a request.")

    drug_name = req.params.get("name")
    date_received = req.params.get("date_received")
    num_refills = req.params.get("num_refills")
    duration = req.params.get("duration")
    
    medication = Medication(
        name=drug_name,
        date_received=date_received,
        num_refills=int(num_refills),
        duration=int(duration)
    )
    
    data_access.add_item(medication)
    
    return func.HttpResponse(
        f"Medication {drug_name} added to the database.",
        status_code=200
    )

    # name = req.params.get("name")
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get("name")

    # if name:
    #     return func.HttpResponse(
    #         f"Hello, {name}. This HTTP triggered function executed successfully."
    #     )
    # else:
    #     return func.HttpResponse(
    #         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #         status_code=200,
    #     )

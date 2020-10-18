import logging
import json
import azure.functions as func
import requests
import datetime

from .data_processing import DataProcessing

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('"Data Sanitization" function processed a request')
    json_retorno: dict = { "status": None, "msg": None }
    json_post_prediction: dict = { "date": None, "temperature": None, "humidity": None, "wind_velocity": None, "pressure": None }
    headers: dict = { 'content-type': "application/json", 'cache-control': "no-cache", 'postman-token': "953560e7-36c4-8375-8721-af301923fbeb" }
    url: str = "URL_SERVIÇO"

    try:
        # Lê os dados obtidos no Thing Speak
        req_body = req.get_json()

        # Processa o saneamento das informações
        processed_data: dict = DataProcessing().Run(req_body)

        # Envia os dados para o modelo preditivo
        json_post_prediction["date"] = datetime.datetime.now().strftime("%Y-%m-%d")
        json_post_prediction["temperature"] = processed_data["Temp"].values[0]
        json_post_prediction["humidity"] = processed_data["Hum"].values[0]
        json_post_prediction["pressure"] = processed_data["Press"].values[0]
        json_post_prediction["wind_velocity"] = processed_data["Wind"].values[0]

        # TODO: Post
        # requests.request("POST", url, data=json.dumps(json_post_prediction), headers=headers)

        json_retorno["status"] = "OK"
        json_retorno["msg"] = "Os dados do Thing Speak foram tratados com sucesso"

        return func.HttpResponse(json.dumps(json_retorno, indent=4), status_code=200)
    except ValueError as e:
        json_retorno["status"] = "Erro"
        json_retorno["msg"] = str(e)
        
        return func.HttpResponse(json.dumps(json_retorno, indent=4), status_code=500)

import logging
import json
import azure.functions as func

from .data_base import Database
from .prediction import Predict

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('"Prediction" function processed a request')
    json_retorno: dict = { "status": None, "msg": None }
    json_resultado_modelo: dict = { "prediction": None, "model": None }

    try:
        # Lê os dados tratados para o modelo preditivo
        req_body = req.get_json()

        temperature: float = float(str(req_body.get('temperature')))
        humidity: float = float(str(req_body.get('humidity')))
        wind_velocity: float = float(str(req_body.get('wind_velocity')))
        pressure: float = float(str(req_body.get('pressure')))

        # Executa o modelo preditivo
        prediction_result: int = Predict().run(temperature, humidity, wind_velocity, pressure)

        json_resultado_modelo["prediction"] = prediction_result
        json_resultado_modelo["model"] = req_body

        # Envia os dados para o repositório de dados
        db: Database = Database()
        db.insert_data(json_resultado_modelo)

        json_retorno["status"] = "OK"
        json_retorno["msg"] = "Modelo preditivo executado com sucesso. Os dados já estão no repositório."

        return func.HttpResponse(json.dumps(json_retorno, indent=4), status_code=200)
    except Exception as e:
        json_retorno["status"] = "Erro"
        json_retorno["msg"] = str(e)
        
        return func.HttpResponse(json.dumps(json_retorno, indent=4), status_code=500)

import logging
import json

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('"Data Sanitization" function processed a request')
    json_retorno = { "status": None, "msg": None }

    try:
        # Lê os dados obtidos no Thing Speak
        req_body = req.get_json()

        # Processa o saneamento das informações
        ## TODO: Dé, incluir as chamadas das funções de tratamento de dados aqui

        # Envia os dados para o modelo preditivo
        ## TODO: Léo, incluir a integração de dados para a próxima função

        json_retorno["status"] = "OK"
        json_retorno["msg"] = "Os dados do Thing Speak foram tratados com sucesso"

        return func.HttpResponse(json.dumps(json_retorno, indent=4), status_code=200)
    except ValueError as e:
        json_retorno["status"] = "Erro"
        json_retorno["msg"] = str(e)
        
        return func.HttpResponse(json.dumps(json_retorno, indent=4), status_code=500)

import datetime
import logging
import json

import azure.functions as func

from .crawler import Crawler
from .model.weather import Weather

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Started at %s', utc_timestamp)

    url_ts: str = "https://api.thingspeak.com/channels/1074545/feeds.json?start={0}%2000:00:01&end={0}%2023:59:59"
    ts_filter_date = datetime.datetime.utcnow().date() - datetime.timedelta(days=1)

    c: Crawler = Crawler(url_ts.format(ts_filter_date.strftime("%Y-%m-%d")))    
    w: Weather = c.GetWeatherFromService()

    ################################################################
    ## TODO: Enviar o JSON para a função de tratamento de dados ##
    ################################################################

    logging.info('Finished at %s', utc_timestamp)
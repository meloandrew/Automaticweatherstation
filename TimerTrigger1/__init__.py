import datetime
import logging
import json

import azure.functions as func

from crawler import Crawler
from model.weather import Weather

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Started at %s', utc_timestamp)

    c: Crawler = Crawler("https://api.thingspeak.com/channels/1074545/feeds.json?start=2020-06-11%2000:00:00&end=2020-06-11%2001:00:00")    
    w: Weather = c.GetWeatherFromService()
    
    logging.info(json.dumps(w.to_dict()))

    logging.info('Finished at %s', utc_timestamp)

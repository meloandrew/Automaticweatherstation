import datetime
import logging
import json
import requests
import azure.functions as func

from .crawler import Crawler
from .model.weather import Weather

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Started at %s', utc_timestamp)

    url_ts: str = "https://api.thingspeak.com/channels/1074545/feeds.json?start={0}%2000:00:01&end={0}%2023:59:59"
    ts_filter_date = datetime.datetime.utcnow().date() - datetime.timedelta(days=1)
    headers: dict = { 'content-type': "application/json", 'cache-control': "no-cache", 'postman-token': "953560e7-36c4-8375-8721-af301923fbeb" }
    url: str = "URL_SERVIÇO"

    c: Crawler = Crawler(url_ts.format(ts_filter_date.strftime("%Y-%m-%d")))    
    w: Weather = c.GetWeatherFromService()

    requests.request("POST", url, data=json.dumps(w.feeds), headers=headers)

    logging.info('Finished at %s', utc_timestamp)
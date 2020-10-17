import json
import time

from model.weather import Weather
from urllib import request

class Crawler():
  URL: str

  def __init__(self, url: str):
    self.URL = url
    pass

  def GetWeatherFromService(self) -> Weather:
    service_data = request.urlopen(self.URL)
    weather_data: Weather

    if service_data is not None:
      weather_data = Weather.from_dict(json.loads(service_data.read()))
      return weather_data
    else:
      return None

# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = weather_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return datetime.strptime(x, '%Y-%m-%dT%H:%M:%S%z')


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Channel:
    id: int
    name: str
    description: str
    latitude: str
    longitude: str
    field1: str
    field2: str
    field3: str
    created_at: datetime
    updated_at: datetime
    last_entry_id: int

    def __init__(self, id: int, name: str, description: str, latitude: str, longitude: str, field1: str, field2: str, field3: str, created_at: datetime, updated_at: datetime, last_entry_id: int) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.created_at = created_at
        self.updated_at = updated_at
        self.last_entry_id = last_entry_id

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        latitude = from_str(obj.get("latitude"))
        longitude = from_str(obj.get("longitude"))
        field1 = from_str(obj.get("field1"))
        field2 = from_str(obj.get("field2"))
        field3 = from_str(obj.get("field3"))
        created_at = from_datetime(obj.get("created_at"))
        updated_at = from_datetime(obj.get("updated_at"))
        last_entry_id = from_int(obj.get("last_entry_id"))
        return Channel(id, name, description, latitude, longitude, field1, field2, field3, created_at, updated_at, last_entry_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["latitude"] = from_str(self.latitude)
        result["longitude"] = from_str(self.longitude)
        result["field1"] = from_str(self.field1)
        result["field2"] = from_str(self.field2)
        result["field3"] = from_str(self.field3)
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        result["last_entry_id"] = from_int(self.last_entry_id)
        return result


class Feed:
    created_at: datetime
    entry_id: int
    field1: str
    field2: str
    field3: str

    def __init__(self, created_at: datetime, entry_id: int, field1: str, field2: str, field3: str) -> None:
        self.created_at = created_at
        self.entry_id = entry_id
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    @staticmethod
    def from_dict(obj: Any) -> 'Feed':
        assert isinstance(obj, dict)
        created_at = from_datetime(obj.get("created_at"))
        entry_id = from_int(obj.get("entry_id"))
        field1 = from_str(obj.get("field1"))
        field2 = from_str(obj.get("field2"))
        field3 = from_str(obj.get("field3"))
        return Feed(created_at, entry_id, field1, field2, field3)

    def to_dict(self) -> dict:
        result: dict = {}
        result["created_at"] = self.created_at.isoformat()
        result["entry_id"] = from_int(self.entry_id)
        result["field1"] = from_str(self.field1)
        result["field2"] = from_str(self.field2)
        result["field3"] = from_str(self.field3)
        return result


class Weather:
    channel: Channel
    feeds: List[Feed]

    def __init__(self, channel: Channel, feeds: List[Feed]) -> None:
        self.channel = channel
        self.feeds = feeds

    @staticmethod
    def from_dict(obj: Any) -> 'Weather':
        assert isinstance(obj, dict)
        channel = Channel.from_dict(obj.get("channel"))
        feeds = from_list(Feed.from_dict, obj.get("feeds"))
        return Weather(channel, feeds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel"] = to_class(Channel, self.channel)
        result["feeds"] = from_list(lambda x: to_class(Feed, x), self.feeds)
        return result


def weather_from_dict(s: Any) -> Weather:
    return Weather.from_dict(s)


def weather_to_dict(x: Weather) -> Any:
    return to_class(Weather, x)

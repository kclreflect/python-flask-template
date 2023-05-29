from dataclasses import dataclass
from typing import Any


@dataclass
class Event:
    body: bytes
    headers: Any
    method: str
    query: Any
    path: str


@dataclass
class Context:
    hostname: str
    statusCode: int
    body: dict[Any, Any] | str
    headers: Any

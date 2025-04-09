import json
from datetime import datetime
from enum import Enum

from bson import ObjectId
from fastapi import Response
from mongoengine import Document


def json_handler(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, list):
        return [json_handler(val) for val in obj]
    if isinstance(obj, dict):
        return {key: json_handler(val) for key, val in obj.items()}
    if isinstance(obj, Document):
        return json_handler(obj._data)
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, Enum):
        return obj.value
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    return obj


def jsonify_response(data):
    return Response(
        json.dumps(data, default=json_handler), media_type="application/json"
    )

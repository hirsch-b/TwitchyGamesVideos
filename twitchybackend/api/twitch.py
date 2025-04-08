from fastapi import APIRouter, Response

from twitchybackend.clients.twitch import get_client
from twitchybackend.models.game import Game
from twitchAPI.helper import limit, first
from fastapi.responses import JSONResponse

import json
from mongoengine import Document

router = APIRouter(prefix="/twitch")

from bson import ObjectId
from datetime import datetime
from enum import Enum

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
    return Response(json.dumps(data, default=json_handler), media_type="application/json")


def upsert_game(game):
    return Game.objects(twitch_id=game.id).modify(
        set__name=game.name,
        set__box_art_url=game.box_art_url,
        upsert=True,
        new=True,
    )


@router.get("/game/{game_id}")
async def get_game_by_id(game_id: str):
    game = Game.objects(twitch_id=game_id).first()
    if not game:
        client = await get_client()
        game = upsert_game(await first(client.get_games(game_ids=[game_id])))
    return game


@router.get("/games/{term}")
async def get_games(term: str):
    client = await get_client()
    games = []
    if term:
        async for game in limit(client.search_categories(term, first=100), 200):
            games.append(upsert_game(game))
    return jsonify_response(games)


@router.get("/videos-by-game/{game_id}")
async def get_videos_by_game(game_id: int):
    client = await get_client()
    game = await get_game_by_id(game_id)
    videos = []

    async for vid in limit(client.get_videos(game_id=game_id, first=100), 100):
        videos.append(vid)
    return jsonify_response({"game": game, "videos": videos})

from fastapi import APIRouter
from twitchAPI.helper import limit

from twitchybackend.clients.twitch import get_client
from twitchybackend.models.game import Game
from twitchybackend.utils import jsonify_response

router = APIRouter(prefix="/twitch")


@router.get("/game/{game_id}")
async def get_game_by_id(game_id: str):
    game = Game.objects(twitch_id=game_id).first()
    return game


@router.get("/games/{term}")
async def get_games(term: str):
    games = []
    if term:
        games = list(Game.objects(name__icontains=term.strip()))
    return jsonify_response(games)


@router.get("/videos-by-game/{game_id}")
async def get_videos_by_game(game_id: int):
    client = await get_client()
    game = await get_game_by_id(game_id)
    videos = []

    async for vid in limit(client.get_videos(game_id=game_id, first=100), 100):
        videos.append(vid)
    return jsonify_response({"game": game, "videos": videos})

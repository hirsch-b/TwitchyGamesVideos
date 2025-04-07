from fastapi import APIRouter

from twitchybackend.clients.twitch import get_client
from twitchybackend.models.game import Game

router = APIRouter(prefix="/twitch")


@router.get("/games/{term}")
async def get_games(term: str):
    client = await get_client()
    games = []
    if term:
        async for game in client.search_categories(term, first=100):
            games.append(game)
            Game.objects(twitch_id=game.id).update_one(
                set__name=game.name,
                set__box_art_url=game.box_art_url,
                upsert=True,
            )
    return games


@router.get("/videos-by-game/{game_id}")
async def get_videos_by_game(game_id: int):
    client = await get_client()
    videos = []

    async for vid in client.get_videos(game_id=game_id, first=10):
        videos.append(vid)
    return videos

from fastapi import APIRouter

from twitchybackend.clients.twitch import get_client

router = APIRouter(prefix="/twitch")


@router.get("/games/{term}")
async def get_games(term: str):
    client = await get_client()
    games = []
    if term:
        async for game in client.search_categories(term, first=100):
            games.append(game)
    return games


@router.get("/videos-by-game/{game_id}")
async def get_videos_by_game(game_id: int):
    client = await get_client()
    videos = []

    async for vid in client.get_videos(game_id=game_id, first=10):
        videos.append(vid)
    return videos

# TwitchyGamesVideos

## Installing the dependencies

```bash
pip install -r requirements.txt
fastapi dev twitchybackend/app.py
```

## Installing dev dependencies

```bash
pip install -r requirements.txt -r requirements.dev.txt
pytest tests/
black
isort
```

## Testing endpoints

```bash
curl http://127.0.0.1:8000/twitch/games/counter-strike+2
curl http://127.0.0.1:8000/twitch/videos-by-game/32399
```

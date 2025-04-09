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
```

## Running the project

You'll need a client ID and a secret from the Twitch console: https://dev.twitch.tv/console

Those tokens must be set in a `local.env` file at the root of the project:

```
TWITCH_CLIENT_ID=Application ID
TWITCH_SECRET=Application Secret
```

```bash
docker compose up -d --build
cd twitchyfrontend
npm run dev
```

## Testing endpoints

```bash
curl http://127.0.0.1:8000/twitch/games/counter-strike+2
curl http://127.0.0.1:8000/twitch/videos-by-game/32399
```

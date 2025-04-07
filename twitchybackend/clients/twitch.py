from os import environ

from twitchAPI.twitch import AuthScope, Twitch

SCOPES = [AuthScope.USER_READ_EMAIL]


async def get_client():
    client_id = environ.get("TWITCH_CLIENT_ID")
    secret = environ.get("TWITCH_SECRET")
    if client_id is None or secret is None:
        raise RuntimeError("TWITCH_CLIENT_ID and TWITCH_SECRET must be set")

    client = Twitch(client_id, secret)
    await client.authenticate_app([])
    return client

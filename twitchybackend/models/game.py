from mongoengine import Document, fields


class Game(Document):
    name = fields.StringField(required=True)
    twitch_id = fields.StringField(required=True)
    box_art_url = fields.StringField()

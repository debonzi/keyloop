from datetime import date
from marshmallow import Schema, fields
from json_marshmallow import gen_schema, schema_registry


def test_simple():
    class ArtistSchema(Schema):
        name = fields.Str()

    class AlbumSchema(Schema):
        title = fields.Str()
        release_date = fields.Date()
        artist = fields.Nested(ArtistSchema())

    bowie = dict(name="David Bowie")
    album = dict(artist=bowie, title="Hunky Dory", release_date=date(1971, 12, 17))

    schema = AlbumSchema()
    result = schema.dump(album)
    expected_result = {
        "artist": {"name": "David Bowie"},
        "title": "Hunky Dory",
        "release_date": "1971-12-17",
    }
    assert result == expected_result

    json_artist_schema = {
        "class_name": "ArtistSchema",
        "definition": {"name": {"type": "Str"},},
    }

    json_album_schema = {
        "class_name": "AlbumSchema",
        "definition": {
            "title": {"type": "Str"},
            "release_date": {"type": "Date"},
            "artist": {"type": "Nested", "schema": "ArtistSchema"},
        },
    }

    schema_registry.register(json_artist_schema)
    schema_registry.register(json_album_schema)

    DinAlbumSchema = gen_schema(json_album_schema)

    schema = DinAlbumSchema()
    din_result = schema.dump(album)
    assert din_result == expected_result

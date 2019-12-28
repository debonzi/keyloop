from pymodm import MongoModel, fields
from pymongo import WriteConcern, ReadPreference, ASCENDING, IndexModel


class Realms(MongoModel):
    slug = fields.CharField(primary_key=True, validators=[lambda x: x.lower()])
    name = fields.CharField(required=True)
    description = fields.CharField(default="")

    def create(self):
        self.save(force_insert=True)

    def update(self):
        self.save()

    class Meta:
        # indexes = [IndexModel([("slug", ASCENDING)], unique=True)]
        read_preference = ReadPreference.SECONDARY
        write_concern = WriteConcern(j=True)
        connection_alias = "keyloop"
        collection_name = "Realms"

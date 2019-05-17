from peewee import *
from datetime import datetime


db = SqliteDatabase('inventory.db')


class Inventory(Model):
    product_id = AutoField(unique=True)
    product_name = CharField(max_length=255)
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.now)

    class Meta:
        database = db


if __name__ == "__main__":
    db.connect()
    db.create_tables([Inventory], safe=True)
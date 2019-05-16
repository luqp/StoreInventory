from peewee import *
from datetime import datetime

import csv


db = SqliteDatabase('inventory.db')


class Inventory(Model):
    product_id = AutoField(unique=True)
    product_name = CharField(max_length=255)
    product_quantity = IntegerField()
    product_price = IntegerField()
    date_updated = DateTimeField(default=datetime.now)

    class Meta:
        database = db


def update_item(inventory, item, date=None):
    if not date:
        date = item['date_updated']
    for row in inventory:
        if  date > row.date_updated:
            row.product_quantity = item['product_quantity']
            row.product_price = item['product_price']
            row.date_updated = date
            row.save()
    return True


def optain_csv_data(file='databases/inventory.csv'):
    inventory = []
    with open(file, newline='') as csvfile:
        invreader = csv.DictReader(csvfile)
        for row in list(invreader)[:]:
            quantity = int(row['product_quantity'])
            value = round(float(row['product_price'].split("$")[-1]) * 100.00)
            date = datetime.strptime(row['date_updated'], "%m/%d/%Y")
            item = {}
            item['product_name'] = row['product_name']
            item['product_price'] = value
            item['product_quantity'] = quantity
            item['date_updated'] = date
            inventory.append(item)
    return inventory


def convert_to_csv_file():
    inventory = Inventory.select()
    products = []
    for row in inventory:
        value = "$" + str(row.product_price / 100)
        date = row.date_updated.strftime("%m/%d/%Y")
        item = {}
        item['product_name'] = row.product_name
        item['product_price'] = value
        item['product_quantity'] = row.product_quantity
        item['date_updated'] = date
        products.append(item)
    return products


if __name__ == "__main__":
    db.connect()
    db.create_tables([Inventory], safe=True)
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
            inventory = Inventory.select().where(Inventory.product_name.contains(item['product_name']))
            if len(inventory):
                update_item(inventory, item)
            else:
                Inventory.create(**item)


def write_new_csv_file(file="backup/backup.csv"):
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

    with open(file, "w", newline='') as backup_file:
        fieldnames = ['product_name', 'product_price', 'product_quantity', 'date_updated']
        inventory_file = csv.DictWriter(backup_file, fieldnames=fieldnames)
        inventory_file.writeheader()
        for product in products:
            inventory_file.writerow(product)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Inventory], safe=True)
    optain_csv_data()
    #write_new_csv_file()
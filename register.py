import re
import csv

from databases.data_handler import update_item, optain_csv_data, convert_to_csv_file


class Register():

    def __init__(self, database, fields):
        self.data = database
        self.fileds = fields

    def create_database(self):
        self.data.create_table()
        self.fill_records(optain_csv_data())
    
    def fill_records(self, data):
        for item in data:
            equals_items = self.data.select().where(
                self.data.product_name == item[self.fileds[0]]
            )
            if len(equals_items):
                update_item(equals_items, item)
            else:
                self.data.create(**item)

    def make_a_backup(self, file="backup/backup.csv"):
        converted_products = convert_to_csv_file(self.data)
        with open(file, "w", newline='') as backup_file:
            inventory_file = csv.DictWriter(backup_file, fieldnames=self.fileds)
            inventory_file.writeheader()
            for product in converted_products:
                inventory_file.writerow(product)
        return True

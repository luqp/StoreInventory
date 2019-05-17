# Store Inventory
This project converts csv data and adds it to a database for use in an inventory console app
in which you can show items, add new items, and create a backup.

<p align="center">
    <img src="https://github.com/windyludev/StoreInventory/blob/master/imgs/store_inventory.jpg"/>
</p>

## It's easy
_(If you want to create your own database)_
* First, you have to run the `inventory.py` file
```
python inventory.py
```
* You have to run the `app.py` file
```
python app.py
```

## Features:
* Converts CSV data into a handler List 
* Converts data of database in CSV file
* Add new items
* Update a items to the last version 
* Shows a single item
* Shows whole table items
* Handles pagination

## Use your own CSV data
Here a ![example](https://github.com/windyludev/StoreInventory/blob/master/backup/backup.csv) of format CSV data that handles this app

To insert your data you can:

### Change the default file:
In the `StoreInventory/databases/data_handler.py ` file, in the `optain_csv_data` method change the parameter path:
```python
20      def optain_csv_data(file='~/here_your_csv_data.csv'):
```

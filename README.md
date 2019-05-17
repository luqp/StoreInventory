# Store Inventory
This project converts csv data and adds it to a database for use in an inventory console app
in which you can show items, add new items, and create a backup.

<p align="center">
    <img src="https://github.com/windyludev/StoreInventory/blob/master/imgs/store_inventory.jpg"/>
</p>

## It's easy
**0. Create the database:** _(If you want to create your own database, don't download the `inventory.db` file)_
* First, you have to run the `inventory.py` file
```
python .\databases\inventory.py
```
**1. Run the program**
* After you have the database, you have to run the `app.py` file
```
python app.py
```

## Features:
* Converts CSV data into a handler List 
* Converts data of database in CSV file
* Add new items
* Update a item to the last version 
* Shows a single item
* Shows whole table items
* Handles pagination

## Use your own CSV data
1. Add your data file to the folder, here a [example](https://github.com/windyludev/StoreInventory/blob/master/backup/backup.csv) of format CSV data that handles this app.

2. Delete the data base and create another new.

#### Insert the path of your CSV file:

3. Add your path parameter in the `StoreInventory/app.py` file, like this:
```python
159     register.create_database('./here_your_csv_data.csv')
```

4. After that run the `app.py` file.

Now you can use the app with your data.

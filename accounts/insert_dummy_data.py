import datetime
from mongoengine import connect
from models import StockItem

# Connect to the MongoDB database (adjust parameters as needed)
connect('mydb', host='localhost', port=27017)

dummy_data = [
    {
        "item_name": "Broom",
        "time": "08:30",
        "date": "01/06/2024",
        "where_bought_from": "General Store",
        "quantity": 10
    },
    {
        "item_name": "Mop",
        "time": "09:15",
        "date": "02/06/2024",
        "where_bought_from": "Home Essentials",
        "quantity": 8
    },
    {
        "item_name": "Dish Soap",
        "time": "10:00",
        "date": "03/06/2024",
        "where_bought_from": "Supermarket",
        "quantity": 20
    },
    {
        "item_name": "Trash Bags",
        "time": "11:30",
        "date": "04/06/2024",
        "where_bought_from": "General Store",
        "quantity": 50
    },
    {
        "item_name": "Toilet Paper",
        "time": "12:00",
        "date": "05/06/2024",
        "where_bought_from": "Supermarket",
        "quantity": 30
    },
    {
        "item_name": "Laundry Detergent",
        "time": "13:45",
        "date": "06/06/2024",
        "where_bought_from": "Home Essentials",
        "quantity": 12
    },
    {
        "item_name": "Bucket",
        "time": "14:30",
        "date": "07/06/2024",
        "where_bought_from": "General Store",
        "quantity": 6
    },
    {
        "item_name": "Sponge",
        "time": "15:10",
        "date": "08/06/2024",
        "where_bought_from": "Supermarket",
        "quantity": 25
    },
    {
        "item_name": "Air Freshener",
        "time": "16:00",
        "date": "09/06/2024",
        "where_bought_from": "Home Essentials",
        "quantity": 18
    },
    {
        "item_name": "Hand Wash",
        "time": "17:20",
        "date": "10/06/2024",
        "where_bought_from": "Supermarket",
        "quantity": 15
    }
]



for item in dummy_data:
    stock_item = StockItem(
        item_name=item["item_name"],
        time=item["time"],
        date=item["date"],
        where_bought_from=item["where_bought_from"],
        quantity=item["quantity"]
    )
    stock_item.save()

print("Dummy data inserted successfully.")

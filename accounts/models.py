from mongoengine import Document, StringField, DateTimeField, IntField
from datetime import datetime

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

class StockItem(Document):
    item_name = StringField(required=True)
    time = StringField()  # storing time as string for simplicity
    date = StringField()  # storing date as string for simplicity
    where_bought_from = StringField()
    quantity = IntField()

class StockUpdateLog(Document):
    action = StringField(required=True, choices=['insert', 'delete', 'update'])
    item_name = StringField(required=True)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField()  # optional field to store update details

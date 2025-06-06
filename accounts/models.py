from mongoengine import Document, StringField, DateTimeField, IntField

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)

class StockItem(Document):
    item_name = StringField(required=True)
    time = StringField()  # storing time as string for simplicity
    date = StringField()  # storing date as string for simplicity
    where_bought_from = StringField()
    quantity = IntField()

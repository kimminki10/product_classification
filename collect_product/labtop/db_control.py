from pymongo import MongoClient


class DBControl:
    def __init__(self) -> None:
        client = MongoClient(host='localhost', port=27017)
        db = client['product_classification']

        self.labtops = db['labtops']

    
    def put_danawa_labtop(self, datas):
        for data in datas:
            self.labtops.update_one({'name': data['name']}, update={"$set": data}, upsert=True)


from danawa_labtop import get_danawa_laptop_info

dbc = DBControl()
li = get_danawa_laptop_info(page=2)
dbc.put_danawa_labtop(li)
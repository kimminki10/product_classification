from pymongo import MongoClient


class DBControl:
    def __init__(self) -> None:
        client = MongoClient(host='localhost', port=27017)
        db = client['product_classification']

        self.labtops = db['laptops']

    
    def put_danawa_labtop(self, datas):
        for data in datas:
            self.labtops.update_one({'name': data['name']}, update={"$set": data}, upsert=True)

    
    def drop_labtops(self):
        self.labtops.drop()

def initialize_db():
    from danawa_labtop import get_danawa_laptop_info_selenium
    from search_engine import laptop_search

    dbc = DBControl()
    dbc.drop_labtops()
    for i in range(1, 20):
        li = get_danawa_laptop_info_selenium(page=i)
        dbc.put_danawa_labtop(li)

    laptop_search.quit_driver()


if __name__=="__main__":
    initialize_db()

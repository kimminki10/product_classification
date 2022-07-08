# product_classification

상품 분류 사이트를 만들 것이다.

노트북을 먼저 해보려 한다.

# 크롤링 환경 구축
```
# venv setting
python3 -m venv venv
source venv/bin/activate

# pip upgrade
python3 -m pip install --upgrade pip

# install requests
python3 -m pip install --upgrade requests

# install selenium
python3 -m pip install --upgrade selenium

# install pymongo
python3 -m pip install --upgrade pymongo
```
# mongoDB install
```
# mongodb docker image download
docker pull mongo

docker run --name mongodb -d -p 27017:27017 mongo
```
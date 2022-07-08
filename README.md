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

# 왜 이 프로젝트를 하게 되었는가?

노트북에 대해 비교적 많이 아는데 노트북 추천을 해달라는 사람들이 많았다. 추천해주는 일은 즐거웠지만 너무 자주 추천 해달라고 요청 받으니 그것도 참 귀찮아졌다. 벤치마크 사이트는 많지만 용도별로 추천해주는 사이트가 없는 것 같아서 내가 만들기로 했다.

노트북을 사기 위해서는 여러가지 전문 정보를 알아야 한다. CPU, GPU 성능, 자신이 노트북으로 하려는 일에 따라서
디스플레이 정보, 휴대성도 중요하다. 일반 소비자들은 이 정보를 아는 경우가 별로 없고 알고 싶어하지도 않는다.
이 노트북을 사면 이 게임을 원활하게 돌릴 수 있는가? 영상 편집을 할 때 이 노트북으로 충분히 할 수 있는가?
소비자가 원하는 정보는 자신이 하려는 용도에 맞는 가장 가성비 좋은 노트북이 무엇인지라 생각하게되어 이 프로젝트를 시작한다.

노트북을 사용할 수 있는 용도에 맞게 분류한다음 그 용도에 현재 가장 잘 맞는 가성비 좋은 노트북을 추천한다.
성능과 가격으로 분류하고 디자인과 회사 브랜드는 소비자가 정할 수 있게 할 것이다.

예를 들어 "League of Legend 정도 중간 옵션으로 원활하게 돌아가는 가벼운 노트북이 필요해" -> 베스트 한개, 브랜드별 노트북 추천
from bs4 import BeautifulSoup as bs
import requests

def get_danawa_laptop_info(page=1, sort_order="NEW"):
    product_list = "http://prod.danawa.com/list/ajax/getProductList.ajax.php"

    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
        "Referer": "http://prod.danawa.com/list/?cate=112758&15main_11_02"
    }

    payload = {
        "priceRangeMinPrice": "",
        "priceRangeMaxPrice": "",
        "btnAllOptUse": "true",
        "page": page,
        "listCategoryCode": "758",
        "categoryCode": "758",
        "physicsCate1": "860",
        "physicsCate2": "869",
        "physicsCate3": "0",
        "physicsCate4": "0",
        "viewMethod": "LIST",
        "sortMethod": sort_order,
        "listCount": "30",
        "group": "11",
        "depth": "2",
        "brandName": "",
        "makerName": "",
        "searchOptionName": "",
        "sDiscountProductRate": "0",
        "sInitialPriceDisplay": "N",
        "sPowerLinkKeyword": "노트북",
        "oCurrentCategoryCode": "a:2:{i:1;i:96;i:2;i:758;}",
        "adSmartDataSet": "",
        "sMallMinPriceDisplayYN": "N",
        "innerSearchKeyword": "",
        "listPackageType": "1",
        "categoryMappingCode": "710",
        "priceUnit": "0",
        "priceUnitValue": "0",
        "priceUnitClass": "",
        "cmRecommendSort": "N",
        "cmRecommendSortDefault": "N",
        "bundleImagePreview": "N",
        "nPackageLimit": "5",
        "bMakerDisplayYN": "Y",
        "dnwSwitchOn": "",
        "isDpgZoneUICategory": "N",
        "isAssemblyGalleryCategory": "N",
        "sProductListApi": "search",
    }

    sess = requests.Session()
    res = sess.post(product_list, headers=header, data=payload)
    
    soup = bs(res.text, 'html.parser')
    elements = soup.select("div.prod_main_info")

    for e in elements:
        prod_name = e.select_one("p.prod_name > a[name=productName]").text.strip()
        print(prod_name)
        for spec in e.select_one("dl > dd > div.spec_list").children:
            if spec.name == "b":
                print()
                print(spec.text.strip())
            else: 
                print(spec.text.strip(), end="")
        break


get_danawa_laptop_info()

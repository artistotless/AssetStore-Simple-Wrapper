import requests
import json

s = requests.Session()
HOST = 'https://assetstore.unity.com'
EVENT = 'https://prd-lender.cdp.internal.unity3d.com/v1/events'
BATCH = 'https://assetstore.unity.com/api/graphql/batch'
JSON_FILE = 'asset.json'
JSON_PATH = '/home/admin/web/unity3ddd.ru/public_html/files/'+JSON_FILE
MAX_ITEMS = 1
HEADERS = None

def Init(host):
    token = s.get(host).cookies['_csrf']
    global HEADERS
    HEADERS = {
"x-csrf-token": token,
"referer":"https://assetstore.unity.com/",
"operations": "PlainTextSuggest,SearchResults",
"accept":"application/json, text/plain, */*",
"x-requested-with": "XMLHttpRequest"
}
    s.options(EVENT)

def JsonToDict(data,offset=0):
    return data[0]['data']['searchPackageFromSolr']['results'][offset]

def GetLength(data):
    return len(data[0]['data']['searchPackageFromSolr']['results'])

def PrintJson(data):
    results = data[0]['data']['searchPackageFromSolr']['results']
    print('\n-----Search Results-----\n')
    for counter in range(1,len(results)):
        if counter > MAX_ITEMS and MAX_ITEMS != 0:
            break
        for key, value in results[counter-1].items():
            print(f'{key} : {value}')
        print('\n----------------\n')

def GetAssetInfo(idAsset):
    payloadInfo=[
        {
            "query":"query Product { product(id: $id) { ...product __typename } } fragment product on Product { id productId itemId slug name description rating { average count __typename } currentVersion { id name publishedDate __typename } reviewCount downloadSize assetCount publisher { id name url supportUrl supportEmail gaAccount gaPrefix __typename } mainImage { big facebook small icon icon75 __typename } originalPrice { itemId originalPrice finalPrice isFree discount { save percentage type saleType __typename } currency entitlementType __typename } images { type imageUrl thumbnailUrl __typename } category { id name slug longName __typename } firstPublishedDate publishNotes supportedUnityVersions state overlay overlayText popularTags { id pTagId name __typename } plusProSale licenseText __typename } ",
            "variables":{
                "id":idAsset
            },
            "operationName":"Product"
        }
    ] 
    return s.post(BATCH,headers=HEADERS,json=payloadInfo).json()
    

def Search(phrase):
    payloadSearch=[
    {
    "query":"query SearchResults($q: [String], $page: Int, $rows: Int, $orderBy: Int, $reverse: Boolean) { searchPackageFromSolr(q: $q, page: $page, pageSize: $rows, sort_by: $orderBy, reverse: $reverse) { results { ... on ProductQ { ...productQ __typename } __typename } category { name count __typename } onSale { name count __typename } exclude { name count __typename } plusPro { name count __typename } free { name count __typename } publisherSuggest { name count __typename } platform { name count __typename } srp { name count __typename } automotive { name count __typename } aec { name count __typename } snaps { name count __typename } discount50 { name count __typename } discount70 { name count __typename } stats { min max __typename } total __typename } } fragment productQ on ProductQ { id name rating { average count __typename } publisherName publisherId category mainImage iconImage price { price originPrice __typename } plusProSale onSale elevated url isNew partner labels __typename } ",
    "variables":{
        "q":[
            "q:"+phrase
                ],
                "page":0,
                "rows":24,
                "orderBy":1,
                "reverse":False
    },
    "operationName":"SearchResults"
}
      ]
    
    return s.post(BATCH,headers=HEADERS,json=payloadSearch).json()
    
def SaveJson(data,path):
    with open(path, 'w') as f:
        json.dump(data, f)


#************MAIN*************
search_phrase = str(input('Введите поисковый запрос: '))

MAX_ITEMS = int(input('Введите максимальное кол-во материалов (0 - без ограничений): '))
Init(HOST)
data = Search(search_phrase)
#PrintJson(data)
#for i in range(0,GetLength(data)):
#    item = JsonToDict(data,i)
#    print(f'\nID: {item["id"]}')
#    print(f'Title: {item["name"]}')
#    print(f'Publisher: {item["publisherName"]}')
#    print(f'PublisherId: {item["publisherId"]}')
#    print(f'Category: {item["category"]}')
#    print(f'Price: {item["price"]["price"]}')
#    print(f'iconImage: {item["iconImage"]}')
#    print(f'MainImage: {item["mainImage"]}')
#    print('\n---------------\n')
#
data = GetAssetInfo(JsonToDict(data,0)["id"])
print(data)
#info = GetAssetInfo(JsonToDict(data)['id')
#PrintJson(info)
SaveJson(data,JSON_PATH)


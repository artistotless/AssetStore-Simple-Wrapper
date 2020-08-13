import requests
import json

s = requests.Session()
HOST = 'https://assetstore.unity.com'
EVENT = 'https://prd-lender.cdp.internal.unity3d.com/v1/events'
BATCH = 'https://assetstore.unity.com/api/graphql/batch'
JSON_FILE = 'asset.json'
HTML_FILE = 'res.html'
FILES_PATH = '/home/admin/web/unity3ddd.ru/public_html/files/'
MAX_ITEMS = -1
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
   
def PrintData(data):
    print('\n-----Search Results-----\n')
    for key, value in data.items():
        print(f'{key} : {value}')
    print('\n----------------\n')

def Html(data):
    html = '<body><table cellspacing="0"><tr><th>&nbsp;</th><th>id</th><th>category</th><th>Price</th><th>Rating</th><th>Image</th</tr>'
    for i in range(0,len(data)):
        html = html + '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(data[i]["name"],data[i]["id"],data[i]["category"],data[i]["price"]["price"],data[i]["rating"]['average'],data[i]["iconImage"])
    html = html+'</table></body>'
    return html 

def GetAssetIdByUrl(url):
    splitted = str(url).split('-')
    return splitted[len(splitted)-1]
 
def GetAssetInfoByUrl(url):
    return GetAssetInfoById(GetAssetIdByUrl(url))

def GetAssetInfoById(idAsset):
    payloadInfo=[
        {
            "query":"query Product { product(id: $id) { ...product __typename } } fragment product on Product { id productId itemId slug name description rating { average count __typename } currentVersion { id name publishedDate __typename } reviewCount downloadSize assetCount publisher { id name url supportUrl supportEmail gaAccount gaPrefix __typename } mainImage { big facebook small icon icon75 __typename } originalPrice { itemId originalPrice finalPrice isFree discount { save percentage type saleType __typename } currency entitlementType __typename } images { type imageUrl thumbnailUrl __typename } category { id name slug longName __typename } firstPublishedDate publishNotes supportedUnityVersions state overlay overlayText popularTags { id pTagId name __typename } plusProSale licenseText __typename } ",
            "variables":{
                "id":idAsset
            },
            "operationName":"Product"
        }
    ] 
    return s.post(BATCH,headers=HEADERS,json=payloadInfo).json()[0]['data']['product']
    

def Search(phrase,category=''):
    resArray =[]
    payloadSearch=[{
    "query":"query SearchResults($q: [String], $page: Int, $rows: Int, $orderBy: Int, $reverse: Boolean) { searchPackageFromSolr(q: $q, page: $page, pageSize: $rows, sort_by: $orderBy, reverse: $reverse) { results { ... on ProductQ { ...productQ __typename } __typename } category { name count __typename } onSale { name count __typename } exclude { name count __typename } plusPro { name count __typename } free { name count __typename } publisherSuggest { name count __typename } platform { name count __typename } srp { name count __typename } automotive { name count __typename } aec { name count __typename } snaps { name count __typename } discount50 { name count __typename } discount70 { name count __typename } stats { min max __typename } total __typename } } fragment productQ on ProductQ { id name rating { average count __typename } publisherName publisherId category mainImage iconImage price { price originPrice __typename } plusProSale onSale elevated url isNew partner labels __typename } ",
    "variables":{
        "q":[
            "category:"+category,
            "q:"+phrase
                ],
                "page":0,
                "rows":1000 if MAX_ITEMS==-1 else MAX_ITEMS,
                "orderBy":1,
                "reverse":False
    },
    "operationName":"SearchResults"
}]
    jsonRes = s.post(BATCH,headers=HEADERS,json=payloadSearch).json()[0]['data']['searchPackageFromSolr']['results']
    for i in range(0,len(jsonRes)):
        if i > MAX_ITEMS and MAX_ITEMS != -1:
            return resArray
        resArray.append(jsonRes[i])
    return resArray

def SaveToFile(data,path):
    with open(path, 'w') as f:
        json.dump(data, f)


#************MAIN*************

#MAX_ITEMS = int(input('Введите максимальное кол-во материалов (0 - без ограничений): '))

Init(HOST)
data = Search(input('Введите поисковый запрос: '),input('Введите название категории, или ENTER ,чтобы искать везде: '))
#data = GetAssetInfoByUrl(input('Asset URL: '))

print(f'\n Нашлось {len(data)} материалов по вашему запросу. \n')
data = Html(data)
SaveToFile(data,FILES_PATH+HTML_FILE)


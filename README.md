# AssetStore-Simple-Wrapper
Search,GetAssetInfo  functions of AssetStore on Python

:white_check_mark:  def Search(phrase)   
:white_check_mark:  def GetAssetInfo(idAsset)

<a target="_blank" href="https://radikal.ru"><img src="https://c.radikal.ru/c08/2008/72/5ab6352567f4.png" /></a>


## Quick Start
```python
import requests
import json

s = requests.Session()
HOST = 'https://assetstore.unity.com'
EVENT = 'https://prd-lender.cdp.internal.unity3d.com/v1/events'
BATCH = 'https://assetstore.unity.com/api/graphql/batch'

Init(HOST)
data = Search('UFPS')

for i in range(0,GetLength(data)):
    item = JsonToDict(data,i)
    print(f'\nID: {item["id"]}')
    print(f'Title: {item["name"]}')
    print(f'Publisher: {item["publisherName"]}')
    print(f'PublisherId: {item["publisherId"]}')
    print(f'Category: {item["category"]}')
    print(f'Price: {item["price"]["price"]}')
    print(f'iconImage: {item["iconImage"]}')
    print(f'MainImage: {item["mainImage"]}')
    
info = GetAssetInfo(JsonToDict(data,0)["id"])
print(info)
```
## Examples
```python
Init('https://assetstore.unity.com')
Url = 'https://assetstore.unity.com/packages/tools/visual-scripting/dotween-pro-32416'
Id = GetAssetIdByUrl(Url)
Info = GetAssetInfoById(Id)
Info_2 = GetAssetInfoByUrl(Url)

#print(Info) or print(Info2)
#Output (Json):
#[{"data": 
{"product": {"id": "33903", "productId": "274979513323", "itemId": "274935347770", "slug": "flowcanvas-33903", "name": "FlowCanvas", "description": "<br>#####<strong>\n-------------------------------------<br>\n------ Summer Sale 20% off! ------<br>\n-------------------------------------<br>\n<br></strong>\n<br>\n<strong>'.Net #4.x' Equivalent Runtime Version is required.<br>'.Net 3.5 (deprecated)' is no longer supported.</strong><br>\n<br>\n<a #href=\"https://flowcanvas.paradoxnotion.com/features-comparison/\">[Features Comparison]</a><br>\n<a href=\"http://www.flowcanvas.paradoxnotion.com\">[Documentation, #Forums, Downloads]</a><br>\n<a href=\"https://discord.gg/97q2Rjh\">[Join Us On Discord]</a><br>\n<br>\n<strong>FlowCanvas</strong> is a powerful and feature-rich Visual #Scripting Solution for Unity, empowering you to create and manipulate virtually any aspect of gameplay elements for your games in a very similar fashion to Unreal #Blueprints, but with far less programming knowledge required all around.<br>\n<br>\n<strong>FlowCanvas</strong> .........
```



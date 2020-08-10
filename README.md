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
url = 'https://assetstore.unity.com/packages/tools/visual-scripting/flowcanvas-33903'
Id = GetAssetIdByUrl(Url)
info = GetAssetInfoById(Id)
info_2 = GetAssetInfoByUrl(Url)

print(info)
```
#### Output example (Json):

#### [{"data": {"product": {"id": "33903", "productId": "274979513323", "itemId": "274935347770", "slug": "flowcanvas-33903", "name": "FlowCanvas", "description": "<strong>FlowCanvas</strong> is a powerful and feature-rich Visual Scripting Solution for Unity, empowering you to create and manipulate virtually any aspect of gameplay elements for your games in a very similar fashion to Unreal Blueprints, but with far less programming knowledge required all around.<br>\n<br>\n<strong>FlowCanvas</strong> and more...




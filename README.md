# AssetStore-Simple-Wrapper
Search,GetAssetInfo  functions of AssetStore on Python
<br><br>
:white_check_mark:  def Search(phrase)   
:white_check_mark:  def GetAssetInfo(idAsset)
<br><br>
<a target="_blank" href="https://radikal.ru"><img src="https://c.radikal.ru/c08/2008/72/5ab6352567f4.png" /></a>
____
<br>
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
<br>





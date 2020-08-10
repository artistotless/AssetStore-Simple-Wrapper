# AssetStore-Simple-Wrapper
Search,GetAssetInfo  functions of AssetStore on Python

:white_check_mark:  def Search(phrase)   
:white_check_mark:  def GetAssetInfo(idAsset)

<a target="_blank" href="https://radikal.ru"><img src="https://c.radikal.ru/c08/2008/72/5ab6352567f4.png" /></a>
____

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
```



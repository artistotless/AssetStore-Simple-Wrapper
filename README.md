# Unity AssetStore API Wrapper
Search, GetAssetInfo functions of AssetStore on Python

:white_check_mark:  Search(phrase,category='')  

:white_check_mark:  GetAssetInfoById(id)

:white_check_mark:  GetAssetInfoByUrl(url)

:white_check_mark:  GetAssetIdByUrl(url)

<a target="_blank" href="https://radikal.ru"><img src="https://c.radikal.ru/c08/2008/72/5ab6352567f4.png" /></a>

## Requirements

*Python v3.7*

## Quick Start
```python
import requests
import json

s = requests.Session()
HOST = 'https://assetstore.unity.com'
EVENT = 'https://prd-lender.cdp.internal.unity3d.com/v1/events'
BATCH = 'https://assetstore.unity.com/api/graphql/batch'
FILES_PATH = '/home/admin/web/site.ru/public_html/files/'

Init(HOST)

res = Search('UFPS')
for key,value in res[0].items():
    print(f"{key} : {value}")

asset = GetAssetInfoByUrl('https://assetstore.unity.com/packages/templates/systems/ufps-ultimate-fps-106748')
print(asset['name'])
print(asset['downloadSize'])
print(asset['description'])

SaveToFile(asset,FILES_PATH + 'asset.txt')

```

### Result of GetAssetInfoByID(id) or GetAssetInfoByUrl(url)
```python
# For example: print(GetAssetInfoById(14290)['name']) || Output: Final IK
# Full list of indexes:
['id']
['productId']
['itemId']
['slug']
['name']
['description']
['rating']
['currentVersion']
['reviewCount']
['downloadSize']
['assetCount']
['publisher']
['mainImage']
['originalPrice']
['images']
['category']
['firstPublishedDate']
['publishNotes']
['supportedUnityVersions']
['state']
['overlay']
['overlayText']
['plusProSale']
['licenseText']
```
### Result of Search(phrase,category='')
```python
# For example: 
results = Search('UFPS')
print(len(results))
print(results[0]['name'])
print(results[0]['price']['price'])
print(results[0]['category'])
#Also u can search, using a category
results = Search('UFPS','templates')

# Full list of indexes:
['id']
['name']
['rating']
['publisherName']
['publisherId']
['category']
['mainImage']
['iconImage']
['price']{price}        
['plusProSale']  
['onSale']
['elevated']     
['url']
['isNew']        
['partner']      
['labels']
```

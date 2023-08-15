# UpAnime

## Search
Details regarding the usage of the search function.
```
http://127.0.0.1:8000/manga/{query}
```

```python
import requests

# Using the example query "dragon".
url = "http://127.0.0.1:8000/manga/dragon"
response = requests.get(url)
data = response.json()

print(data)

```
### Json Output Format:
```json
{
    "id": {
        "title": "string",
        "author": "string",
        "updated_on": "string"
    },
```

## Get Manga Info
Details regarding the usage of the get manga info function.
```
http://127.0.0.1:8000/manga/info/{id}
```

```python
import requests

# Using the example query "pb992910".
url = "http://127.0.0.1:8000/manga/info/pb992910"
response = requests.get(url)
data = response.json()

print(data)
```
### Json Output Format:
```json
{
    "title": "string",
    "author": [
        "string"
    ],
    "status": "string",
    "updated": "string",
    "genres": [
        "string"
    ],
    "alternative": [
        "string"
    ],
    "chapters": [
        {
            "chapter-id": "string"
        },
    ]
}
```
## Get Manga Chapter Pages
Details regarding the usage of the Get manga chapter pages function.
```
http://127.0.0.1:8000/manga/info/{id}/{chapter-id}
```
```python
import requests

# Using the example id "pb992910".
# Using the example chapter-id "chapter-1".
url = "http://127.0.0.1:8000/manga/info/pb992910/chapter-1"
response = requests.get(url)
data = response.json()

print(data)

```
### Json Output Format:
```json
 "chapter-id": [
        {
            "alt": "string",
            "img": "string"
        }
              ]
}
```

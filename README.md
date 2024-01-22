# sfile-api
for search file from sfile.mobi
# search
with required keyword
```
https://sfile-api.vercel.app/search/<keyword>
```
next if true:
```
https://sfile-api.vercel.app/<keyword>/<page>
```
## result
```json
{
    "author": "Latip176",
    "data": {
        "data": [
            {
                "icon": "// icon file",
                "size": "// size file",
                "title": "// name file",
                "id": "// id file"
            },
            // other data
        ],
        "file_found": // int,
        "next": // None | True
    },
    "msg": "success"
}

# download
with required id file
```
https://sfile-api.vercel.app/download/<id>
```
## result
```JSON
{
    "author": "Latip176",
    "data": {
        "url": "// url download",
        "date": "// date of post file",
        "downloaded": // downloaded count
    },
    "msg": "success"
}
```

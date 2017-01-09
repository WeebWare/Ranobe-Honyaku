### /api/v1/applications

### GET
`Arguments`
```
```
`Returns`
```
Array of application objects
```

`Example response`
```json
HTTP/1.0 200 OK
Content-Length: 182
Content-Type: application/json
Date: Tue, 13 Dec 2016 00:49:16 GMT
Server: Werkzeug/0.11.11 Python/3.5.2

[
    {
        "id": "1",
        "name": "Ranobe-Honyaku iOS",
        "url": "https://ranobe-honyaku.moe/applications/1",
        "source": "https://github.com/Ranobe-Honyaku/iOS",
        "owner": "Recchan",
        "description": "The official iOS client for Ranobe-Honyaku."
    }
]
```

### POST

`Arguments`
```
Authorization token (required)
```

`Returns`
```
The created application object
```
`Example Response`
```json
HTTP/1.0 201 CREATED
Content-Length: 251
Content-Type: application/json
Date: Tue, 13 Dec 2016 01:53:57 GMT
Server: Werkzeug/0.11.11 Python/3.5.2

{
    "id": "1",
    "name": "Ranobe-Honyaku iOS",
    "url": "https://ranobe-honyaku.moe/applications/1",
    "source": "https://github.com/Ranobe-Honyaku/iOS",
    "owner": "Recchan",
    "description": "The official iOS client for Ranobe-Honyaku."
}
```

### DELETE

`Arguments`
```
Authorization token (required)
```
`Returns`
```
Returns the deleted Application object without an id
```
`Example Response`
```json
HTTP/1.0 200 OK
Content-Length: 280
Content-Type: application/json
Date: Tue, 13 Dec 2016 02:30:59 GMT
Server: Werkzeug/0.11.11 Python/3.5.2
{
  "description": "The official android client for Ranobe-Honyaku, built on Electron",
  "id": null,
  "name": "Ranobe-Honyaku Desktop",
  "owner": "Recchan",
  "source": "https://github.com/Ranobe-Honyaku/Desktop",
  "url": "https://ranobe-honyaku.moe/applications/3"
}
```
>>>>>>> Stashed changes

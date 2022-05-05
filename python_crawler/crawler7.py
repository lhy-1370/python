import requests as req

url = "https://webhook.site/d0b77355-4d96-4cee-a0cc-329cab061a1f"
#res = req.get(url, headers={
#    "User-Agent": "fastcampus/B1"
#})

res = req.post(url, data={
    "name": "hi"
})

print(res.text)
import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

def aes_encrypt(text,key,iv):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    padded_text = pad(text.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return b64encode(ciphertext).decode('utf-8')

def b(a,b):
    c = b
    d = '0102030405060708'
    e = a
    f = aes_encrypt (e,c,d)
    return f

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"

d = {
    "i0x": "",
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_2611222522",
    "threadId": "R_SO_4_2611222522"
}

i = "2dGXFZnqc39mWRJb"

encSecKey_x = "02c642e3dddf22c732af1811ce28eaecbf6dbea4f558ee60392a80f74c0303676e4aae4719f1d93fc1d8ad37a0bd7ffb24c91301acf496654903df5038e581c8960abe09457a145bd0a1af7d4fb4cd2a45d9ee01f2a80a5ee1a5fbde8e00b8dc07c83430b19386d28de9177119d4e05ffffe346abe92a6f5c77d9949cb943283"

d_json = json.dumps(d)
textcent = b(d_json,g)
textcent = b(textcent,i)

haeders = {
     "user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
data = {
    "params": textcent,
    "encSecKey": encSecKey_x
}
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

resp = requests.post(url = url , headers = haeders, data = data)

if resp.status_code != 200:
    print(f"HTTP Request failed with status code: {resp.status_code}")
    print("Response content:")
    print(resp.text)
else:
    try:
        # 尝试解析 JSON
        data = resp.json()
        # 提取评论
        comments = data.get('data', {}).get('comments', [])
        # 将评论和评论者的名字写入文本文件
        with open('comments.txt', 'w', encoding='utf-8') as file:
            for comment in comments:
                user_name = comment.get('user', {}).get('nickname', 'Unknown')
                content = comment.get('content', '')
                file.write(f"{user_name}: {content}\n")
        print("Comments and user names have been saved to comments.txt")
    except requests.exceptions.JSONDecodeError as e:
        # 如果解析失败，打印响应内容
        print("Failed to decode JSON. Response content:")
        print(resp.text)


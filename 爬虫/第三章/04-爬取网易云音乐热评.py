# 1.找到未加密的参数                # 由 window.arsea(参数,xxx,xxx,xxx) 函数生成而来，需要打开浏览器开发者工具一步步找
# 2.想办法把参数进行加密(必须参考网易的逻辑)，params => encTest,encSecKey => encSenKey
# 3.请求到网易，拿到评论信息

import json
from base64 import b64encode

import requests
from Crypto.Cipher import AES

url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
# 请求方式是POST
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1330348068",
    "threadId": "R_SO_4_1330348068"
}

f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
e = "010001"
i = "d5bpgMn9byrHNtAh"


def get_encSecKey():
    return "1b5c4ad466aabcfb713940efed0c99a1030bce2456462c73d8383c60e751b069c24f82e60386186d4413e9d7f7a9c76600c012b61adf418af84eb0be5b735988addafbd7221903c44d027b2696f1cd50c49917e515398bcc6080233c71142d226ebb"


def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  # 返回的就是params


def enc_params(data, key):  # 加密过程
    iv = "0102030405060708"
    aes = AES.ner(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创建加密器
    bs = aes.encrypt(data)  # 加密
    return str(b64encode(bs), "utf-8")  # 转化成字符串返回


# 处理加密过程
'''
function a(a) {     # 随机的16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length,   # 随机数
            e = Math.floor(e),  # 取整
            c += b.charAt(e);   # 取字符串中的xxx位置 会出来16个随机的字母或数字
        return c
    }
    function b(a, b) {  # a是要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)  # b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # e是数据
          , f = CryptoJS.AES.encrypt(e, c, {    # c 是加密的密钥
            iv: d,  # 便宜量
            mode: CryptoJS.mode.CBC # 模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {    d:数据 , e:010001 , f:很长 ， g:0CoJUm6Qyw8W8jud
        var h = {}  # 空对象
          , i = a(16);  # i就是一个16位的随机值
        return h.encText = b(d, g), # g是密钥
        h.encText = b(h.encText, i),    # 返回的就是params，i也是密钥
        h.encSecKey = c(i, e, f),   # 得到的就是encSecKey，e和f是定死的，如果此时我把i固定,得到的key一定是固定的
        h
    }
    
    两次加密：
    数据+g => b => 第一次加密+i => b = params
'''

resp = requests.put(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

print(resp.text)

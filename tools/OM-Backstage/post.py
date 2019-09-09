# coding=utf-8
import requests
url = "http://119.28.249.120:8080/job/Sargam-Android/109/artifact/app/build/finally/resource_mapping_sargamRelease-minApi17-arm64-v8a-83949001-2019-08-12-13-43.txt"

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://119.28.249.120:8080/job/Sargam-Android/109/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'jenkins-timestamper-offset=-28800000; ACEGI_SECURITY_HASHED_REMEMBER_ME_COOKIE=eWFvbGlhbmcuY3VpOjE1NjU4Mzg4MzU2MDQ6MzQ3NzlmODk4MzE1ZjFkNjhkY2QxMTNiOTg0NjA5M2ZhNjI4YTVhMDhjM2ViOWUwMmUxMjc0ZjFiZjkzYTYzMw==; hudson_auto_refresh=false; screenResolution=1366x768; SL_G_WPT_TO=zh; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; JSESSIONID.a1ccadc4=node01awsa3l02e2l31or4h87mpwu5z18203674.node0',
    'If-Modified-Since': 'Mon, 12 Aug 2019 13:52:59 GMT'
}

r = requests.post(url, headers=headers)
print(r.content)


if __name__ == '__main__':
    pass

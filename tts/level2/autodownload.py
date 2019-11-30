import requests
import os
import re

nowday = 1
urlrule = "http://resources.tmooc.cn/tctm/TTS/ttsPage/L1APy/L1APy_V01/Level_2/"
endurl = "/COURSE/ppt.html"

def download_img(img_url,name):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    r = requests.get(img_url, headers=header, stream=True)
    print('img status:' + str(r.status_code)) # 返回状态码
    if r.status_code == 200:
        open(name, 'wb').write(r.content) # 将内容写入图片
    del r

while True:
    pptrule = ""
    if nowday < 10:
        pptrule = "DAY0"+str(nowday)  
    else:
        pptrule = 'DAY' + str(nowday)
    nowday+=1     
    res = requests.get(urlrule+pptrule+endurl)
    print("download "+pptrule+":")
    print('html staus:' + str(res.status_code))
    if res.status_code != 200:
        print("No such file")
        continue
    else:
        print("File acquired")
    res.encoding = 'utf-8'
    r = res.text;
    dpath = os.getcwd();
    os.mkdir(dpath+'\\'+pptrule)
    c = open(pptrule+'/'+pptrule+'.html','w+',encoding='utf-8');
    c.write(r);
    c.close()
    img_url_list = re.findall('<img width="960px" src="(.*?)" />',r)
    for img in img_url_list: 
        download_img(urlrule+pptrule+'/COURSE/'+img,pptrule+"/"+img)
    print("done")
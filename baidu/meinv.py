import requests

# baidu_image 函数定义
def baidu_image(page):
    # 参数pn是分页条件
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11938254251170471042&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=' \
          '&rn=30&gsm=d2&1669557713502=&pn='
    url = url + str(page)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

    # 发送请求，获取json数据
    response_json = requests.get(url, headers=headers).json()

    # print(response_json)

    num = page-30
    image_urls = []
    # 获取图片url
    for data in response_json['data']:
        if len(data) != 0:
            # print(data)
            image_urls.append(data['thumbURL'])

    for image_url in image_urls:
        # 发送请求
        resp = requests.get(image_url, headers=headers)

        num = num + 1
        # 写入图片到本地
        with open('testFile/'+str(num) + '.jpg', 'wb') as file:
            file.write(resp.content)
# baidu_image 函数定义结束

# 下载图片
for i in range(10):
    baidu_image((i+1)*30)

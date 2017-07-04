import urllib.request
from bs4 import BeautifulSoup

url = "http://hzzby.360jlb.cn/"
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content,'lxml')
# 根据class为list_item的a标签
weenkend = soup.find_all('div', class_="in-pic3")
tags = weenkend[0].find_all('li')
for tag in tags:
        image = tag.img['src']
        place = tag.select('.place')[0].get_text()
        time = tag.select('.time')[0].get_text()
        price = tag.select('.price-wrap')[0]
        normal_price = price.get_text()
        vip_price = price.find_all('span')[0].get_text()
        print(image)
        print(place)
        print(time)
        print(normal_price)
        print(vip_price)
        print('------------------------------------')
        # article_user = tag.p.a.get_text()
        # article_user_url = tag.p.a['href']
        # created = tag.p.span['data-shared-at']
        # article_url = tag.h4.a['href']
        #
        # # 可以在查找的 tag 下继续使用 find_all()
        # tag_span = tag.div.div.find_all('span')
        #
        # likes = tag_span[0].get_text(strip=True)
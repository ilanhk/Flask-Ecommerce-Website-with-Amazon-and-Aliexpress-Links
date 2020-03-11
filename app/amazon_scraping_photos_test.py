from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.amazon.com/dp/B07GR4YJHH').text

soup = BeautifulSoup(source, 'lxml')

photo_cont = soup.find("div", {"id": "altImages"})



print(photo_cont)
print(source)



# <ul class="a-unordered-list a-nostyle a-button-list a-horizontal a-spacing-top-micro">
# <li class="a-spacing-small item imageThumbnail a-declarative" data-ux-click=""><span class="a-list-item">
# <span class="a-button a-button-thumbnail a-button-toggle a-button-selected a-button-focus" id="a-autoid-4"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="a-autoid-4-announce"><span class="a-button-text" aria-hidden="true" id="a-autoid-4-announce">
# <img src="https://images-na.ssl-images-amazon.com/images/I/51vcArUHlQL._AC_US40_.jpg">
# </span></span></span>
# </span></li><li class="a-spacing-small item imageThumbnail a-declarative" data-ux-click=""><span class="a-list-item">
# <span class="a-button a-button-thumbnail a-button-toggle" id="a-autoid-5"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="a-autoid-5-announce"><span class="a-button-text" aria-hidden="true" id="a-autoid-5-announce">
# <img src="https://images-na.ssl-images-amazon.com/images/I/41u4Te4opiL._AC_US40_.jpg">
# </span></span></span>
# </span></li><li class="a-spacing-small item imageThumbnail a-declarative" data-ux-click=""><span class="a-list-item">
# <span class="a-button a-button-thumbnail a-button-toggle" id="a-autoid-6"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="a-autoid-6-announce"><span class="a-button-text" aria-hidden="true" id="a-autoid-6-announce">
# <img src="https://images-na.ssl-images-amazon.com/images/I/51Balfx%2BOnL._AC_US40_.jpg">
# </span></span></span>
# </span></li><li class="a-spacing-small item imageThumbnail a-declarative" data-ux-click=""><span class="a-list-item">
# <span class="a-button a-button-thumbnail a-button-toggle" id="a-autoid-7"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="a-autoid-7-announce"><span class="a-button-text" aria-hidden="true" id="a-autoid-7-announce">
# <img src="https://images-na.ssl-images-amazon.com/images/I/41lfKBrozGL._AC_US40_.jpg">
# </span></span></span>
# </span></li><li class="a-spacing-small item imageThumbnail a-declarative" data-ux-click=""><span class="a-list-item">
# <span class="a-button a-button-thumbnail a-button-toggle" id="a-autoid-8"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="a-autoid-8-announce"><span class="a-button-text" aria-hidden="true" id="a-autoid-8-announce">
# <img src="https://images-na.ssl-images-amazon.com/images/I/51480mdYZAL._AC_US40_.jpg">
# </span></span></span>
# </span></li><li class="a-spacing-small item imageThumbnail a-declarative" data-ux-click=""><span class="a-list-item">
# <span class="a-button a-button-thumbnail a-button-toggle" id="a-autoid-9"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="a-autoid-9-announce"><span class="a-button-text" aria-hidden="true" id="a-autoid-9-announce">
# <img src="https://images-na.ssl-images-amazon.com/images/I/5115gPQPiYL._AC_US40_.jpg">
# </span></span></span>
# </span></li><li class="a-spacing-small item imageThumbnail a-declarative" data-ux-click=""><span class="a-list-item">
# <span class="a-button a-button-thumbnail a-button-toggle" id="a-autoid-10"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="a-autoid-10-announce"><span class="a-button-text" aria-hidden="true" id="a-autoid-10-announce">
# <img src="https://images-na.ssl-images-amazon.com/images/I/41vofkxe6dL._AC_US40_.jpg">
# </span></span></span>
# </span></li></ul>
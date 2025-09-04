
from PIL import ImageOps, Image
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import os

# 从网站下载二维码图片
# if not os.path.exists('captchas'):
#     os.makedirs('captchas')
    
# for i in range(1, 100):
#     bs = BeautifulSoup(urlopen(f'https://pythonscraping.com/humans-only/'))
#     imgUrl = bs.find('img', {'class': 'wpcf7-captchac'})['src']
#     print('imgUrl: ', imgUrl)
#     urlretrieve(imgUrl, f'captchas/{imgUrl.split("/")[-1]}')

# 用Pillow处理图片（背景白，字体变黑）
def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 255 if x<143 else 0)
    image = ImageOps.expand(image, border=20, fill='white')
    image.save(imagePath)
    
for filename in os.listdir('captchas'):
    if '.png' in filename:
        cleanImage(f'captchas/{filename}')

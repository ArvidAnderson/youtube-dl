from PIL import Image
import requests #For thumbnail url img


def dl_thumbnail_url(url_thumbnail, img_res):
    response = requests.get(url_thumbnail, stream=True)
    img = Image.open(response.raw)
    img = img.resize((img_res), Image.ANTIALIAS)
    img = img.save('thumbnail_temporary.png')
    img_file_name = 'thumbnail_temporary.png'
    return img_file_name
import imageio.v3 as iio
from PIL import Image
import numpy as np


yollar=[""]#BURAYA EKLİYORSUN NE OLDUĞUNU


calısma_alanları=[]


for elemanlar in yollar:
    arr=iio.imread(elemanlar)
    img=Image.fromarray(arr).convert('RGB')
    img=img.resize((256,256))
    calısma_alanları.append(np.array(img))

iio.imwrite(
    "deneme.gif",
    calısma_alanları,
    save_all=True,
    duration=500,
    loop=0
)
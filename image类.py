from PIL import Image
from PIL import ImageFilter   
im = Image.open("C:\\Users\\tjt\\Desktop\\1.png")
L_img = im.convert("L")  #将RGBA模式的im转为L模式的图片
crop_img = im.crop((100,100,200,200))   #切割图片
copy_img = im.copy()  #复制图片
im.paste(crop_img,(0,0,100,100))    #将crop_img粘贴到im的(0,0,100,100)区域
resize_img = im.resize((200, 100))   #重新定义图片大小


new_img = Image.new("RGB",(200,200),(255,0,0))   #new(mode,size,color)

source = im.split()   #im为RGBA格式，将其三个通道分离, source为图像元组（R,G,B,A），三个都是图像
composite_img = Image.composite(source[0],source[1],source[2])   #composite(img1,img2,mask)，都是图片，mask作为透明度
blend_img = Image.blend(source[0],source[1],0.2)  #blend(img1,img2,alpha),将两个图片的像素值相加，alpha为比例，0时即为img1，1时即为img2

merge_img = Image.merge("RGBA",source)  #merge(mode,bands),bands为图像的列表或元组，将bands合并成一个图像
img_bands = im.getbands() #将im通道拆分，返回通道名称元组("R","G","B","A")

img_pixel = im.getpixel((0,0))   #返回像素点值
pix = im.load()    #加载图片，用于返回像素值或更改，比getpixel()快
print (pix[0,0])
pix[0,0] = (255,255,255)

im_45 = im.rotate(45)
im_30 = im.rotate(30, Image.NEAREST,1)   #旋转图片（degree,filter,expand）,expand为true表示输出图像足够大，可以装载旋转后的图像
im_30.show()

bluF = im.filter(ImageFilter.BLUR)                ##均值滤波
conF = im.filter(ImageFilter.CONTOUR)             ##找轮廓
edgeF = im.filter(ImageFilter.FIND_EDGES)         ##边缘检测
conF.show()

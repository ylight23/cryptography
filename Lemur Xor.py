from PIL import Image, ImageChops
import os
import numpy as np
#mo file anh
os.chdir(r'H:') 
im1 = Image.open('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
im2 = Image.open('flag_7ae18c704272532658c10b5faad06d74.png')
#chuyen anh thanh mang numpy co do do dai 256 phan tu
i1= np.array(im1)*255
i2= np.array(im2)*255
#xor bit lai 2 mang voi nhau 8 bit 1
result = np.bitwise_xor(i1,i2).astype(np.uint8)
#convert ket qua thanh anh va hien thi

Image.fromarray(result).show()
# print(im1.mode,im2.mode)
# print(im1.format,im2.format)
# print(im1.size, im2.size)
# im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
# im3.show()
# im3.save("Your_path/im3.png")




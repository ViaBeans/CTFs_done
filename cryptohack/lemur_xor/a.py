from PIL import Image, ImageChops  
import PIL
     
# creating a image1 object  
im1 = Image.open("./lemur.png")
     
# creating a image2 object  
im2 = Image.open("./flag.png")

im3 = Image.new ('RGB', (im1.width, im1.height))

for i in range(im1.width):
    for j in range(im1.height):
        p1 = im1.getpixel((i,j))
        p2 = im2.getpixel((i,j))
        r3 = p1[0] ^ p2[0]
        g3 = p1[1] ^ p2[1]
        b3 = p1[2] ^ p2[2]
        p3 = (r3, g3, b3)
        im3.putpixel((i,j), p3)

im3.save("res.png")

     
# applying logical_xor method  
     

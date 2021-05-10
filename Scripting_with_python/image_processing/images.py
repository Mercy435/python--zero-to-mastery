from PIL import Image, ImageFilter

img1 = Image.open('imagejpg/4.1 bulbasaur.jpg')
img2 = Image.open('imagejpg/4.3 pikachu.jpg')
img3 = Image.open('imagejpg/4.4 charmander.jpg')
img4 = Image.open('imagejpg/4.3 squirtle.jpg')

print(dir(Image))  # shows methods for image
print(img1)  # returns an object of the image
print(img2.format)  # returns jpeg
print(img3.size)  # returns size in a tuple
print(img3.mode)  # returns rgb red green blue
print(dir(img3))  # returns properties of the img
print(img3.getpixel)
# to filter the image, import imagefilter from pillow
filtered_img1 = img1.filter(ImageFilter.BLUR)
filtered_img1.save("images/blur.png", 'png')  # to create a new file that is blur in png format as well as save it

filtered_img2 = img2.filter(ImageFilter.SMOOTH)  # works better with landscape pictures
filtered_img2.save("images/smooth.png", 'png')

filtered_img3 = img3.filter(ImageFilter.SHARPEN)
filtered_img3.save("images/sharpen.jpeg", 'jpeg')
# png and jpeg supports these filters

fil_img4 = img4.convert('L')  # L is greyscale
fil_img4.save("images/grey.png", "png")  # turns color of image grey
fil_img4.show()  # shows us the image

crooked = filtered_img2.rotate(180)  # rotate objects
crooked.save('images/rotate_grey.jpeg', 'jpeg')

resize = filtered_img1.resize((30, 30))  # resize objects,, resize is in a tuple
resize.save('images/resize_blur.png', 'png')

box = (100, 100, 400, 400)  # to crop images
region = filtered_img2.crop(box)
region.save('images/cropped_smooth.png', 'png')


img_ = Image.open('images/6.1 astro.jpg')
print(img_.size)  # 5611,5399

# resizing the image cos its too big
new_img = img_.resize((400, 400))  # since the original size of the image wasnt even, doing this resizing squashes it
new_img.save('thumbnail.png', 'png')

# To keep the aspect ratio, so it isnt squashed, do this instead of resize
img_.thumbnail((400,400)) #this is the max values
img_.save('thumbnail.jpg')

print(img_.size)

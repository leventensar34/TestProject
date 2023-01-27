from PIL import Image, ImageFilter

image = Image.open("kus.jpg")

image.show()

image.save("kus2.jpg")

image.rotate(180).save("kus3.jpg")

image.rotate(90).save("kus4.jpg")

image.convert(mode="L").save("kus5.jpg")

degistir = (960, 600)

image.thumbnail(degistir)

image.save("kus6.jpg")

image.filter(ImageFilter.GaussianBlur(5)).save("kus7.jpg")

kirpilacak_alan = (340, 0, 950, 600)

image2 = Image.open("atatürk.jpg")

image2.crop(kirpilacak_alan).save("atatürk1.jpg")

import qrcode

img = qrcode.make('안녕안녕')
img.save('C:/Source/hello.png')
print(type(img))
print(img.size)
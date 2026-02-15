import qrcode
print("qr code generator")
data=input("enter the text or url:")
filename=input("enter the  file name(without extension .png):")
qr =qrcode.QRCode(
    version=None,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_colour= ' black', back_colour='white')
img.save(filename+'.png')
print('qr code generated successfully')
img.show()
# qr.print_ascii()
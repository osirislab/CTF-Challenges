import Image

img = Image.open( "img.png" )
width, height = img.size
pix = img.load()
result = ""

def magic( pix ):
	k = 1.158371
	res = (pix[0]&0x1f)*k+(pix[1]&0x3f)*k+(pix[2]&0x7f)*k
	return int( res )

for w in range(width):
	for h in range(height):
		result += chr( magic( pix[w,h] ) )
		
open("img.encode","wb").write( result )
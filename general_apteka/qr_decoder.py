from pyzbar.pyzbar import decode
from PIL import Image

def decoder(object):
	d = decode(Image.open(object))
	code = d[0].data.decode('ascii')
	return code
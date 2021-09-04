#OCR
import PIL.Image
import PIL.ImageEnhance
import PIL.ImageFilter
import pytesseract as ocr
#Referenciar exe tesseract
ocr.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#Manipulação de imagem binária
fp = open("test.jpg","rb")

#Alterando imagem
img = PIL.Image.open(fp)
im = img.filter(PIL.ImageFilter.MedianFilter())
enhancer = PIL.ImageEnhance.Contrast(im)
img = enhancer.enhance(2)
im = img.convert('1')

#Platagem de imagem tratada
#im.show()

#Necessário pacote de idiomas indicado pelas variáveis de ambiente do sistema
text = ocr.image_to_string(img, lang='por')

#Print do texto extraído
print(text)


import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd='E:\Lib\site-packages\pytesseract'
#f=open('champ checklist','r')
#print(f.read())
#f.close()
img = cv2. imread ('shopImages/Aatrox.png',-1)
cv2.imshow ('image',img)
cv2.waitKey (0)
print(pytesseract.image_to_string(img))
print("wtf work god damn it")

#cv2.imwrite('Aatrox_copy.png',img)
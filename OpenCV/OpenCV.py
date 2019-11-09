import cv2

img=cv2.imread('galaxy.jpg',0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

cv2.imshow('Galaxy',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)


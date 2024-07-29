import cv2



source ="download.jpeg"
destination="newImage.png"
scale_percent = 50


src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
#cv2.imshow("titile",src)

cv2.waitKey(0)



new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)


dsize = (new_height , new_width)

output = cv2.resize(src , dsize)


cv2.imwrite('newImage.png',output)
cv2.waitKey(0)
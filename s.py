import cv2

img1 = cv2.imread('a.jpg')
img2 = cv2.imread('b.jpg')

v_img = cv2.vconcat([img1, img2])
h_img = cv2.hconcat([img1, img2])

cv2.imshow('Horizontal', h_img)
cv2.imshow('Vertical', v_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.10 다양한 흐림 필터로 잡음을 제거해 보자, 354쪽
#
import numpy as np
import cv2
path = "C:/Users/user/github/DataSciPy/data/image/"

original_image = cv2.imread(path + 'mandrill.png', 1)
result_image1 = cv2.GaussianBlur(original_image,  (9,9), 1)
result_image2 = cv2.medianBlur(original_image, 9)
result_image3 = cv2.bilateralFilter(original_image, 9, 50, 50)

cv2.imshow('original', original_image)
cv2.imshow('Gauss', result_image1)
cv2.imshow('bilateralFilter', result_image2)
cv2.imshow('medianBlur', result_image3)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
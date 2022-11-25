#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.8 이미지에 필터를 씌워 보자, 350쪽
#
import numpy as np
import cv2
path = "C:/Users/user/github/DataSciPy/data/image/"
org = cv2.imread(path + 'mandrill.png', 1)
5
kernel1 = np.ones((3, 3), np.float32) / 9
kernel3 = np.ones((5, 5), np.float32) / 25
kernel4 = np.ones((7, 7), np.float32) / 49
kernel2 = np.ones((9, 9), np.float32) / 81

averaged33 = cv2.filter2D(org, -1, kernel1)
averaged99 = cv2.filter2D(org, -1, kernel2)
averaged55 = cv2.filter2D(org, -1, kernel3)
averaged77 = cv2.filter2D(org, -1, kernel4)

cv2.imshow('original', org)
cv2.imshow('filtered1', averaged33)
cv2.imshow('filtered3', averaged55)
cv2.imshow('filtered4', averaged77)
cv2.imshow('filtered2', averaged99)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
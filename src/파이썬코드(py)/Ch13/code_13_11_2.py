#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 13.11 관심있는 곳만 남겨보자, 356쪽
#
import cv2
global color_image
path = "C:/Users/user/github/DataSciPy/data/image/"

# 트랙바가 변경되면 그 값을 임계치로 컬러 이미지를 이진화하여 창에 그림
def on_change_threshold(x):
   _, th_image = cv2.threshold(color_image, x, 255, cv2.THRESH_BINARY)
   cv2.imshow('Thresholding', th_image)


# 윈도를 생성함
cv2.namedWindow('Thresholding')
cv2.createTrackbar('threshold', 'Thresholding', 0, 255, on_change_threshold)

# 촛불 이미지를 읽음
color_image = cv2.imread(path + 'candles.jpg', cv2.IMREAD_COLOR)

# 처음에는 원본 이미지를 그림 (트랙바를 변경하면 임계치에 따라 이진화 결과 출력)
cv2.imshow('Thresholding', color_image)

# 다음 두 행은 키보드 입력을 기다렸다가 모든 창을 끄고 종료하는 코드
cv2.waitKey(0)
cv2.destroyAllWindows()
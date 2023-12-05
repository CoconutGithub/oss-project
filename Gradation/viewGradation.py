# import os,sys
# from PIL import Image


# img = Image.open('./Gradation/test.jpg')
# img.show()
from PIL import Image, ImageDraw

def visual_gradation(width, height, save_path):
    # 그라데이션을 위한 새로운 이미지 생성
    image = Image.new("RGB", (width, height))

    # 이미지에 그라데이션 값 적용
    draw = ImageDraw.Draw(image)
    for x in range(width):
        # 색상 그라데이션 계산 (빨간색에서 파란색까지)
        red = 0
        green = int(255 * (1.0 - x / width))
        blue = int(255 * (x / width))

        # 현재 열에 대한 선 그리기
        draw.line([(x, 0), (x, height)], fill=(red, green, blue))

    # 결과 이미지 저장
    image.save(save_path)

# 이미지 크기와 저장 경로 지정
image_width = 400
image_height = 200
output_image_path = "outputImage.jpg"

# 색상 그라데이션 시각화 수행
visual_gradation(image_width, image_height, output_image_path)
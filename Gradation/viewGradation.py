from PIL import Image, ImageDraw

def visual_gradation(width, height, save_path):
    # 새로운 이미지 생성
    image = Image.new("RGB", (width, height))

    # 이미지에 그라데이션 값 적용
    draw = ImageDraw.Draw(image)
    for x in range(width):
        # 색상 그라데이션 계산 (빨간색에서 파란색까지)

        # 색 변경하려면 수정가능(rgb값으로)
        red = 0
        green = int(255 * (1.0 - x / width))
        blue = int(255 * (x / width))

        # 현재 열에 대한 선 그리기
        draw.line([(x, 0), (x, height)], fill=(red, green, blue))

    image.save(save_path)

image_width = 400
image_height = 200
output_image_path = "./Gradation/outputImage.jpg"

visual_gradation(image_width, image_height, output_image_path)
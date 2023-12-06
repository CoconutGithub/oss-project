import os
from PIL import Image, ImageDraw, ImageFilter

def apply_gradation_filter(image,start,end,input_alpha=0.5):
    # 그라데이션 필터 적용
    width, height = image.size
    grad_image=visual_gradation(width, height,start,end)
    
    # 원본 이미지와 그라데이션 이미지를 합침
    blended_image = Image.blend(image.convert('RGB'), grad_image,input_alpha)
    blended_image = blended_image.convert('RGB')
    return blended_image


def visual_gradation(width, height,start,end):
    # 새로운 이미지 생성
    image = Image.new("RGB", (width, height))

    # 이미지에 그라데이션 값 적용
    draw = ImageDraw.Draw(image)
    for x in range(width):
        # 색상 그라데이션 계산 (빨간색에서 파란색까지)

        # 색 변경하려면 수정가능(rgb값으로)
        red = int(start[0]*(1.0-x/width)+end[0]*(x/width))
        green = int(start[1]*(1.0-x/width)+end[1]*(x/width))
        blue = int(start[2]*(1.0-x/width)+end[2]*(x/width))

        # 현재 열에 대한 선 그리기
        draw.line([(x, 0), (x, height)], fill=(red, green, blue))

    return image

#ff8647
#96d35f

#hex색상값 rgd로 변환
start_color_input = input("Enter start color (hex): ")
start_color = (int(start_color_input[0:2], 16), int(start_color_input[2:4], 16), int(start_color_input[4:6], 16))

end_color_input = input("Enter end color (hex): ")
end_color = (int(end_color_input[0:2], 16), int(end_color_input[2:4], 16), int(end_color_input[4:6], 16))

original_image_path = "oss-project/Gradation/test.jpg"
print(original_image_path)
original_image = Image.open(original_image_path)
filtered_image = apply_gradation_filter(original_image, start_color,end_color)

filtered_image.save("oss-project/Gradation/filtered_image.jpg")




import os,math
from PIL import Image, ImageDraw, ImageFilter

def apply_gradation_filter(image, start, end, input_alpha=0.5, shape='row'):
    # 그라데이션 필터 적용
    width, height = image.size

    if shape == 'row' or shape == 'col':
        grad_image = visual_gradation(width, height, start, end, shape)
    elif shape == 'circular':
        grad_image = circular_gradation(width, height, start, end)
    else:
        raise ValueError("Invalid shape. Use 'row', 'col', or 'circular'.")

    # 원본 이미지와 그라데이션 이미지를 합침
    blended_image = Image.blend(image.convert('RGB'), grad_image, input_alpha)
    blended_image = blended_image.convert('RGB')
    return blended_image

def visual_gradation(width, height, start, end, shape='row'):
    image = Image.new("RGB", (width, height))
    # 이미지 Draw 객체 생성

    draw = ImageDraw.Draw(image)

    if shape == 'col':
        for x in range(width):
            # 색상 그라데이션 계산
            red = int(start[0] * (1.0 - x / width) + end[0] * (x / width))
            green = int(start[1] * (1.0 - x / width) + end[1] * (x / width))
            blue = int(start[2] * (1.0 - x / width) + end[2] * (x / width))

            # 현재 열에 대한 선 그리기
            draw.line([(x, 0), (x, height)], fill=(red, green, blue))
    elif shape == 'row':
        for y in range(height):
            # 색상 그라데이션 계산
            red = int(start[0] * (1.0 - y / height) + end[0] * (y / height))
            green = int(start[1] * (1.0 - y / height) + end[1] * (y / height))
            blue = int(start[2] * (1.0 - y / height) + end[2] * (y / height))

            # 현재 열에 대한 선 그리기
            draw.line([(0, y), (width, y)], fill=(red, green, blue))
    else:
        raise ValueError("Invalid shape. Use 'row' or 'col'.")
    
    return image

def circular_gradation(width, height, start_color, end_color):
    # 새로운 이미지 생성
    image = Image.new("RGB", (width, height))

    # 이미지 Draw 객체 생성
    draw = ImageDraw.Draw(image)

    # 중심 좌표 및 반지름 계산
    center_x, center_y = width // 2, height // 2
    radius = min(center_x, center_y)

    # 원형 그라데이션 값 적용
    for y in range(height):
        for x in range(width):
            # 현재 좌표에서 중심 좌표까지의 거리 계산
            distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)

            # 반지름보다 크면 거리를 반지름으로 설정
            distance = min(distance, radius)

            # 거리에 따른 색상 계산
            ratio = distance / radius
            r = int(start_color[0] * (1.0 - ratio) + end_color[0] * ratio)
            g = int(start_color[1] * (1.0 - ratio) + end_color[1] * ratio)
            b = int(start_color[2] * (1.0 - ratio) + end_color[2] * ratio)

            # 현재 좌표에 색상 설정
            draw.point((x, y), fill=(r, g, b))

    return image

#ff8647
#96d35f

#hex색상값 rgd로 변환
start_color_input = input("Enter start color (hex): ")
start_color = (int(start_color_input[0:2], 16), int(start_color_input[2:4], 16), int(start_color_input[4:6], 16))

end_color_input = input("Enter end color (hex): ")
end_color = (int(end_color_input[0:2], 16), int(end_color_input[2:4], 16), int(end_color_input[4:6], 16))

original_image_path = "Gradation/cat.png"
print(original_image_path)
original_image = Image.open(original_image_path)
filtered_image = apply_gradation_filter(original_image, start_color,end_color,0.5,'circular')

filtered_image.save("Gradation/filtered_image.jpg")




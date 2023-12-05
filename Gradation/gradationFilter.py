from PIL import Image, ImageDraw, ImageFilter

def apply_gradation_filter(image):
    # 그라데이션 필터 적용
    width, height = image.size
    grad_image = Image.new('RGBA', (width, height))
    draw = ImageDraw.Draw(grad_image)
    
    # 그라데이션의 시작과 끝 색상
    start_color = (255, 0, 0, 0)  # 빨간색, 투명도 0
    end_color = (0, 0, 255, 255)  # 파란색, 투명도 255
    
    for y in range(height):
        # 각 픽셀의 그라데이션 색상 계산
        r = int((start_color[0] * (height - y) + end_color[0] * y) / height)
        g = int((start_color[1] * (height - y) + end_color[1] * y) / height)
        b = int((start_color[2] * (height - y) + end_color[2] * y) / height)
        a = int((start_color[3] * (height - y) + end_color[3] * y) / height)
        
        # 수평으로 그라데이션을 그림
        draw.line([(0, y), (width, y)], fill=(r, g, b, a))
    
    # 원본 이미지와 그라데이션 이미지를 합침
    blended_image = Image.blend(image.convert('RGBA'), grad_image, alpha=0.5)
    blended_image = blended_image.convert('RGB')
    return blended_image

original_image_path = "./Gradation/test.jpg"
original_image = Image.open(original_image_path)
filtered_image = apply_gradation_filter(original_image)

# filtered_image.show()
filtered_image.save("./Gradation/filtered_image.jpg")

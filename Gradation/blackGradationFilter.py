from PIL import Image, ImageDraw

def apply_gradation_filter(image, start, end, input_alpha=0.5):
    # 이미지의 검정색 부분을 투명하게 만들기
    alpha_mask = image.convert("L").point(lambda x: 0 if x == 0 else 255)
    image.putalpha(alpha_mask)

    # 그라데이션 이미지 생성
    width, height = image.size
    grad_image = visual_gradation(width, height, start, end)

    # 그라데이션 이미지를 배경으로 하여 합성
    result_image = Image.alpha_composite(Image.new("RGBA", image.size, (0, 0, 0, 0)), grad_image)
    result_image.paste(image, (0, 0), image)

    return result_image

def visual_gradation(width, height, start, end):
    # 새로운 이미지 생성
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # 그라데이션 값 적용
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            alpha = int((1.0 - x / width) * 255)
            color = start + (alpha,)
            image.putpixel((x, y), color)

    return image

# hex 색상값을 RGB로 변환하는 함수
def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


try:
    # 시작 색상과 끝 색상을 지정
    start_color_input = input("Enter start color (hex): ")
    start_color = hex_to_rgb(start_color_input)

    end_color_input = input("Enter end color (hex): ")
    end_color = hex_to_rgb(end_color_input)

    # 이미지 경로 (본인의 이미지 경로를 추가해주세요)
    image_path = "Gradation/KakaoTalk_Photo_2023-12-09-19-19-51.png"

    # 이미지 열기
    original_image = Image.open(image_path)

    # 색칠 함수 적용
    filtered_image = apply_gradation_filter(original_image, start_color, end_color)

    # 결과 이미지 보여주기
    filtered_image.show()
except IOError:
    print("Error:png 파일이 아닙니다.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
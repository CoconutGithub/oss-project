from PIL import Image, ImageDraw
import math

def apply_gradation_filter(image,start,end,shape='row'):
        """
        이미지에 그라데이션을 적용하는 메서드입니다.

        매개변수:
        - image: 입력된 이미지.
        
        반환:
        - 그라데이션이 적용된 이미지.
        """
        """
        Apply the gradation filter to the input image.

        Parameters:
        - image: The input image.

        return: 
        The filtered image.
        """
        # 그라데이션 필터 적용
        width, height = image.size

        if shape == 'row' or shape == 'col':
            grad_image = visual_gradation(width, height,start,end,shape)
        elif shape == 'circular':
            grad_image = circular_gradation(width, height,start,end)
        else:
            raise ValueError("Invalid shape. Use 'row', 'col', or 'circular'.")

        # 원본 이미지와 그라데이션 이미지를 합침
        blended_image = Image.blend(image.convert('RGB'), grad_image, 0.5)
        blended_image = blended_image.convert('RGB')

        return blended_image

def visual_gradation(width, height,start,end,shape):
        """
        가로 또는 세로 그라데이션이미지를 생성합니다.

        매개변수:
        - width: 이미지의 가로값.
        - height: 이미지의 세로값
        반환:
        - 생성된 그라데이션 이미지
        """
        
        """
        Generate a visual gradation.

        Parameters:
        - width: The width of the image.
        - height: The height of the image.

        return: 
        The generated gradation image.
        """
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

def circular_gradation(width, height,start,end):
        """
        원형 그라데이션이미지를 생성합니다.

        매개변수:
        - width: 이미지의 가로값.
        - height: 이미지의 세로값.

        반환: 
        - 생성된 원형그라데이션 이미지.
        """

        """
        Generate a circular gradation.

        Parameter:
        - width: The width of the image.
        - height: The height of the image.
        
        return: 
        - The generated circular gradation image.
        """
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
                r = int(start[0] * (1.0 - ratio) + end[0] * ratio)
                g = int(start[1] * (1.0 - ratio) + end[1] * ratio)
                b = int(start[2] * (1.0 - ratio) + end[2] * ratio)

                # 현재 좌표에 색상 설정
                draw.point((x, y), fill=(r, g, b))

        return image
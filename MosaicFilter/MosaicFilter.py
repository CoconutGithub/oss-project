from PIL import Image
import os

def apply_mosaic_filter(image, block_size=10):
    """
    주어진 이미지에 모자이크 기능을 적용
    
    매개변수 : 
    - image(PIL.Image.Image) : 입력된 이미지값
    - block_size (int): 모자이크 블록의 크기
    
    반환 :
    - 모자이크 된 이미지
    """
    
    width, height = image.size

    # 입력 이미지와 동일한 모드와 동일한 크기의 새 이미지 생성
    mosaic_image = Image.new(image.mode, image.size)

    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            
            # 원본 이미지에서 블록 잘라내기
            box = (x, y, x + block_size, y + block_size)
            block = image.crop(box)
            
            # 블록의 평균 색상을 계산
            average_color = (
                sum(p[0] for p in block.getdata()) // block_size**2,
                sum(p[1] for p in block.getdata()) // block_size**2,
                sum(p[2] for p in block.getdata()) // block_size**2
            )

            # 평균 색상으로 새 이미지를 생성하여 필터링된 이미지에 붙여넣기
            mosaic_block = Image.new(image.mode, block.size, average_color)
            mosaic_image.paste(mosaic_block, box)

    # 모자이크 처리된 이미지를 반환
    return mosaic_image

def main():
    # 현재 스크립트 파일의 디렉토리
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 입력 이미지 경로
    input_image_path = os.path.join(script_dir, "test.jpg")

    # 모자이크 필터를 적용할 블록 크기
    ## block_size가 클수록 흐림
    block_size = 20
    
    # 입력 이미지 열기
    ## RGB 모드로 변환
    try:
        input_image = Image.open(input_image_path).convert("RGB")  
    except FileNotFoundError:
        print(f"Error: Input image not found at {input_image_path}")
        return

    # 모자이크 필터 적용
    mosaic_image = apply_mosaic_filter(input_image, block_size=block_size)

    # 필터링된 이미지 보기
    mosaic_image.show()

    # 저장할 이미지의 파일 경로
    output_image_path = os.path.join(script_dir, "mosaic_image.jpg")

    # 필터링된 이미지 저장
    mosaic_image.save(output_image_path)

if __name__ == "__main__":
    main()
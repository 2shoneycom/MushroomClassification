import os
from PIL import Image

# 기준 디렉토리 설정
base_dir = "/Users/lsh/Downloads/trainset(300x300)"

# 디렉토리 목록을 알파벳 순으로 정렬
subdirs = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])

# 저장할 이미지 리스트들을 위한 빈 딕셔너리 초기화
train_images = {}

# 각 디렉토리 순회
for idx, subdir in enumerate(subdirs, start=0):
    # 각 디렉토리 내 이미지 파일 목록을 정렬하여 가져옴
    image_files = sorted([f for f in os.listdir(os.path.join(base_dir, subdir)) if f.lower().endswith(('.jpg', '.jpeg'))])
    # 각 디렉토리에 해당하는 이미지 리스트 초기화
    train_images[f'train_images_{idx}'] = []

    # 각 이미지 파일을 열고 리스트에 추가
    for image_file in image_files:
        image_path = os.path.join(base_dir, subdir, image_file)
        image = Image.open(image_path)
        train_images[f'train_images_{idx}'].append(image)

# 결과 확인 (예시: train_images_1의 첫 번째 이미지 출력)
#train_images['train_images_1'][0].show()  # train_images_1 리스트의 첫 이미지 출력

for i in train_images:
    print(len)
#하위 디렉터리 검색하기.
import os

# def search(dirname):
#     try:
#         filenames = os.listdir(dirname) # os.listdir => 해당 디렉터리 안의 파일 이름을 리스트로 저장
#         for filename in filenames:
#             full_filename = os.path.join(dirname, filename) #os.path.join => 디렉토리와 파일명을 이어주는 함수
#             if os.path.isdir(full_filename): # isdir => 이 파일이 디렉터리 형식인지? 참이면 재귀 호출
#                 search(full_filename)
#             else:
#                 ext = os.path.splitext(full_filename)[-1] # os.path.splitext => 파일명을 확장자를 기준으로 두 부분으로 나누어준다.
#                 if ext == '.py':
#                     print(full_filename)
#     except PermissionError:
#         pass

# search("C:/Users/admin/Desktop/방구석코딩")

# os.walk 를 사용한 더 간편한 검색.
for (path, dir, files) in os.walk("C:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print(f'{path}/{filename}')
            
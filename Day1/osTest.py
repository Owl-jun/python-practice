import os

os.chdir('C:/Users/admin/Desktop/방구석코딩')

result = os.popen("dir")

print(result.read())
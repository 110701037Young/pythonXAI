import base64

# 讀取圖片檔案
with open("image/apple.png", "rb") as image_file:
    # 編碼成 base64
    base64_str = base64.b64encode(image_file.read()).decode("utf-8")

print(base64_str)

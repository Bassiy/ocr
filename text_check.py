from PIL import Image
import pytesseract

# 画像ファイルのパス
image_path = '/home/bassiy/onedrive-nkz/ドキュメント/challenge/program/Work/software_dev/weather_site4/screenshot/screenshot_愛知県.png'

# 画像を開く
image = Image.open(image_path)

# 画像からテキストを抽出
text = pytesseract.image_to_string(image, lang='jpn')  # 日本語の場合は 'jpn'

# 抽出したテキストを表示
print(text)

# テキストを単語ごとに分割
words = text.split()

print(words)

# "ー週間の天気"がリストに含まれているか確認
if any("ー週間の天気" in item for item in words):
    print("あり")
else:
    print("なし")
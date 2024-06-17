import os
from PIL import Image
import pytesseract

# Tesseract-OCRの実行ファイルのパスを設定（必要に応じて変更してください）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 画像ファイルが保存されているディレクトリのパス
image_directory = 'screenshot'

# 画像ディレクトリ内のファイル名を取得
image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

# 「一週間の天気」という文字が含まれていない画像のファイル名を出力
for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    text = pytesseract.image_to_string(Image.open(image_path), lang='jpn')
    if "一週間の天気" not in text:
        print(image_file)

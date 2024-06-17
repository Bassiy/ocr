from PIL import Image
import pytesseract
import os


# スクリーンショットフォルダのパス
screenshot_folder = 'screenshot'

# すべての画像ファイルをループ
for filename in os.listdir(screenshot_folder):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        image_path = os.path.join(screenshot_folder, filename)
        
        # 画像を開く
        image = Image.open(image_path)
        
        # 画像からテキストを抽出
        text = pytesseract.image_to_string(image, lang='jpn')  # 日本語の場合は 'jpn'

        # テキストを単語ごとに分割
        words = text.split()

        # "ー週間の天気"がリストに含まれているか確認
        if any("ー週間の天気" in item for item in words):
            print("ok")
        else:
            print(f"文字が含まれていない画像: {filename}")

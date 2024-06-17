from jinja2 import Template
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Jsonファイルからエリアコードを探し出す関数
def find_area_code(area_name):
    area = requests.get('https://www.jma.go.jp/bosai/common/const/area.json')
    data = area.json()
    for key, value in data['offices'].items():
        if value['name'] == area_name:
            return key
    return "情報を取得できませんでした"

# 天気予報のデータを取得する関数
def get_weather_data(area_code):
    try:
        jma_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
        jma_json = requests.get(jma_url).json()
        weather_codes = jma_json[1]["timeSeries"][0]["areas"][0]["weatherCodes"]
        return weather_codes, None
    except Exception as e:
        return [], "情報を取得できませんでした。"

# 選択肢のリストを返す関数
def get_options():
    return [
        '入力してください', '北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県',
        '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県',
        '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県',
        '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県',
        '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県',
        '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県',
        '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄'
    ]

# 日付リストを返す関数
def get_date_list():
    return [
        "今日", "明日", "明後日", "３日後", "４日後", "５日後", "6日後"
    ]

@app.route("/", methods=["GET", "POST"])
def index():
    options = get_options()
    area_name = request.form.get('options') if request.method == 'POST' else "愛知県"
    area_code = find_area_code(area_name)
    weather_codes, error_message = get_weather_data(area_code) if "エリアコードが発見できませんでした" not in area_code else ([], "エリアコードが発見できませんでした")
    date = get_date_list()

    return render_template(
        "index.html",
        area_name=area_name,
        options=options,
        weatherCodes=weather_codes,
        date=date,
        error_message=error_message
    )

if __name__ == "__main__":
    app.run()

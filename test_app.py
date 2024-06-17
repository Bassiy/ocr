import pytest
from unittest.mock import patch, Mock
from app import find_area_code, get_weather_data

# 正常系テスト
@patch('app.requests.get')
def test_find_area_code_normal(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        'offices': {
            '000000': {'name': '愛知県'},
            '000001': {'name': '東京都'}
        }
    }
    mock_get.return_value = mock_response
    assert find_area_code('愛知県') == '000000'
    assert find_area_code('東京都') == '000001'

# 異常系テスト
@patch('app.requests.get')
def test_find_area_code_abnormal(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        'offices': {
            '000000': {'name': '愛知県'},
            '000001': {'name': '東京都'}
        }
    }
    mock_get.return_value = mock_response
    assert find_area_code('存在しない県') == '情報を取得できませんでした'

# 正常系テスト
@patch('app.requests.get')
def test_get_weather_data_normal(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = [
        {},
        {
            'timeSeries': [
                {
                    'areas': [
                        {'weatherCodes': ['100', '101', '102']}
                    ]
                }
            ]
        }
    ]
    mock_get.return_value = mock_response
    weather_codes, error_message = get_weather_data('000000')
    assert weather_codes == ['100', '101', '102']
    assert error_message is None

# 異常系テスト
@patch('app.requests.get')
def test_get_weather_data_abnormal(mock_get):
    mock_get.side_effect = Exception('API呼び出しに失敗しました')
    weather_codes, error_message = get_weather_data('000000')
    assert weather_codes == []
    assert error_message == '情報を取得できませんでした。'

if __name__ == "__main__":
    pytest.main()

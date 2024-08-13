import json
from unittest.mock import Mock, patch

from pandas import DataFrame

from src.service import simple_find


@patch("pandas.read_excel")
def test_simple_find(mock_read: Mock) -> None:
    data = DataFrame(
        [
            {
                "Дата операции": "02.06.2024 20:34:17",
                "Дата платежа": "02.06.2024",
                "Номер карты": "*4983",
                "Статус": "OK",
                "Сумма операции": -69.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -69.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Супермаркеты",
                "MCC": 5499,
                "Описание": "Славица",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 69.0,
            },
            {
                "Дата операции": "02.06.2024 15:01:00",
                "Дата платежа": "02.06.2024",
                "Номер карты": "*4983",
                "Статус": "OK",
                "Сумма операции": -365.97,
                "Валюта операции": "RUB",
                "Сумма платежа": -365.97,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Супермаркеты",
                "MCC": 5411,
                "Описание": "Перекрёсток",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 365.97,
            },
        ]
    )

    mock_read.return_value = data
    assert simple_find("Перекрёсток") == json.dumps(
        [
            {
                "Дата операции": "02.06.2024 15:01:00",
                "Дата платежа": "02.06.2024",
                "Номер карты": "*4983",
                "Статус": "OK",
                "Сумма операции": -365.97,
                "Валюта операции": "RUB",
                "Сумма платежа": -365.97,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Супермаркеты",
                "MCC": 5411,
                "Описание": "Перекрёсток",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 365.97,
            }
        ],
        ensure_ascii=False,
    )

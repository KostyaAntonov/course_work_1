import pytest
from pandas import DataFrame

from src.time import find_range_time, find_range_time_df, find_time_of_day, range_time


@pytest.mark.parametrize(
    "correct, date",
    (
        ["Доброе утро", "2018-01-10 8:8:8"],
        ["Добрый день", "2018-01-10 13:13:13"],
        ["Добрый вечер", "2018-01-10 18:18:18"],
        ["Доброй ночи", "2018-01-10 2:2:2"],
    ),
)
def test_find_time_of_day(correct: str, date: str) -> None:
    assert find_time_of_day(date) == correct


def test_range_time() -> None:
    assert range_time("2018-01-10 8:8:8") == [
        "01 10 2018",
        "01 09 2018",
        "01 08 2018",
        "01 07 2018",
        "01 06 2018",
        "01 05 2018",
        "01 04 2018",
        "01 03 2018",
        "01 02 2018",
        "01 01 2018",
    ]


def test_range_time2() -> None:
    assert range_time("2018-02-10 8:8:8", 2) == [
        "02 10 2018",
        "02 09 2018",
        "02 08 2018",
        "02 07 2018",
        "02 06 2018",
        "02 05 2018",
        "02 04 2018",
        "02 03 2018",
        "02 02 2018",
        "02 01 2018",
        "01 31 2018",
        "01 30 2018",
        "01 29 2018",
        "01 28 2018",
        "01 27 2018",
        "01 26 2018",
        "01 25 2018",
        "01 24 2018",
        "01 23 2018",
        "01 22 2018",
        "01 21 2018",
        "01 20 2018",
        "01 19 2018",
        "01 18 2018",
        "01 17 2018",
        "01 16 2018",
        "01 15 2018",
        "01 14 2018",
        "01 13 2018",
        "01 12 2018",
        "01 11 2018",
        "01 10 2018",
        "01 09 2018",
        "01 08 2018",
        "01 07 2018",
        "01 06 2018",
        "01 05 2018",
        "01 04 2018",
        "01 03 2018",
        "01 02 2018",
        "01 01 2018",
    ]


def test_find_range_time() -> None:
    data = [
        {"Дата платежа": "11.01.2018"},
        {"Дата платежа": "12.01.2018"},
        {"Дата платежа": "10.01.2018"},
        {"Дата платежа": "9.01.2018"},
        {"Дата платежа": "8.01.2018"},
        {"Дата платежа": "7.01.2018"},
        {"Дата платежа": "6.01.2018"},
        {"Дата платежа": "5.01.2018"},
    ]
    list_time = [
        "01 10 2018",
        "01 09 2018",
        "01 08 2018",
        "01 07 2018",
        "01 06 2018",
        "01 05 2018",
        "01 04 2018",
        "01 03 2018",
        "01 02 2018",
        "01 01 2018",
    ]
    assert find_range_time(data, list_time) == [
        {"Дата платежа": "10.01.2018"},
        {"Дата платежа": "9.01.2018"},
        {"Дата платежа": "8.01.2018"},
        {"Дата платежа": "7.01.2018"},
        {"Дата платежа": "6.01.2018"},
        {"Дата платежа": "5.01.2018"},
    ]


def test_find_range_time_df() -> None:
    data = DataFrame(
        [
            {
                "Дата операции": "08.01.2018 13:38:08",
                "Дата платежа": "10.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -1004.9,
                "Валюта операции": "RUB",
                "Сумма платежа": -1004.9,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Различные товары",
                "MCC": 5311,
                "Описание": "Torgovyy Dom Mayak",
                "Бонусы (включая кэшбэк)": 20,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 1004.9,
            },
            {
                "Дата операции": "05.01.2018 15:28:22",
                "Дата платежа": "07.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -79.6,
                "Валюта операции": "RUB",
                "Сумма платежа": -79.6,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Супермаркеты",
                "MCC": 5411,
                "Описание": "Пятёрочка",
                "Бонусы (включая кэшбэк)": 1,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 79.6,
            },
            {
                "Дата операции": "05.01.2018 14:58:38",
                "Дата платежа": "07.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -120.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -120.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Цветы",
                "MCC": 5992,
                "Описание": "Magazin  Prestizh",
                "Бонусы (включая кэшбэк)": 2,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 120.0,
            },
            {
                "Дата операции": "04.01.2018 15:00:41",
                "Дата платежа": "05.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -1025.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -1025.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Топливо",
                "MCC": 5541,
                "Описание": "Pskov AZS 12 K2",
                "Бонусы (включая кэшбэк)": 20,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 1025.0,
            },
            {
                "Дата операции": "04.01.2018 14:05:08",
                "Дата платежа": "06.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -1065.9,
                "Валюта операции": "RUB",
                "Сумма платежа": -1065.9,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Супермаркеты",
                "MCC": 5411,
                "Описание": "Пятёрочка",
                "Бонусы (включая кэшбэк)": 21,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 1065.9,
            },
            {
                "Дата операции": "03.01.2018 15:03:35",
                "Дата платежа": "04.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -73.06,
                "Валюта операции": "RUB",
                "Сумма платежа": -73.06,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Супермаркеты",
                "MCC": 5499,
                "Описание": "Magazin 25",
                "Бонусы (включая кэшбэк)": 1,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 73.06,
            },
            {
                "Дата операции": "03.01.2018 14:55:21",
                "Дата платежа": "05.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -21.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -21.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Красота",
                "MCC": 5977,
                "Описание": "OOO Balid",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 21.0,
            },
            {
                "Дата операции": "01.01.2018 20:27:51",
                "Дата платежа": "04.01.2018",
                "Номер карты": "*7197",
                "Статус": "OK",
                "Сумма операции": -316.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -316.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Красота",
                "MCC": 5977,
                "Описание": "OOO Balid",
                "Бонусы (включая кэшбэк)": 6,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 316.0,
            },
            {
                "Дата операции": "01.01.2018 12:49:53",
                "Дата платежа": "01.01.2018",
                "Номер карты": "",
                "Статус": "OK",
                "Сумма операции": -3000.0,
                "Валюта операции": "RUB",
                "Сумма платежа": -3000.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": "",
                "Категория": "Переводы",
                "MCC": "",
                "Описание": "Линзомат ТЦ Юность",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 3000.0,
            },
        ]
    )
    assert find_range_time_df(data, range_time("2018-04-10 8:8:8")).to_dict("records") == [
        {
            "MCC": 5541,
            "Бонусы (включая кэшбэк)": 20,
            "Валюта операции": "RUB",
            "Валюта платежа": "RUB",
            "Дата операции": "04.01.2018 15:00:41",
            "Дата платежа": "05.01.2018",
            "Категория": "Топливо",
            "Кэшбэк": "",
            "Номер карты": "*7197",
            "Округление на инвесткопилку": 0,
            "Описание": "Pskov AZS 12 K2",
            "Статус": "OK",
            "Сумма операции": -1025.0,
            "Сумма операции с округлением": 1025.0,
            "Сумма платежа": -1025.0,
        },
        {
            "MCC": 5411,
            "Бонусы (включая кэшбэк)": 21,
            "Валюта операции": "RUB",
            "Валюта платежа": "RUB",
            "Дата операции": "04.01.2018 14:05:08",
            "Дата платежа": "06.01.2018",
            "Категория": "Супермаркеты",
            "Кэшбэк": "",
            "Номер карты": "*7197",
            "Округление на инвесткопилку": 0,
            "Описание": "Пятёрочка",
            "Статус": "OK",
            "Сумма операции": -1065.9,
            "Сумма операции с округлением": 1065.9,
            "Сумма платежа": -1065.9,
        },
    ]

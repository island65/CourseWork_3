from scr.funcs import open_file, format_date, sort_date, hide_accounts_data, bill_output


def test_open_file():
    assert isinstance(open_file(), list)


def test_sort_date():
    assert sort_date([
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
  },
  {
        "id": 939719570,
        "state": "canceled",
        "date": "2018-06-30T02:08:58.425572"
  }
]) == [
    {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
      }]


def test_format_date():
    assert format_date([{"date":"2019-08-26T10:50:58.294041"}]) == [{"date":"26.08.2019"}]


def test_hide_accounts_data():
    assert hide_accounts_data([{"to":"Счет 64686473678894779589", "from":"Maestro 1596837868705199"}]) == [{'to': 'Счет **9589', 'from': 'Maestro 1596 78** **** 5199'}]


def test_bill_output():
    assert bill_output([{'id': 863064926, 'state': 'EXECUTED', 'date': '08.12.2019', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет **5907', 'from': ''}]) == ['08.12.2019 Открытие вклада\n -> Счет **5907\n41096.24 USD\n']


from reports import AverageGDPReport

def test_average_gdp():
    """Проверка расчета среднего значения и сортировки по убыванию."""
    report = AverageGDPReport()
    data = [
        {'country': 'Russia', 'gdp': '2000'},
        {'country': 'Russia', 'gdp': '3000'},
        {'country': 'USA', 'gdp': '5000'}
    ]

    result = report.generate(data)

    # Ожидаемые результаты
    assert result[0] == ['USA', 5000.0]
    assert result[1] == ['Russia', 2500.0]

def test_empty_data():
    """Проверка, что скрипт не крашится при отсутствии данных"""
    report = AverageGDPReport()
    assert report.generate([]) == []
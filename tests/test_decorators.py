import pytest

from src.decorators import log


def test_log_success_console(capsys):
    """Логирование успеха в консоль"""

    @log()
    def add(a, b):
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_success_file(tmp_path):
    """Логирование успеха в файл"""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    multiply(4, 5)
    content = log_file.read_text().strip()
    assert content == "multiply ok"


def test_log_error_console(capsys):
    """Логирование ошибки в консоль"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out


def test_log_error_file(tmp_path):
    """Логирование ошибки в файл"""
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    content = log_file.read_text().strip()
    assert "divide error: ZeroDivisionError. Inputs: (10, 0), {}" in content

from enum import Enum

import typer

from .timer import app as timer

app = typer.Typer(name="progress", help="Работа с прогрессом обучения")


FormatEnum = Enum('FormatEnum', " ".join(["json", "markdown"]))


@app.command()
def export(
        _format: FormatEnum = typer.Option(None, "-f", "--format")
):
    """Экспорт прогресса в какой-то формат"""


@app.command()
def finish():
    """Завершить материал"""


@app.command(name="next")
def _next():
    """Получить следующий урок по плану"""


@app.command()
def current():
    """Получить текущие материалы в изучении"""


app.add_typer(timer)

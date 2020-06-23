import typer

from .timer import app as timer

app = typer.Typer(name="progress", help="Работа с прогрессом обучения")


@app.command()
def export():
    """Экспорт прогресса в какой-то формат"""
    pass


@app.command()
def finish():
    """
    Завершить материал
    """
    pass


@app.command(name="next")
def _next():
    """
    Получить следующий урок по плану
    """
    pass


app.add_typer(timer)

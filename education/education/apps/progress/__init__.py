import typer

from .exporter import app as exporter
from .timer import app as timer

app = typer.Typer(name="progress", help="Работа с прогрессом обучения")


@app.command()
def finish():
    """
    Завершить материал
    """
    pass


@app.command()
def next():
    """
    Получить следующий урок по плану
    """
    pass


app.add_typer(exporter)
app.add_typer(timer)

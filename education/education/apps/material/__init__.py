import typer

from .exporter import app as exporter
from .importer import app as importer
from .note import app as note


app = typer.Typer(name="material", help="Работа с материалами")


@app.command()
def add():
    """
    Добавить материал в базе
    """
    pass


@app.command()
def select():
    """
    Выборка по материалам
    """
    pass


@app.command()
def remove():
    """
    Удалить материал по ID
    """
    pass


app.add_typer(importer)
app.add_typer(exporter)
app.add_typer(note)

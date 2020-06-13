import typer

from .bot import app as bot

app = typer.Typer(
    name="quiz",
    help="Работа с задачами"
)


@app.command()
def add():
    """
    Добавить quiz
    """
    pass


@app.command()
def list():
    """
    Список текущих quiz
    """
    pass


@app.command()
def log():
    """
    Лог по прохождению
    """
    pass


app.add_typer(bot)

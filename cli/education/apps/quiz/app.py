import typer

app = typer.Typer(name="quiz", help="Работа с задачами")


@app.command()
def add():
    """Добавить quiz"""


@app.command()
def list():
    """Список текущих quiz"""


@app.command()
def log(
    watch: bool = typer.Option(False, "-w")
):
    """Лог по прохождению"""

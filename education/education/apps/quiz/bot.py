import typer


app = typer.Typer(
    name="bot",
    help="Управление telegram ботом"
)


@app.command()
def start():
    """
    Запустить бот
    """
    pass


@app.command()
def log():
    """
    Логи бота
    """
    pass

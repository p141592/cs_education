import typer


from .server import main as server

app = typer.Typer(name="bot", help="Управление telegram ботом")


@app.command()
def start():
    """
    Запустить бот
    """
    typer.echo("Запуск бота")
    server()


@app.command()
def log():
    """
    Логи бота
    """
    pass

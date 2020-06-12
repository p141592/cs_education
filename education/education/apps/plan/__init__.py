import typer

app = typer.Typer(
    name="plan",
    help="Работа с планом обучения"
)


@app.command()
def roadmap():
    """
    Генерация roadmap
    """
    pass


@app.command()
def stat():
    pass

import typer

app = typer.Typer(
    name="plan",
    help="Работа с планом обучения"
)


@app.command()
def append_point():
    pass

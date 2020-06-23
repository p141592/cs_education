import typer


app = typer.Typer(name="timer", help="Таймер потраченного времени")


@app.command()
def start():
    pass


@app.command()
def stop():
    pass

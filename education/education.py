import typer

app = typer.Typer()


@app.command()
def main(name: str, name2: str = ""):
    """
    test description
    """
    typer.echo(f"Hello {name}")


if __name__ == "__main__":
    app()

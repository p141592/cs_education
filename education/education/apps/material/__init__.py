import typer

from apps.material.exporter import app as exporter
from apps.material.importer import app as importer


app = typer.Typer(
    name="material",
    help="Работа с материалами"
)


@app.command()
def index(
    content_type: str = typer.Option(None, "--content-type", "-c"),
    material_type: str = typer.Option(None, "--material-type", "-m"),
    section: str = typer.Option(None, "--section", "-s"),
    format: str = typer.Option("markdown", "--format", "-f", show_default=True)
):
    """
    Генерация индекса материалов
    """
    pass


app.add_typer(importer)
app.add_typer(exporter)

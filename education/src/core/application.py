import typer

from src.apps.education import app as education
from src.apps.material import app as material
from src.apps.plan import app as plan

__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        typer.echo(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


app = typer.Typer(
    version: bool = typer.Option(None, "--version", callback=version_callback),
)
app.add_typer(education)
app.add_typer(material)
app.add_typer(plan)

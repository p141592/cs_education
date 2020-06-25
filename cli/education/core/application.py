import sqlite3

import typer
import logging

from apps.material import app as material
from apps.progress import app as progress
from apps.quiz import app as quiz
from apps.schedule import app as schedule
from apps.bot import app as bot

__version__ = "0.1.0"

from core.db import DB_PATH

NAME = "cs_education"


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

app = typer.Typer(name=NAME, help="Инструменты для работы с обучением")

app.add_typer(material)
app.add_typer(progress)
app.add_typer(quiz)
app.add_typer(schedule)
app.add_typer(bot)


@app.callback(invoke_without_command=True)
def main(version: bool = typer.Option(None, "--version", "-v"),):
    if version:
        typer.echo(f"{NAME} version: {__version__}")
        raise typer.Exit()


@app.command()
def merge(
        source_db: typer.FileBinaryRead = typer.Argument(...)
):
    """Слияние баз обучения\n
    source_db: Путь до базы sqlite, которая зальется в текущую
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        with conn:
            conn.execute(f"""
            attach '{source_db}' as toMerge;           
            BEGIN; 
            insert into AuditRecords select * from toMerge.AuditRecords; 
            COMMIT; 
            detach toMerge;
            """)
    finally:
        conn.close()

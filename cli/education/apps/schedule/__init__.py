import typer

app = typer.Typer(name="schedule", help="Работа с расписанием")


@app.command()
def sync():
    """Синхронизировать расписание с расписанием в календаре"""


@app.command()
def view():
    """Посмотреть текущее расписание"""


@app.command()
def add():
    """Добавить занятие"""

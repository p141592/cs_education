import typer

app = typer.Typer(name="schedule", help="Работа с расписанием")

@app.command()
def get():
    """Получить календарь для заполнения"""

@app.command()
def sync():
    """Синхронизировать расписание с расписанием в календаре"""

@app.command()
def slots():
    """Посмотреть текущие слоты"""

import orjson
import typer
import models
from core import session_scope

app = typer.Typer(
    name="materials",
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


@app.command()
def add():
    """
    Добавить материал в базе
    """
    pass


@app.command()
def select():
    """
    Выборка по материалам
    """
    pass


@app.command()
def remove():
    """
    Удалить материал по ID
    """
    pass


@app.command(
    name="import"
)
def _import(
    data: typer.FileText = typer.Argument(...)
):
    """
    Импорт материалов в базу

    Структура:
    {"table":
        {"column": value, "index": None}
    }\n
    index None == Создание новой записи / не None == замена текущей
    """
    _source = orjson.loads(data.read())

    data_candidates = []
    for table, raws in _source.items():
        _model = getattr(models, table)
        assert _model.Serializer, f"Объект {table} не содержит сериализатор"
        for _r in raws:
            _data = _model.Serializer.parse_obj(_r)
            data_candidates.append(_model(**_data.dict()))

    with session_scope() as session:
        session.add_all(data_candidates)


@app.command(
    name="export"
)
def _export(
        format: str = typer.Option('--format', '-f')
):
    """Экспорт материалов"""

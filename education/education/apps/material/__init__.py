import orjson
import typer
import models

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


@app.command(
    name="import"
)
def _import(
    data: typer.FileText = typer.Option(...)
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
    for table, raws in _source.items():
        _model = getattr(models, table)
        assert _model.Serializer, f"Объект {table} не содержит сериализатор"
        for _r in raws:
            _data = _model.Serializer.parse_obj(_r)
            pass
    pass


def _export(
    name="export"
):
    """Экспорт материалов"""

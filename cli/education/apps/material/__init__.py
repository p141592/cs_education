import orjson
import typer
import models
from core.db import session_scope, BaseDBModel

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
    data: typer.FileText = typer.Argument(...),
    overwrite: bool = typer.Option(False, help="Перезаписать объекты, если есть такой PK"),
    tables: models.TABLES_ENUM = typer.Option(None, help="Список таблиц в которые сделать записи", case_sensitive=False)
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
    _t = models.TABLES
    data_candidates = []
    for table, raws in _source.items():
        if tables and table not in tables:
            # Пропустить таблицу, если список таблиц регулируется аргументами и этой таблицы там нет
            continue

        assert table.lower() in models.TABLES, f"Таблица {table} не объявлена в моделях"
        _model = getattr(models, table)
        assert _model.model, f"Объект {table} не содержит сериализатор"

        for _r in raws:
            # Добавить проверку существования ID в базе
            # -> Если такой элемент уже есть, делать обновление
            _data = _model.model().parse_obj(_r)
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


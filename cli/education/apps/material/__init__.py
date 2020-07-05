from pathlib import Path
from typing import List

import click
import orjson
import typer
import models
from core.db import session_scope
from settings import BASE_DIR

app = typer.Typer(name="materials", help="Работа с материалами")


@app.command()
def index(
    content_type: str = typer.Option(None, "--content-type", "-c"),
    material_type: str = typer.Option(None, "--material-type", "-m"),
    section: str = typer.Option(None, "--section", "-s"),
    format: str = typer.Option("markdown", "--format", "-f", show_default=True),
):
    """Генерация индекса материалов"""


@app.command()
def add(
        table: models.TABLES_ENUM = typer.Option(
            ..., "--table", "-t", help="Таблица в которую добавить запись", case_sensitive=False
        ),
        body: str = typer.Argument(None),
        repeat: bool = typer.Option(True, "")
):
    """Добавить материал в базу"""
    with session_scope() as session:
        # Получаем таблицу
        _table = getattr(models, table)
        # Если есть аргументы в словаре -- завершение
        if body:
            data = _table.model()(body)  # Выкинет исключение, а нам это и хорошо
            session.add(_table(**data.dict()))
        else:
            while True:
                # Если нет -- получаем все поля модели, просим пользователя ввести их по очереди -- завершение
                # Завершение: валидируем аргументы, сохраняем записть, возвращаем данные как они в базе
                if not repeat or not click.confirm('Добавить еще?'):
                    break


@app.command()
def select():
    """Выборка по материалам"""


@app.command()
def remove(
        id: int = typer.Argument(...),
        table: models.TABLES_ENUM = typer.Option(
            ..., "--table", "-t", help="Таблица в которой удалить записи", case_sensitive=False
        )
):
    """Удалить материал по ID"""
    with session_scope() as session:
        _object = getattr(models, table)
        session.delete(_object.query.filter_by(id=id))


@app.command(name="import")
def _import(
        data: typer.FileText = typer.Argument(...),
        overwrite: bool = typer.Option(False, "--overwrite", "-w", help="Перезаписать объекты, если есть такой PK"),
        tables: List[models.TABLES_ENUM] = typer.Option(None, "--tables", "-t", help="Список таблиц в которые сделать записи",
                                                  case_sensitive=False)
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

    with session_scope() as session:
        for table, raws in _source.items():
            if tables and table not in tables:
                # Пропустить таблицу, если список таблиц регулируется аргументами и этой таблицы там нет
                continue

            _object = getattr(models, table)
            assert _object, f"Таблицы {table} не существует"

            for _r in raws:
                _id = _r.pop("id", None)
                # Добавить проверку существования ID в базе
                # -> Если такой элемент уже есть, делать обновление
                _data = _object.model(exclude=['id']).parse_obj(_r)
                one = session.query(_object).filter_by(id=_id).one_or_none()

                if one:
                    if not overwrite:
                        print(f"Объект {table}{_r} не записан")
                        continue
                    session.query(_object).filter(_object.id == _id) \
                        .update(_data.dict())
                    session.query(_object).filter(_object.id == _id).update(_data.dict())
                else:
                    session.add(_object(**_data.dict()))


@app.command(
    name="export"
)
def _export(
        format: str = typer.Option('json', '--format', '-f'),
        tables: models.TABLES_ENUM = typer.Option(
            None, "--tables", "-t", help="Список таблиц в которые сделать записи", case_sensitive=False
        ),
        path: Path = typer.Option(Path(BASE_DIR)),
        filename: str = typer.Option("cs_education_dump")
):
    """Экспорт материалов"""
    # Получить список всех таблиц
    #

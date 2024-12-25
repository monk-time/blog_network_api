import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

PROJECT_DIR_NAME = 'app'
MANAGE_PATH = BASE_DIR / PROJECT_DIR_NAME

if not MANAGE_PATH.exists() or not MANAGE_PATH.is_dir():
    pytest.fail(
        f'В директории `{BASE_DIR}` не найдена папка c проектом '
        f'`{PROJECT_DIR_NAME}`. Убедитесь, что у вас верная структура проекта.'
    )

FILENAME = 'manage.py'

if not (MANAGE_PATH / FILENAME).is_file():
    pytest.fail(
        f'В директории `{MANAGE_PATH}` не найден файл `{FILENAME}`. '
        'Убедитесь, что у вас верная структура проекта.'
    )

pytest_plugins = [
    'tests.fixtures.fixture_user',
    'tests.fixtures.fixture_data',
]

# test .md
default_md = '# api_final\napi final\n'
filename = 'README.md'
assert (BASE_DIR / filename).is_file(), (
    f'В корне проекта не найден файл `{filename}.`'
)

file = Path(filename).read_text(encoding='utf-8', errors='ignore')
assert file != default_md, f'Не забудьте оформить `{filename}.`'

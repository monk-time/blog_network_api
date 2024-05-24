import os
import sys
from pathlib import Path

import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

root_dir_content = os.listdir(BASE_DIR)
PROJECT_DIR_NAME = 'app'

if (
    PROJECT_DIR_NAME not in root_dir_content
    or not (BASE_DIR / PROJECT_DIR_NAME).is_dir()
):
    pytest.fail(
        f'В директории `{BASE_DIR}` не найдена папка c проектом '
        f'`{PROJECT_DIR_NAME}`. Убедитесь, что у вас верная структура проекта.'
    )

MANAGE_PATH = BASE_DIR / PROJECT_DIR_NAME
project_dir_content = os.listdir(MANAGE_PATH)
FILENAME = 'manage.py'

if FILENAME not in project_dir_content:
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
assert (
    filename in root_dir_content
), f'В корне проекта не найден файл `{filename}.`'

file = Path(filename).read_text(encoding='utf-8', errors='ignore')
assert file != default_md, f'Не забудьте оформить `{filename}.`'

# SPDX-FileCopyrightText: 2022 XMPP Providers Team
#
# SPDX-License-Identifier: AGPL-3.0-or-later

'''
Download / prepare / process xmpp providers data
'''
from datetime import date
from pathlib import Path
import os
import shutil
import sys
import zipfile

import requests

DOWNLOAD_PATH = Path('downloads')
DATA_PATH = Path('data')
STATIC_PATH = Path('static')
BADGES_PATH = STATIC_PATH / 'badge'
PROVIDERS_JSON_PATH = DATA_PATH / 'results'
PROVIDERS_PAGES_PATH = Path('content/provider')

PROVIDERS_DATA_URL = 'https://invent.kde.org/melvo/xmpp-providers/' \
    '-/jobs/artifacts/master/download/?job=filtered-provider-lists'
BADGES_DATA_URL = 'https://invent.kde.org/melvo/xmpp-providers/' \
    '-/jobs/artifacts/master/download/?job=badges'
CLIENTS_DATA_URL = 'https://invent.kde.org/melvo/xmpp-providers/' \
    '-/raw/master/clients.json'

MD_FRONTMATTER = '''---\ntitle: %s\ndate: %s\n---\n
{{< provider-details provider="%s">}}
'''


def status_ok(status_code: int) -> bool:
    '''
    Check if HTTP status code is ok (i.e. in 200/300 region)
    '''
    return 200 >= status_code < 400


def initialize_directory(path: Path) -> None:
    '''
    Remove path (if it exists) and containing files, then recreate path
    '''
    if path.exists() and path.is_dir():
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)


def prepare_data_files() -> None:
    '''
    Download and prepare provider data files
    '''
    initialize_directory(DOWNLOAD_PATH)

    # Temporarily move 'logo' folder and recommended_clients.json
    # in order to clean up directories
    shutil.copytree(STATIC_PATH / 'logo', DOWNLOAD_PATH  / 'logo')
    shutil.copyfile(DATA_PATH / 'recommended_clients.json',
                    DOWNLOAD_PATH / 'recommended_clients.json')
    initialize_directory(STATIC_PATH)
    initialize_directory(DATA_PATH)

    get_providers_data()
    get_badges()
    get_clients_data()

    shutil.copytree(DOWNLOAD_PATH / 'logo', STATIC_PATH  / 'logo')
    shutil.copyfile(DOWNLOAD_PATH / 'recommended_clients.json',
                    DATA_PATH / 'recommended_clients.json')

def get_providers_data() -> None:
    '''
    Download, extract, and move providers data
    '''
    providers_request = requests.get(PROVIDERS_DATA_URL)
    if not status_ok(providers_request.status_code):
        sys.exit(f'Error while trying to download from {PROVIDERS_DATA_URL}')

    with open(DOWNLOAD_PATH / 'providers_data.zip',
              'wb') as providers_data_zip:
        providers_data_zip.write(providers_request.content)

    with zipfile.ZipFile(DOWNLOAD_PATH / 'providers_data.zip',
                        'r') as zip_file:
        zip_file.extractall(DOWNLOAD_PATH / 'providers_data')

    shutil.copyfile(DOWNLOAD_PATH / 'providers_data' / 'providers-D.json',
                    DATA_PATH / 'providers.json')
    shutil.copytree(DOWNLOAD_PATH / 'providers_data' / 'results',
                    DATA_PATH / 'results')


def get_badges() -> None:
    '''
    Download, extract, and move badges
    '''
    badge_request = requests.get(BADGES_DATA_URL)
    if not status_ok(badge_request.status_code):
        sys.exit(f'Error while trying to download from {BADGES_DATA_URL}')

    with open(DOWNLOAD_PATH / 'badges_data.zip',
              'wb') as badge_data_zip:
        badge_data_zip.write(badge_request.content)

    with zipfile.ZipFile(DOWNLOAD_PATH / 'badges_data.zip', 'r') as zip_file:
        zip_file.extractall(DOWNLOAD_PATH / 'badges_data')

    shutil.copytree(DOWNLOAD_PATH / 'badges_data' / 'badges',
                    BADGES_PATH,
                    dirs_exist_ok=True)


def get_clients_data() -> None:
    '''
    Download, extract, and move clients data
    '''
    clients_request = requests.get(CLIENTS_DATA_URL)
    if not status_ok(clients_request.status_code):
        sys.exit(f'Error while trying to download from {CLIENTS_DATA_URL}')

    os.mkdir(DOWNLOAD_PATH / 'clients_data')
    with open(DOWNLOAD_PATH / 'clients_data' / 'clients.json',
              'wb') as clients_data_zip:
        clients_data_zip.write(clients_request.content)

    shutil.copyfile(DOWNLOAD_PATH / 'clients_data' / 'clients.json',
                    DATA_PATH / 'clients.json')


def create_provider_pages() -> None:
    '''
    Create a .md page per provider
    '''
    initialize_directory(PROVIDERS_PAGES_PATH)

    today = date.today()
    date_formatted = today.strftime('%Y-%m-%d')

    (_, _, filenames) = next(os.walk(PROVIDERS_JSON_PATH))
    for filename in filenames:
        filename = filename[:-5]
        with open(PROVIDERS_PAGES_PATH / f'{filename}.md',
                  'w',
                  encoding='utf8') as md_file:
            md_file.write(
                MD_FRONTMATTER % (filename, date_formatted, filename))


if __name__ == '__main__':
    prepare_data_files()
    create_provider_pages()

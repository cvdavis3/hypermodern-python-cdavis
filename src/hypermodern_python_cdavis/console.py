# src/hypermodern_python_cdavis/console.py
import textwrap

import click
import requests
import locale

from . import __version__

# API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
API_URL_0 = "https://"
API_URL_1 = ".wikipedia.org/api/rest_v1/page/random/summary"
# API_URL = "http://abcdefghblahblah.com/test.mp4"

@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    usr_locale = locale.getlocale()
    language = usr_locale[0][0:2]
    API_URL = API_URL_0 + language + API_URL_1
    try:
        with requests.get(API_URL, stream=True) as response:
            try:
                response.raise_for_status()
                data = response.json()

                title = data["title"]
                extract = data["extract"]

                click.secho(title, fg="green")
                click.echo(textwrap.fill(extract))
            except requests.exceptions.HTTPError:
                click.echo('API unreachable')
    except requests.exceptions.ConnectionError:
        click.echo('API unreachable')
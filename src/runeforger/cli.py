"""Console script for runeforger."""

import typer
from rich.console import Console

from runeforger import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for runeforger."""
    console.print("Replace this message by putting your code into "
               "runeforger.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()

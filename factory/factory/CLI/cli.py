import typer
from ..models import mathModels
app = typer.Typer()


@app.command()
def subtracter(x: int, y: int):
    """
    used to subtract two numbers
    """
    subtracter = mathModels.Factory.create_executor("subtract")
    result = subtracter.run(x, y)
    typer.echo(result)


@app.command()
def adder(x: int, y: int):
    """
    used to add two numbers together
    """
    subtracter = mathModels.Factory.create_executor("add")
    result = subtracter.run(x, y)
    typer.echo(result)


def main():
    app()

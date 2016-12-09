import click
from .base import sorobase

@click.command()
@click.option('--high', default=10, help='Highest possible number')
@click.option('--nb', default=10, help='Number of operations to perform')
@click.option('--op', default='+', help='List of possible operations to use. To combine operations, use "+-/*"')
@click.option('--pause', default=10, help='Pause between each operation')
@click.option('--inter', default=True, help='Display intermediate results', type=bool)
@click.option('--inf', default=False, help='Infinite number of operations. Use <enter> to continue.', type=bool)
def cli(high, nb, op, pause, inter, inf):
    """The most basic program for soroban training."""
    s = sorobase(nb_high=high, nb_size=nb, operation=op)
    s.run(pause=pause, inter=inter, inf=inf)

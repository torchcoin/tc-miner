import click
import emoji
import numpy as np
import time

@click.command()
@click.option('--wallet_address', prompt='Wallet address')
@click.option('--pool_address', prompt='Pool address')
def cli(wallet_address, pool_address):
    """TorchCoin mining software.
    """

    click.echo("Mining block %s..." % 'a1jh233r9sfn29wdk92sasd0vd')
    click.echo("Using metric %s..." % 'Accuracy')
    time.sleep(1)

    click.echo("... Accuracy: %s/0.85" % '0.79')
    time.sleep(1)

    click.echo("... Accuracy: %s/0.85" % '0.795')
    time.sleep(1)

    click.echo("... Accuracy: %s/0.85" % '0.796')
    time.sleep(1)

    click.echo("... Accuracy: %s/0.85" % '0.796')
    time.sleep(1)

    click.echo(emoji.emojize(
        ":droplet: block solved by another party.",
        use_aliases=True))
    time.sleep(1)

    click.echo("Mining block %s..." % 'a1jh233r9sfn29wdk92sasd0vd')
    click.echo("Using metric %s..." % 'F1-Score')
    time.sleep(1)

    click.echo("... F1-Score: %s/0.42" % '0.38')
    time.sleep(1)

    click.echo("... F1-Score: %s/0.42" % '0.381')
    time.sleep(1)

    click.echo("... F1-Score: %s/0.42" % '0.386')
    time.sleep(1)

    click.echo("... F1-Score: %s/0.42" % '0.4001')
    time.sleep(1)

    click.echo("... F1-Score: %s/0.42" % '0.411')
    time.sleep(1)

    click.echo("... F1-Score: %s/0.42" % '0.423')
    time.sleep(1)

    click.echo(emoji.emojize(
        ":fire: block solved.",
        use_aliases=True))
    click.echo(emoji.emojize(
        ":fire: +0.002 TCH -> %s" % wallet_address,
        use_aliases=True))
    time.sleep(1)

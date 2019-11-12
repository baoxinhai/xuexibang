# -*- coding:utf-8 -*-
__author__ = 'Jinyang Shao'

import click

from xuexibang import app


@app.cli.command()
def fortest():
    click.echo("command line message")


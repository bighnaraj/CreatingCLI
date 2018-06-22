import click 

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('please enter a subcommand')
    else:
        click.echo('invoking subcommand %s' % ctx.invoked_subcommand)

@cli.command()
@click.argument('filename')
def gen_sources(filename):
    click.echo('The subcommand gen_sources reads %s' %filename)

@cli.command()
def gen_nodes():
    click.echo('The subcommand gen_nodes')

@cli.command()
def convert():
    click.echo('The subcommand convert')


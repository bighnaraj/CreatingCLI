import click 
import yaml

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
    with open("filename") as f:
        yaml_data = yaml.load(f)
    with open("source.list","w") as f:
        for item in yaml_data['BOOTSTRAP']['repos']:
            input = item['type']+" "+item['uri']+" "+item['suite']+" "+item['section']
            f.write(input+"\n")


@cli.command()
def gen_nodes():
    click.echo('The subcommand gen_nodes')

@cli.command()
def convert():
    click.echo('The subcommand convert')


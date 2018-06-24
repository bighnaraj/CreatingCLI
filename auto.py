###########

import click 
import pandas
import yaml

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('please enter a subcommand')
    else:
        click.echo('invoking subcommand %s' % ctx.invoked_subcommand)

@cli.command()
@click.argument('pluginsfile')
def gen_sources(pluginsfile):
    click.echo('The subcommand gen_sources reads %s' %pluginsfile)
    with open(pluginsfile) as f:
        yaml_data = yaml.load(f)
    with open("source.list","w") as f:
        for item in yaml_data['BOOTSTRAP']['repos']:
            input = item['type']+" "+item['uri']+" "+item['suite']+" "+item['section']
            f.write(input+"\n")


@cli.command()
@click.argument('rackfile')
def gen_nodes(rackfile):
    click.echo('The subcommand gen_nodes reads %s' %rackfile)
    racks_data = pandas.read_csv(rackfile)

@cli.command()
def convert():
    click.echo('The subcommand convert')


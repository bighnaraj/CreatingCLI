#This file is for CLI "auto" which accepts two subcommands "gen_sources" and "gen_nodes"

import click 
import pandas
import yaml
from click.testing import CliRunner

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
    try:
        if ".yaml" in filename:
            with open(pluginsfile) as f:
                yaml_data = yaml.load(f)
                with open("source.list","w") as f:
                for item in yaml_data['BOOTSTRAP']['repos']:
                    write_data = item['type']+" "+item['uri']+" "+item['suite']+" "+item['section']
                    f.write(write_data+"\n")

        else:
            click.echo("\'%s\' is not a valid yaml file" %filename)
    except FileNotFoundError as e:
        click.echo("Wrong File Name Entered. File \'%s\' does not exist" %filename)   


@cli.command()
@click.argument('rackfile')
def gen_nodes(rackfile):
    click.echo('The subcommand gen_nodes reads %s' %rackfile)
    racks_data = pandas.read_csv(rackfile)
    
    with open("sample.yaml","w") as outfile:
        list_dictionary = []
        for i in range(len(racks_data)):
            dictionary_yaml = dict(racks_data.ix[i])
            temp = {}
            temp['rack_name'] = dictionary_yaml['name']
            temp['mc_name'] = 'm'+ str(i)
            temp['network'] = {'pxe':str.strip(dictionary_yaml[' pxe']),'public':str.strip(dictionary_yaml[' public']),
                               'storage':str.strip(dictionary_yaml[' storage']),'mgmt':str.strip(dictionary_yaml[' mgmt'])}
            list_dictionary.append(temp.copy())

    updated_dictionary['machines'] = list_dictionary
    yaml.dump(updated_dictionary,outfile,default_flow_style=False)


@cli.command()
def convert():
    click.echo('The subcommand convert')



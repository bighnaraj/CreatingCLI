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
    try:
        if ".yaml" in pluginsfile:
            click.echo("The subcommand gen_sources reads '%s'" %pluginsfile)
            with open(pluginsfile) as f:
                yaml_data = yaml.load(f)
                with open("source.list","w") as f:
                    for item in yaml_data['BOOTSTRAP']['repos']:
                        write_data = item['type']+" "+item['uri']+" "+item['suite']+" "+item['section']
                        f.write(write_data+"\n")

        else:
            click.echo("'%s' is not a valid yaml file" %pluginsfile)
    except FileNotFoundError as e:
        click.echo("Wrong File Name Entered. File '%s' does not exist" %pluginsfile)   

@cli.command()
@click.argument('rackfile')
def gen_nodes(rackfile):
    try:
        if ".csv" in rackfile:
            click.echo("The subcommand gen_nodes reads '%s'" %rackfile)
            racks_data = pandas.read_csv(rackfile)
            with open("machines.yaml","w") as outfile:
                list_dictionary = []
                for i in range(len(racks_data)):
                    dictionary_yaml = dict(racks_data.ix[i])
                    internal_dictionary['rack_name'] = dictionary_yaml['name']
                    internal_dictionary['mc_name'] = 'm'+ str(i+1)
        #internal_dictionary['network'] = {'pxe':str.strip(dictionary_yaml[' pxe']),'public':str.strip(dictionary_yaml[' public']),
        #                   'storage':str.strip(dictionary_yaml[' storage']),'mgmt':str.strip(dictionary_yaml[' mgmt'])}

                    pxe_address = subnet_addressing(str.strip(dictionary_yaml[' pxe']))
                    pxe_value = {'start':pxe_address[2]}
                    pxe_value['end'] = pxe_address[3]
                    pxe_value['gateway'] = pxe_address[4]

                    public_address = subnet_addressing(str.strip(dictionary_yaml[' public']))
                    public_value = {'start':public_address[2]}
                    public_value['end'] = public_address[3]
                    public_value['gateway'] = public_address[4]

                    storage_address = subnet_addressing(str.strip(dictionary_yaml[' storage']))
                    storage_value = {'start':storage_address[2]}
                    storage_value['end'] = storage_address[3]
                    storage_value['gateway'] = storage_address[4]

                    mgmt_address = subnet_addressing(str.strip(dictionary_yaml[' mgmt']))
                    mgmt_value = {'start':mgmt_address[2]}
                    mgmt_value['end'] = mgmt_address[3]
                    mgmt_value['gateway'] = mgmt_address[4]

                    list_network = {}
                    list_network['pxe'] = pxe_value
                    list_network['public'] = public_value
                    list_network['storage'] = storage_value
                    list_network['mgmt'] = mgmt_value
                    internal_dictionary['network'] = list_network

                    list_dictionary.append(internal_dictionary.copy())

                updated_dictionary['machines'] = list_dictionary
                yaml.dump(updated_dictionary,outfile,default_flow_style=False)
        else:
            click.echo("'%s' is not a valid csv file" %rackfile)
    except FileNotFoundError as e:
        click.echo("Wrong File Name Entered. File '%s' does not exist" %rackfile)

@cli.command()
def convert():
    click.echo('The subcommand convert')

def subnet_addressing(address):
    # Get address string and CIDR string from command line
    (addrString, cidrString) = address.split('/')

    # Split address into octets and turn CIDR into int
    addr = addrString.split('.')
    cidr = int(cidrString)

    # Initialize the netmask and calculate based on CIDR mask
    mask = [0, 0, 0, 0]
    for i in range(cidr):
        mask[int(i/8)] = mask[int(i/8)] + (1 << (7 - i % 8))

    # Initialize net and binary and netmask with addr to get network
    net = []
    for i in range(4):
        net.append(int(addr[i]) & mask[i])

    # Duplicate net into broad array, gather host bits, and generate broadcast
    broad = list(net)
    brange = 32 - cidr
    for i in range(brange):
        broad[3 - int(i/8)] = broad[3 - int(i/8)] + (1 << (i % 8))

    # retrun information, mapping integer lists to strings for easy printing
    gatewaystr = ".".join(map(str, net))
    net[-1] = net[-1] + 1
    broad[-1] -= 1
    maskstr = ".".join(map(str,mask))
    netstr = ".".join(map(str, net))
    broadstr = ".".join(map(str, broad))
    return (addrString,maskstr,netstr,broadstr,gatewaystr)


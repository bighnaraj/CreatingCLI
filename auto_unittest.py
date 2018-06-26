import os
import unittest
import auto
from click.testing import CliRunner
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_gen_sources(self):
        runner = CliRunner()
        result_valid_yaml = runner.invoke(auto.gen_sources, ["plugins.yaml"])
        assert 'The subcommand gen_sources reads \'plugins.yaml\'' in result_valid_yaml.output
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        assert 'source.list' in files 

        result_invalid_yaml = runner.invoke(auto.gen_sources, ["aaaa"])
        assert '\'aaaa\' is not a valid yaml file' in result_invalid_yaml.output

        result_file_notexist = runner.invoke(auto.gen_sources, ["xyz.yaml"])
        assert 'Wrong File Name Entered. File \'xyz.yaml\' does not exist' in result_file_notexist.output
        
 
    def test_get_nodes(self):
        runner = CliRunner()
        result_valid_csv = runner.invoke(auto.gen_nodes, ["racks.csv"])
        assert 'The subcommand gen_nodes reads \'racks.csv\'' in result_valid_csv.output
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        assert 'machines.yaml' in files

        result_invalid_csv = runner.invoke(auto.gen_nodes, ["aaaa"])
        assert '\'aaaa\' is not a valid csv file' in result_invalid_csv.output

        result_file_notexist = runner.invoke(auto.gen_nodes, ["xyz.csv"])
        assert 'Wrong File Name Entered. File \'xyz.csv\' does not exist' in result_file_notexist.output

 
if __name__ == '__main__':
    unittest.main()

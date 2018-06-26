import os
import unittest
import auto
from click.testing import CliRunner
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_gen_sources(self):
        runner = CliRunner()
        result_valid = runner.invoke(auto.gen_sources, ["plugins.yaml"])
        assert 'The subcommand gen_sources reads plugins.yaml' in result_valid.output
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        assert 'source.list' in files
        

        result_invalid = runner.invoke(auto.gen_sources, ["aaaa"])
        assert 'aaaa is not a valid yaml file' in result_invalid.output
        
 
    def test_get_nodes(self):
        runner = CliRunner()
        result = runner.invoke(auto.gen_nodes, ["racks.csv"])
        assert 'The subcommand gen_nodes reads racks.csv' in result.output

 
if __name__ == '__main__':
    unittest.main()

import unittest
import auto
from click.testing import CliRunner
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_gen_sources(self):
        runner = CliRunner()
        result = runner.invoke(auto.gen_sources, ["plugins.yaml"])
        assert 'The subcommand gen_sources reads plugins.yaml' in result.output
        #assert 'invoking subcommand gen_sources' in result.output
        #assert 'invoking subcommand get_nodes' in result.output
 
    def test_get_nodes(self):
        runner = CliRunner()
        result = runner.invoke(auto.gen_nodes, ["racks.csv"])
        assert 'The subcommand gen_nodes reads racks.csv' in result.output

 
if __name__ == '__main__':
    unittest.main()

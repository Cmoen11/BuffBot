import unittest
from commandsRefactored import Commands


class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.commands = Commands()

    def test_bye(self):
        self.assertEqual(self.commands.bye("!bye", "85431603408420864"), "Bye bye!")

    #TODO: test all other commands when they've been refactored in commandsRefactored.

if __name__ == '__main__':
    unittest.main(exit=False)

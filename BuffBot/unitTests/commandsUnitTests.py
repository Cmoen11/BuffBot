import unittest
from BuffBot.unitTests.commandsRefactored import Commands
from BuffBot.commands import get_random_line

class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.commands = Commands()

    def test_bye(self):
        self.assertEqual(self.commands.bye("!bye", "85431603408420864"), "Bye bye!")

    def test_math(self):
        self.assertEqual(self.commands.math("!math", "85431603408420864", params=4 * 4), 16)

    #def test_eightBall(self):
     #   self.assertEqual(self.commands.eightBall("!8ball", "85431603408420864"), get_random_line("..8ballresponsen.txt"))
    #TODO: test all other commands when they've been refactored in commandsRefactored.

    def test_whoIsTheBuffest(self):
        self.assertEqual(self.commands.whoIsTheBuffest("!whoIsTheBuffest", "85431603408420864"), "Wiklem")


if __name__ == '__main__':
    unittest.main(exit=False)

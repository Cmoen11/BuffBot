import unittest
from BuffBot.unitTests.commandsRefactored import Commands


class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.commands = Commands()

    def test_bye(self):
        self.assertEqual(self.commands.bye("!bye", "85431603408420864"), "Bye bye!")

    def test_math(self):
        self.assertEqual(self.commands.math("!math", "85431603408420864", params=4 * 4), 16)

    #TODO: test all other commands when they've been refactored in commandsRefactored.

    def test_whoIsTheBuffest(self):
        self.assertEqual(self.commands.whoIsTheBuffest("!whoIsTheBuffest", "85431603408420864"), "Wiklem")

    def test_smugAdd(self):
        self.assertEqual(self.commands.smugAdd('https://static.pexels.com/photos/24353/pexels-photo.jpg'), )

if __name__ == '__main__':
    unittest.main(exit=False)

import unittest
from unitTests.commandsRefactored import Commands


class CommandsTest(unittest.TestCase):

    def setUp(self):
        self.commands = Commands()
        self.path = '../smug-anime-faces'

    def test_bye(self):
        self.assertEqual(self.commands.bye("!bye", "85431603408420864"), "Bye bye!")

    def test_math(self):
        self.assertEqual(self.commands.math("!math", "85431603408420864", params=4 * 4), 16)

    #TODO: test all other commands when they've been refactored in commandsRefactored.

    def test_whoIsTheBuffest(self):
        self.assertEqual(self.commands.whoIsTheBuffest("!whoIsTheBuffest", "85431603408420864"), "Wiklem")

    '''
    def test_eightBall(self):
        self.assertIn(self.commands.eightBall("!8ball", "85431603408420864"), self.commands.eightBallReader())

    
    def test_smug(self):
        self.assertIn(self.commands.smug("!smug", "85431603408420864"), self.commands.smugList())
    '''


if __name__ == '__main__':
    unittest.main(exit=False)

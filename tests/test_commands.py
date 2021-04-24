import re
import unittest
from cleo.testers.application_tester import ApplicationTester

from blackwatch.blackwatch import application


class TestCommands(unittest.TestCase):
    def test_application_accepts_watch_command(self):
        app = application

        tester = ApplicationTester(app)
        tester.execute("watch --help")

        self.assertTrue(re.search(r"<folder>\s+Which folder do you want to watch?", tester.io.fetch_output()))
        self.assertTrue(re.search(r"<command>\s+What command to run?", tester.io.fetch_output()))
        self.assertEqual(0, tester.status_code)

    # def test_watch_command_can_be_used(self):
    #     application = Application()
    #     application.add(WatchCommand())

    #     command = application.find('watch')
    #     command_tester = CommandTester(command)
    #     # This doesn't work, because watch command runs for eternity
    #     command_tester.execute("./ dir")

    #     print(command_tester.io.fetch_output())

    #     assert "..." == command_tester.io.fetch_output()


if __name__ == "__main__":
    unittest.main()

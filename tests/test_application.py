import re
import unittest
from cleo.testers.application_tester import ApplicationTester

from blackwatch.blackwatch import application


class TestApplication(unittest.TestCase):
    def test_application_accepts_command(self):
        app = application

        tester = ApplicationTester(app)
        tester.execute("")

        self.assertTrue(re.search("Console Tool", tester.io.fetch_output()))
        self.assertTrue(re.search("Display the manual of a command", tester.io.fetch_output()))
        self.assertEqual(0, tester.status_code)


if __name__ == "__main__":
    unittest.main()

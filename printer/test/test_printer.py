import unittest
from io import StringIO
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from printer import Printer

class TestPrinter(unittest.TestCase):

    def setUp(self):
        self.held_stdout = sys.stdout
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = self.held_stdout

    def test_print_good(self):
        Printer.standard("This is a good message.", style='bold')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[1m\033[32mSuccess: This is a good message.\033[0m", output)

    def test_print_bad(self):
        Printer.error("This is a bad message.", style='underline')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[4m\033[31mError: This is a bad message.\033[0m", output)

    def test_print_info(self):
        Printer.info("This is an informational message.", style='italic')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[3m\033[34mInfo: This is an informational message.\033[0m", output)

    def test_print_warn(self):
        Printer.warning("This is a warning message.", style='blink')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[5m\033[33mWarning: This is a warning message.\033[0m", output)

    def test_print_succ(self):
        Printer.success("This is a success message.", style='faint')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[2m\033[35mSuccess: This is a success message.\033[0m", output)

    def test_print_debug(self):
        Printer.debug("This is a debug message.", style='reversed')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[7m\033[36mDebug: This is a debug message.\033[0m", output)

    def test_print_cust(self):
        Printer.custom("This is a custom cyan message.", "cyan", style='bold', prefix="Custom:")
        output = self.held_output.getvalue().strip()
        print(repr(output))
        self.assertIn("\033[1m\033[36mCustom: This is a custom cyan message.\033[0m", output)

    def test_custom_separator(self):
        Printer.standard("This-is-a-message", style='bold')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[1m\033[32mSuccess: This-is-a-message\033[0m", output)

    def test_custom_end(self):
        Printer.standard("This is a message", style='bold', end='***')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[1m\033[32mSuccess: This is a message\033[0m***", output)

    def test_style_bold(self):
        Printer.standard("This is a bold message.", style='bold')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[1m\033[32mSuccess: This is a bold message.\033[0m", output)

    def test_style_faint(self):
        Printer.standard("This is a faint message.", style='faint')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[2m\033[32mSuccess: This is a faint message.\033[0m", output)

    def test_style_italic(self):
        Printer.standard("This is an italic message.", style='italic')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[3m\033[32mSuccess: This is an italic message.\033[0m", output)

    def test_style_underline(self):
        Printer.standard("This is an underlined message.", style='underline')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[4m\033[32mSuccess: This is an underlined message.\033[0m", output)

    def test_style_blink(self):
        Printer.standard("This is a blinking message.", style='blink')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[5m\033[32mSuccess: This is a blinking message.\033[0m", output)

    def test_style_reversed(self):
        Printer.standard("This is a reversed message.", style='reversed')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[7m\033[32mSuccess: This is a reversed message.\033[0m", output)

    def test_style_hidden(self):
        Printer.standard("This is a hidden message.", style='hidden')
        output = self.held_output.getvalue().strip()
        self.assertIn("\033[8m\033[32mSuccess: This is a hidden message.\033[0m", output)

    def test_invalid_style(self):
        Printer.standard("This is a message with invalid style.", style='invalid')
        output = self.held_output.getvalue().strip()
        self.assertIn("Invalid style: invalid. Must be one of", output)

    def test_invalid_separator(self):
        Printer.standard("This is a message with invalid separator.", sep=1)
        output = self.held_output.getvalue().strip()
        self.assertIn("Separator must be a string.", output)

    def test_invalid_end(self):
        Printer.standard("This is a message with invalid end.", end=1)
        output = self.held_output.getvalue().strip()
        self.assertIn("End character must be a string.", output)

    def test_invalid_file(self):
        Printer.standard("This is a message with invalid file.", file=1)
        output = self.held_output.getvalue().strip()
        self.assertIn("File must be an object with a write method.", output)

    def test_simple_print(self):
        print("Hello, world!")
        output = self.held_output.getvalue().strip()
        print(repr(output))  # Esto debe mostrar 'Hello, world!'
        self.assertEqual(output, "Hello, world!")

if __name__ == '__main__':
    unittest.main()

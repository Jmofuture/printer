<<<<<<< HEAD
# Printer Package

The `Printer` package provides a simple way to print messages with ANSI colors and styles in Python.

## Installation

You can install the package using pip:

```bash
pip install printer



## Available Colors
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white

## Available Styles
- bold
- faint
- italic
- underline
- blink
- reversed
- hidden

#Usage

from printer import Printer as p



# Print a standard message
p.standard("This is a standard message", style="bold")

# Print an error message
p.error("This is an error message", style="underline")

# Print an info message
p.info("This is an info message", style="italic")

# Print a warning message
p.warning("This is a warning message", style="blink")

# Print a success message
p.success("This is a success message", style="reversed")

# Print a debug message
p.debug("This is a debug message", style="hidden")

# Print a custom message
p.custom("This is a custom message", color="cyan", style="bold", prefix="Custom:")
=======
# print_color

`print_color` is a Python package that allows you to print colored messages using ANSI codes. It also allows you to apply styles such as bold, italic, and underline.

## Installation

You can install this package using pip:

```bash
pip install print_color
>>>>>>> ee5a89a92b84791d0a4ad441f8ba4845d8d16503

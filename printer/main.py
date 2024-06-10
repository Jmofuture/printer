class Printer:

    COLORS = {
        'reset': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    
    STYLES = {
        'bold': '\033[1m',
        'underline': '\033[4m',
        'reversed': '\033[7m'
    }
    
    @staticmethod
    def printer_good(message: str, bold: bool = False):
        style = Printer.STYLES['bold'] if bold else ''
        print(f"{style}{Printer.COLORS['green']}{message}{Printer.COLORS['reset']}")
    
    @staticmethod
    def printer_bad(message: str, bold: bool = False):
        style = Printer.STYLES['bold'] if bold else ''
        print(f"{style}{Printer.COLORS['red']}{message}{Printer.COLORS['reset']}")
    
    @staticmethod
    def printer_info(message: str, bold: bool = False):
        style = Printer.STYLES['bold'] if bold else ''
        print(f"{style}{Printer.COLORS['blue']}{message}{Printer.COLORS['reset']}")
    
    @staticmethod
    def printer_warning(message: str, bold: bool = False):
        style = Printer.STYLES['bold'] if bold else ''
        print(f"{style}{Printer.COLORS['yellow']}{message}{Printer.COLORS['reset']}")
    
    @staticmethod
    def printer_success(message: str, bold: bool = False):
        style = Printer.STYLES['bold'] if bold else ''
        print(f"{style}{Printer.COLORS['magenta']}{message}{Printer.COLORS['reset']}")
    
    @staticmethod
    def printer_debug(message: str, bold: bool = False):
        style = Printer.STYLES['bold'] if bold else ''
        print(f"{style}{Printer.COLORS['cyan']}{message}{Printer.COLORS['reset']}")
    
    @staticmethod
    def printer_custom(message: str, color: str, bold: bool = False):
        style = Printer.STYLES['bold'] if bold else ''
        if color in Printer.COLORS:
            print(f"{style}{Printer.COLORS[color]}{message}{Printer.COLORS['reset']}")
        else:
            print(f"{style}{Printer.COLORS['white']}{message}{Printer.COLORS['reset']}")

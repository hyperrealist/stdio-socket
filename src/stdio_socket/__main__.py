import os
import sys

import typer

from .console import console_entrypoint
from .expose import expose
from .psuedo_tty import pptty_entrypoint


def _ensure_unbuffered_script():
    if sys.stdout.line_buffering:
        os.execv(sys.executable, [sys.executable, "-u"] + sys.argv)


def main():
    """
    Main entry point for this module - expose.
    """
    if not __name__ == "__main__":
        _ensure_unbuffered_script()
    typer.run(expose)


def console():
    """
    Entrypoint for the console feature
    """
    _ensure_unbuffered_script()
    typer.run(console_entrypoint)


def pptty():
    """
    Entrypoint for the console feature
    """
    _ensure_unbuffered_script()
    typer.run(pptty_entrypoint)


if __name__ == "__main__":
    typer.run(expose)

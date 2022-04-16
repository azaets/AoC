import logging
import os
import sys

aoc_tools_logger = None


def init_submodules():
    """
    Initializes submodules.
    """
    from . import utils


def inti_logger():
    global aoc_tools_logger

    if aoc_tools_logger is None:
        aoc_tools_logger = logging.getLogger('AoC-Tools')
        aoc_tools_logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(levelname)-8s | %(message)s"))

        aoc_tools_logger.addHandler(console_handler)


inti_logger()
init_submodules()

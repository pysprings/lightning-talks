#!/usr/bin/env python3
import logging


def set_root_level(level):
    logging.getLogger().setLevel(level)


def init_logger():
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s {%(module)s:%(lineno)3s} %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S %Z",
        )
    )

    logging.basicConfig(level=logging.INFO, handlers=[handler])

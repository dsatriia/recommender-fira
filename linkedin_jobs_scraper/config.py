import os
import logging


class Config:
    os.environ["LI_AT_COOKIE"] = "AQEDAThq-1kDJE42AAABfpv7y1oAAAF-wAhPWlYAhLjMOcU82GYLk1P5ik_N9xeIg3RS5Q4Wfd3MBi5qU_JzlwUJRR9t0Gbo8nHPnxOnoAtFZiZa1t334OzXlNSHQK7Mw9IQQY-r86H9elucEZUsD0N0"
    LI_AT_COOKIE = os.environ['LI_AT_COOKIE'] if 'LI_AT_COOKIE' in os.environ else None
    print("debug baru")
    print(os.environ['LI_AT_COOKIE'])
    LOGGER_NAMESPACE = 'li:scraper'

    _level = logging.INFO

    if 'LOG_LEVEL' in os.environ:
        _level_env = os.environ['LOG_LEVEL'].upper().strip()

        if _level_env == 'DEBUG':
            _level = logging.DEBUG
        elif _level_env == 'INFO':
            _level = logging.INFO
        elif _level_env == 'WARN' or _level_env == 'WARNING':
            _level = logging.WARN
        elif _level_env == 'ERROR':
            _level = logging.ERROR
        elif _level_env == 'FATAL':
            _level = logging.FATAL

    LOGGER_LEVEL = _level

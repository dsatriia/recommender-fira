import os
import logging


class Config:
    os.environ["LI_AT_COOKIE"] = "AQEDAThq-1kB7t76AAABfklmtJ4AAAF-bXM4nlYAu_N5vZZJeYOH-QBSoFzAEIxXaFKCLS9FOHAG_07yzBKyD28nMhq8J0V49U4h5Aw_7w3FFAgDcOQDf4WhN02l8xG1_nktgMj28hHRGcQ9xpSscQed"
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

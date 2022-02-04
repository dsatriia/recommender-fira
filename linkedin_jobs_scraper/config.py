import os
import logging


class Config:
    os.environ["LI_AT_COOKIE"] = "AQEDATnUOO0Dc4zEAAABfsSWUIEAAAF-6KLUgU4AW5AIM3Sz6xWDl5-pPahj24qNQ_SLioHfQcFGkMWn6nAXc9Q13j1j4LuOnZAvyf3zas3tkwG3j66to5ofMC2HuAyDD-g5S26aaWEkB3kv7OHZMx1Q"
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

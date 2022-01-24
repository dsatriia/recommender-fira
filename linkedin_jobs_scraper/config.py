import os
import logging


class Config:
    os.environ["LI_AT_COOKIE"] = "AQEDAThq-1kESDDAAAABfozl8bMAAAF-sPJ1s1YAOf4rczGlmtbDoZsIM9-_JJe5fPQhPUa8aHKTDoh0b2Rw1gTKezLtrXkMwSPz807sDJAVpMhpwZwPdsUuxnXgUpe8OPEv4hteFYev_EAkwnem5_S8"
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

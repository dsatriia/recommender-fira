import os
import logging


class Config:
    os.environ["LI_AT_COOKIE"] = "AQEDAThq-1kDa2P8AAABfrCIzvQAAAF-1JVS9FYAJ8m3Phh3KqMqpYbYTBgnWuDAW6enR468NdfjTXhmNvcR8mI1E60ycOb0E6sOBMQi6QPa5qehMp6sL1AxmpcZVCxKvRuEHwgrHVx5Vv96AMB0YD1Y"
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

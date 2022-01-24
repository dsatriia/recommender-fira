import os
import logging


class Config:
    os.environ["LI_AT_COOKIE"] = "AQHw7IeH2qdFQQAAAXzpqfuaOh7AJL6e_n1tDAXPYtCMSn-LfxCS_4qgZUM8oUQV5qAxzUs_qOFsarPZAnB2ktWeAId6-Wxg9gTs3JVEqUeYI0W9QkUTAXOPNpXu_Z4uFD4tCWAu5FDTNnCwEOE1CXvOgM-WoXXOttp7uYbS7sOGRwK6eslnJvm5ddxKjm2qYoNBBvXJu_C-nhHcpMwPZTMWD_Rg0oM_sWejkYaKt95qju7_G3z2rtXEwPlcj4gNFjiuhqghJY86zdCRYwfLNy7hhJaYRyB7yOIld46WOTu-beQcX8JzSYgZa9gzNiZSRKIomByomvueKMMyfXA"
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

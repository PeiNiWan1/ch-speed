import logging
class Loggers:
    _logger = logging.getLogger('Server')
    def __init__(self, *args, **kwargs):
      pass

    @classmethod
    def info(cls, *args):
        """记录 INFO 级别的日志"""
        msg = ' '.join(map(str, args))  # 将所有参数转换为字符串并拼接
        cls._logger.info(msg)

    @classmethod
    def debug(cls, *args):
        """记录 DEBUG 级别的日志"""
        msg = ' '.join(map(str, args))  # 将所有参数转换为字符串并拼接
        cls._logger.debug(msg)

    @classmethod
    def warning(cls, *args):
        """记录 WARNING 级别的日志"""
        msg = ' '.join(map(str, args))  # 将所有参数转换为字符串并拼接
        cls._logger.warning(msg)

    @classmethod
    def error(cls, *args):
        """记录 ERROR 级别的日志"""
        msg = ' '.join(map(str, args))  # 将所有参数转换为字符串并拼接
        cls._logger.error(msg)

    @classmethod
    def critical(cls, *args):
        """记录 CRITICAL 级别的日志"""
        msg = ' '.join(map(str, args))  # 将所有参数转换为字符串并拼接
        cls._logger.critical(msg)

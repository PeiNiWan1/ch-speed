#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

     # 默认的环境配置
    environment = 'development'  # 默认为开发环境

    # 检查是否有额外的命令行参数传递环境
    if len(sys.argv) > 2 and sys.argv[2] in ['dev', 'prod']:
        environment = sys.argv[2]

    if environment == 'prod':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChSpeed.settings.prod')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChSpeed.settings.dev')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

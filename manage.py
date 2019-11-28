#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from os.path import join, dirname
import dotenv


def main():
    dotenv_path = join(dirname(__file__), f".env.{os.getenv('DJANGO_ENV') or 'development'}")
    dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), dotenv_path))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biotower.settings')
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

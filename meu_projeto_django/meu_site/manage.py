#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser  # Import the webbrowser module


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Check if the command is to run the server
    if 'runserver' in sys.argv:
        # Use webbrowser to open the URL when the server starts
        webbrowser.open('http://127.0.0.1:8000/usuarios/login/')

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

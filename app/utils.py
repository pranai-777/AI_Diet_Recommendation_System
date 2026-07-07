"""
=========================================
Utility Functions
AI Diet Recommendation System
=========================================
"""

import os


def check_file_exists(file_path):
    """
    Check whether a file exists.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"\n❌ File Not Found:\n{file_path}"
        )

    return True


def print_heading(title):
    """
    Print a nice heading.
    """

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def print_success(message):
    """
    Print success message.
    """

    print(f"✅ {message}")


def print_error(message):
    """
    Print error message.
    """

    print(f"❌ {message}")
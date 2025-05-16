import os
import sys
from pathlib import Path


def get_package_path():
    """Returns the path to the installed package."""
    return os.path.dirname(os.path.abspath(__file__))


def get_resource_path(relative_path):
    """
    Get the absolute path to a resource file, works both when running
    as a script and when installed as a package.

    Args:
        relative_path (str): The relative path to the resource from the src directory

    Returns:
        str: The absolute path to the resource
    """
    package_path = get_package_path()
    return os.path.join(package_path, relative_path)

# Example usage in your code:
# from src.resource_path import get_resource_path
# image_path = get_resource_path('img/chips.png')
# sprite = pygame.image.load(image_path)

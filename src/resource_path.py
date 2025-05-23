import os


def get_package_path():
    """
    Returns the path to the installed package. This is a utility function created because the pip installed game would
    not find the images and sounds by their relative path.
    """

    return os.path.dirname(os.path.abspath(__file__))


def get_resource_path(relative_path):
    """
    Get the absolute path to a resource file, works both when running
    as a script and when installed as a package. This is a utility function created because the pip installed game would
    not find the images and sounds by their relative path.

    Args:
        relative_path (str): The relative path to the resource from the src directory

    Returns:
        str: The absolute path to the resource
    """
    package_path = get_package_path()
    return os.path.join(package_path, relative_path)

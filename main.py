import importlib # This allows us to import a package programmatically
import inspect   # This allows introspection of the package
import os        # I use this for examining the file structure
from pprint import pprint


def main():
    plugin_root = "plugins"
    plugin_objects = {}
    # Get a list of files and folders in the directory you are searching
    for item in os.listdir(plugin_root):
        plugin_path = os.path.join(plugin_root, item)
        # Only check directories to see if they contain packages
        if os.path.isdir(plugin_path):
            plugin_name = item
            # In order to load the package, you have to know the name
            # of the main program. Python 2 packages had to include an
            # __init__.py module, so Holzhaus appears to have decided to
            # continue that requirement for all Jasper.ai plugins, providing
            # a standard entry point for all plugins.
            # Additionally, you also have to provide a package name. This name
            # really doesn't seem to matter in this implementation, although if
            # you examine the plugin classes below, you will see that the
            # name is used as a namespace, so it is probably a good idea to
            # keep them unique if possible so you don't end up overwriting
            # members of the package. Using the relative path name seems like
            # a good way to ensure uniqueness for this demo.
            if os.path.isfile(os.path.join(plugin_path, '__init__.py')):
                spec = importlib.util.spec_from_file_location(
                    'test mod',
                    os.path.join(plugin_path, '__init__.py')
                )
            # You can also use other filenames as long as you have
            # established them in advance.
            elif os.path.isfile(os.path.join(plugin_path, 'main.py')):
                spec = importlib.util.spec_from_file_location(
                    plugin_name,
                    os.path.join(plugin_path, 'main.py')
                )
            else:
                print("I can't find a main file in {plugin_path}")
                break
            mod = importlib.util.module_from_spec(spec)
            print(f"mod: {mod}")
            print(f"name: {spec.name}")
            # Load the package. This is equivalent to "import package"
            spec.loader.exec_module(mod)
            # Now use introspection to get a list of classes within the
            # package. There should only be one.
            plugin_classes = inspect.getmembers(
                mod,
                lambda cls: inspect.isclass(cls)
            )
            print(plugin_classes)
            # The result is a list of tuples where the first
            # element is the name of the class and the second
            # is a reference to the plugin itself.
            for plugin_class in plugin_classes:
                plugin_class_name = plugin_class[0]
                print(f"initializing {plugin_class_name}")
                plugin_objects[plugin_class_name] = plugin_class[1]()
            pprint(plugin_objects)


if __name__ == "__main__":
    main()

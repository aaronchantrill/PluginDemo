# PluginDemo

This is a brief demo in response to a question from @Winner about how [Naomi](https://projectnaomi.com)'s plugin system is implemented.

The plugin system is one of the main features that first attracted me to work with [Jasper.ai](jasperproject.github.io) which is the project Naomi is based on. I wanted a way to quickly experiment with mixing and matching speech to text, text to speech, etc. engines to discover which would work best. I have used the plugin system, but never really explored how it actually worked.

This repository provides a greatly stripped-down plugin system demonstrating how a plugin can be imported as a package from a file using the [importlib](https://docs.python.org/3/library/importlib.html)  library, then how classes can be identified in the package using the [inspect](https://docs.python.org/3/library/inspect.html)  library, and finally how the results can be used to instantiate these classes into objects. One aspect that I did not demo here is using the [configparser](https://docs.python.org/3/library/configparser.html)  library to parse a config file for information about the plugin, which is where Naomi gets the plugin name to pass to the importlib.util.spec_from_file_location() function. Instead, I just used the name of the directory the package inhabits.

Naomi uses these plugins in two ways. There are plugins like **stt**, **tts**, and **tti** where Naomi uses only a single plugin, which is instantiated as a specific variable. There are also cases where multiple plugins of the same type are instantiated, such as **speechhandler** and **notificationclient** plugins. These are usually placed in a list which can be iterated through, executing standard methods on each.

I hope this is helpful. I learned quite a bit while preparing this.
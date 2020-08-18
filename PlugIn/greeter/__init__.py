# greeter/__init__.py

#import plugins
from greeter.plugins import Plugins as plugins

greetings = plugins.names_factory(__package__)
greet = plugins.call_factory(__package__)
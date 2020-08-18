# greeter/yo.py
#import plugins
from greeter.plugins import Plugins as plugins

@plugins.register
def greet(name):
    print(f"Yo {name}, good times!")

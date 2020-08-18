# greeter/howdy.py
#import plugins
from greeter.plugins import Plugins as plugins

@plugins.register
def greet(name):
    print(f"Howdy good {name}, honored to meet you!")

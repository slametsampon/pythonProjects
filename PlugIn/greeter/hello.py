# greeter/hello.py
#import plugins
from greeter.plugins import Plugins as plugins

@plugins.register
def greet(name):
    print(f"Hello {name}, how are you today?")

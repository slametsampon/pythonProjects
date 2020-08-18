import greeter
import random

print(greeter.greetings())
print(greeter.greet(plugin="howdy", name="Guido"))

greeting = random.choice(greeter.greetings())
print(greeter.greet(greeting, name="Frida"))



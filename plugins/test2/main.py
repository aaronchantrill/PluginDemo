# This demonstrates that multiple classes can be loaded from a single
# module.
class TestPlugin2:
    def __init__(self):
        print("Test Plugin 2 initialized")

class TestClass3:
    def __init__(self):
        print("Test Class 3 from package test2 initialized")

class ExampleClass:
    def method1(self):
        print("Method 1")
        self.method2()

    def method2(self):
        print("Method 2")
        self.method3()

    def method3(self):
        print("Method 3")
        # Perform some operations
        self.method4()

# Create an instance of the class
example = ExampleClass()
example.method1()
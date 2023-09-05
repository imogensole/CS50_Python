# Create your own module of functions

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye {name}")

# ensures that main won't run when we are importing the function
if __name__ == "__main__":
    main()
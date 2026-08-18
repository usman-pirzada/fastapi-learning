# TODO: didnot understood:
#   - What happened by `another_log`
#   - why hash_fence() do its working (unlike fence()) when wrapper fn is commented without even calling `hash_log()`

def fence(fn):
    def wrapper_fn():
        print("*" * 10)
        fn()
        print("*" * 10)
    
    return wrapper_fn

def custom_fence(fence: str = "+"):
    def fence2(fn):
        def wrapper_fn(text: str):
            print(fence * 10)
            fn(text)
            print(fence * 10)
        
        return wrapper_fn
    
    return fence2

def hash_fence(fn):
    # def wrapper_fn():
        print("*" * 10)
        fn()
        print("*" * 10)
    
    # return wrapper_fn

@fence
def log():
    print("Decorated!")

@hash_fence
def hash_log():
    print("Hash Log!")


another_log = fence(log)
another_log()

print()

log()

print()

# @fence2("-")    # This will give error if we dont make another wrapper function for fence2
@custom_fence("#")
def log2(text: str):
    print(text)


log2("Student")


# Function Hinting
from typing import Callable, Any

# def decorator( fn: Callable[[int, int], float] ):
def decorator( fn: Callable[[Any], None] ):
    pass

# --------------------------------

routes: dict[str, Callable[[Any], Any]] = {}

def route(path: str):
    def register_route(fn):
        routes[path] = fn
        return fn
    
    return register_route

@route("/shipment")
def get_shipment():
    return "Shipment<1001, in transit>"

request: str = ""

while request != "quit":
    request = input(">   ")

    if request in routes:
        response = routes[request]()
        print(response, end="\n\n")
    else:
        print("Not Found")
# working with decorators in python
def ask_for_help():
    print("Please help me")

# ask_for_help()

def greeting(func):
    def polite():
        print("Hi!")
        func()
        print("Thank you!")
    return polite

greeting(ask_for_help)()

# instead of the above line, we can try the following method
@greeting # Adding the decorator
def ask_for_help():
    print("Please help me")

ask_for_help()

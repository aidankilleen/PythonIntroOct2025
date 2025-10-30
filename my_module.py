# my_module.py

# constant - naming convention - constants are ALL CAPS
DEFAULT_NAME="Fred"

def greet(name):

    print (f"Welcome {name}")


# this code gets executed when the module is run directl
# this code is skipped when the module is imported
if __name__ == "__main__":
    print(__name__)

    greet("Aidan")


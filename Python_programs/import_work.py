# this is first way
    # import demo_import

    # demo_import.welcome()
    # print(demo_import.x)

# this is second way
    # from demo_import import welcome,x

    # welcome()
    # print(x)

# third way
    # from demo_import import *

    # welcome()
    # print(x)

# forth way
    # import demo_import as d

    # d.welcome()
    # print(d.x)

# fifth way 
    # from demo_import import welcome as w,x

    # w()
    # print(x)

############# __name__ == "__main__" works #########################

import demo_import

demo_import.welcome() ## now it is printing statement 2 times because we are calling welcome func
#twice one from this file and other from jha se import kiya hai to uss comflict durr karne 
# liye hum __name__ ka use karege


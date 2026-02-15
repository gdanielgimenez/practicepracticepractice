# 8.15 printing models
from printers import greetings as saludos
from printers import *
import printers as prnt
from printers import greetings
import printers
from printers import print_models, show_completed_models

unprinted_designs = ['iphone 16', 'google pixel',
                     'xiaomi', 'samsung galaxy infinite']
completed_models = []

# function calls to test imported functions
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 8.16 kinds of imports

printers.greetings("nano")
greetings("Nani")
saludos("Nano")
prnt.greetings("NANO")
greetings("nani")

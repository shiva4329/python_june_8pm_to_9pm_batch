# how to import display and view fn's from submodule
# method 1

# import sub_module1.package2.display # Note : throws error bcoz display is not package

from sub_module1.package2 import display
display()
from sub_module1.package2 import view
view()

#Method2
from sub_module1.package2 import *

display()
view()

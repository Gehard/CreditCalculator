from collections import OrderedDict
import json
# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
firms = OrderedDict(json.loads(input()))

# your code here
for i in range(2):
    firms.popitem()
print(firms)

"""
OR

firms.popitem(last=True)
firms.popitem(last=True)
print(firms)

"""
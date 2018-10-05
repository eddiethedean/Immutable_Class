from immutable import Immutable

class Test_Immute(Immutable):

    def __init__(self, x):
        self.x = x

new_obj = Test_Immute(6)
print(new_obj.x)

new_obj.x = 7
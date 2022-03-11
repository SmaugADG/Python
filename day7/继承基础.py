class Father(object):
    def __init__(self):
        self.name='father'

    def print_name(self):
        print(self.name)
class Son(Father):
    pass

my_son=Son()
print(my_son.name)  # father
my_son.print_name() # father




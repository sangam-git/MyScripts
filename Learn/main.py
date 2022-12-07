# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from re import split


class classFile1():
    def __init__(self, f, l, i):
        self.f = f
        self.l = l
        self.i = i
        print("in init")

    def print_data(self):
        # Use a breakpoint in the code line below to debug your script.
        print("{} {} your id is {}".format(self.f, self.l, self.i))
    # @classmethod
    def wrongParam(cls, str):
        # f, l, i = split(str, "-")
        print("before init")
        # return cls(str, "", "1cr")
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    # classFile1.print_data(classFile1("suhas", "hiremath", "2crore"))
    a = classFile1.wrongParam(classFile1(1, 2, 3), "suhas")
    # a.print_data()
# else:
#     print("import __name__ = " + __name__)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

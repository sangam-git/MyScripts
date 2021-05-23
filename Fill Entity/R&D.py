def enter_exit_info(func):
    def wrapper(self, *arg, **kw):
        # print ('-- entering', func.__name__)
        # print '-- ', self.__dict__
        # res = func(self, *arg, **kw)
        # print '-- exiting', func.__name__
        # print '-- ', self.__dict_
        res = 1
        return res

    return wrapper


class TestWrapper():

    def __init__(self, *a, **b):
        print("inside init")
        # self.a = a
        # self.b = b
        # self.c = 0

    def tesedec(self):
        print("haha")

    @tesedec
    @__init__
    def sub(self):
        print("aaa")

    @enter_exit_info
    def add_in_c(self):
        self.c = self.a + self.b
        print(self.c)

    @enter_exit_info
    def mult_in_c(self):
        self.c = self.a * self.b
        print(self.c)


if __name__ == '__main__':
    t = TestWrapper(2, 3)
    # t.add_in_c()
    # t.mult_in_c()
    t.sub

from Timesheet import Entity

u = Entity()
u.browser


class ClientTimesheet():
    def login(self):
        u.browser.get("new url")

    def entevrvales(self):
        pass


# # # Open a new window
# u.browser.execute_script("window.open('');")
# u.browser.switch_to.window(u.browser.window_handles[0]) # driver.window_handles[1])
u.browser.get('https://www.google.com')
i = u.browser.window_handles
for each, e in range(i):
    if i(each).title == "gmail":
        u.browser.switch_to_window(each)

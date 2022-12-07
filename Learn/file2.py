import time

import js2py

#
#
# def fun1():
#     print("in file2")
#
#
# fun1()

c = """function add(x,y)
        {return  x + y;
         }
        sum =   add(2,3);
         alert(sum);"""
# e = js2py.EvalJs()
# e.execute(c)
# print(e.sum)

pop = """alert('hi'); """
import selenium
from selenium import webdriver

b = webdriver.Chrome("../Entity/Browsers/chromedriver.exe")
# b.get("http:/google.com")
b.maximize_window()
# e.execute(pop)
# b.execute_script(script=pop)
b.execute_script(c)
time.sleep(5)
b.quit()
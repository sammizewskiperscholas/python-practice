# x = 5
# if x<0:

# print("hello")
# print(5+8)
# print("see the raise exception below")
# print("enter the value of x:")
# x= int(input())
# # if x <0:
# #     raise Exception("The value of x should be positive")

# # x=45
# assert(x>35), "the value of x should be more than 35"
# x=int(input())

# try:
#     # 5/k
#     # 5+10
#     a=a+b
    
# except Exception as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("this is else block")
# finally:
#     print("try-catch successfully executed")

class Negative_numbers(Exception):
    pass
class toosmall(Exception):
    def __init__(self, message,value):
        self.message = message
        self.value = value

def test_data(x):
    if x<0:
        raise Negative_numbers("this is the negative number")
    if x<100:
        raise toosmall("this is the small number than 100",x)
try:
    # test_data(-5)
    test_data(50)
except Negative_numbers as e:
    print(e)
except Exception as e:
    # print(e)
    print(e.message,e.value)

    




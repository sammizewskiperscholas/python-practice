#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". 
# Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].


def make_it_big(num_list):
    big_list = []
    for n in num_list:
        if n > 0:
            big_list.append("big")
        else:
            big_list.append(n)
    return big_list

print(make_it_big([-1,3,5,-5]))
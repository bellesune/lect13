def my_func(num_iters, initial, second):
    if num_iters == 0:
        print("Nothing to iterate")
        return "Don't iterate"
    
    counter = 0
    while initial > 0 and counter < 10:
        initial += second
        counter += 1
    else:
        if counter == 10:
            return "counter is 10"
        else:
            return "initial is {}".format(initial)


# print(my_func(0,1,2))
# print(my_func(3,1,2))
# print(my_func(3,0,2))

# print(my_func(-2,-1100))
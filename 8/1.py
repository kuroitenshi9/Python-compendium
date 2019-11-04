'''
1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp. 
W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.
'''

this_is_list = [1, 0, 5, 68.9, "a", (2, 3), ["a", "b", "c"], True, {1, 2, 3}, 4+3j, {"pl" : "poland", "en" : "england"}]

for elem in this_is_list:
    try:
        result = 10 / elem
    except ZeroDivisionError as e:
        result = "Wyjątek 1:" + str(e)
    except TypeError as e:
        result = "Wyjątek 2:" + str(e)
    
    print(result)
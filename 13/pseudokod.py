def timer():
    def sort_elements(sort_method):
        start = time.now()
        sort_method()
        end = time.now()
        return end - start
    return sort_elements

@timer
def quicksort():
    pass
@timer
def countingsort():
    pass
@timer
def bubblesort():
    pass

clock - timer()

result_for_bubblesort = clock(bublesort())

from mpi4py import MPI

def find_sum(vector):
    my_sum = 0.0
    for i in range(len(vector)):
        my_sum += vector[i]
    return my_sum

def find_maximum(vector):
    my_max = 0.0
    for i in range(len(vector)):
        if vector[i] > my_max:
            my_max = vector[i]
    return my_max

n_numbers = 1024
rank = MPI.COMM_WORLD.Get_rank()

my_first_number = n_numbers * rank

vector = [my_first_number + i for i in range(n_numbers)]

my_sum = find_sum(vector)
print(f"The sum of the number is {my_sum}")

my_max = find_maximum(vector)
print(f"The largest number is {my_max}")

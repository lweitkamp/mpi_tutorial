from mpi4py import MPI

numbers = 10

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

numbers_per_rank = numbers // n_ranks
if numbers % n_ranks > 0:
    numbers_per_rank += 1

my_first = rank * numbers_per_rank
my_last = my_first + numbers_per_rank

for i in range(my_first, my_last):
    if i < numbers:
        print("I'm rank {:d} and I'm printing the number {:d}.".format(rank, i))

from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
print(f"My rank number is {rank}")

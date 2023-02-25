from mpi4py import MPI
import sys

n_ranks = MPI.COMM_WORLD.Get_size()
if n_ranks != 2:
    print("This example requires exactly two ranks")
    sys.exit(1)

rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:
    message = "Hello, World"
    MPI.COMM_WORLD.send(message, dest=1, tag=0)

if rank == 1:
    message = MPI.COMM_WORLD.recv(source=0, tag=0)
    print(message)

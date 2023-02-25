from mpi4py import MPI
import sys

n_ranks = MPI.COMM_WORLD.Get_size()
if n_ranks % 2 != 0:
    print("This example requires that the number of ranks is divisible by 2")
    sys.exit(1)

rank = MPI.COMM_WORLD.Get_rank()

if rank % 2 == 0:
    message = f"Hello from rank {rank}"
    MPI.COMM_WORLD.send(message, dest=rank+1, tag=0)

if rank % 2 == 1:
    message = MPI.COMM_WORLD.recv(source=rank-1, tag=0)
    print(f"Message received at rank {rank}:" + message)

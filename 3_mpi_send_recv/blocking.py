from mpi4py import MPI
import sys

n_numbers = 10000

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

if n_ranks != 2:
    print("This example requires exactly two ranks")
    sys.exit(1)


send_message = [i for i in range(n_numbers)]
neighbour = 1 if rank == 0 else 0

if rank == 0:
    MPI.COMM_WORLD.send(send_message, dest=neighbour, tag=0)

message = MPI.COMM_WORLD.recv(source=neighbour, tag=0)
print(f"Message received by rank {rank}")

if rank == 1:
    MPI.COMM_WORLD.send(send_message, dest=neighbour, tag=0)

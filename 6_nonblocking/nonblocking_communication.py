from mpi4py import MPI
import sys

n_numbers = 10000

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

if n_ranks != 2:
    print("Expecting exactly two ranks")
    sys.exit(1)


neighbour = 1 if rank == 0 else 0
send_message = [i for i in range(n_numbers)]

# MPI.COMM_WORLD.send(send_message, dest=neighbour, tag=0)
MPI.COMM_WORLD.isend(send_message, dest=neighbour, tag=0)

req = MPI.COMM_WORLD.irecv(source=neighbour, tag=0)
message = req.wait()

print(f"Message received by rank {rank}")

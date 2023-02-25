from mpi4py import MPI
import sys

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

if n_ranks != 2:
    print("Expecting exactly two ranks.")
    sys.exit(1)

rank_0_count = 0
rank_1_count = 0
max_len = 1000000
ball = "ball"

if rank == 0:
    neighbour = 1
else:
    neighbour = 0

if rank == 0:
    MPI.COMM_WORLD.send(ball, dest=1, tag=0)


counter = 0
bored = False
while not bored:
    ball = MPI.COMM_WORLD.recv(source=neighbour, tag=0)
    counter += 1
    MPI.COMM_WORLD.send(ball, dest=neighbour, tag=0)

    bored = counter >= max_len

print(f"Rank {rank} is done playing.")

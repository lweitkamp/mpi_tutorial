"""a serial code for Poisson equation
   contact seyong.kim81@gmail.com for comments and questions
"""

import numpy as np
from mpi4py import MPI
import math


def poisson_step(GRIDSIZE, u, unew, rho, hsq, rank, n_ranks):

    # Calculate one timestep
    for j in range(1, (GRIDSIZE//n_ranks)+1):
        for i in range(1, GRIDSIZE+1):
            difference = u[j][i-1] + u[j][i+1] + u[j-1][i] + u[j+1][i]
            unew[j][i] = 0.25*(difference - hsq*rho[j][i])
        print(f"Rank={rank}, j={j}")

    # Find the difference compared to the previous time step
    unorm = 0.0
    for j in range(1, (GRIDSIZE//n_ranks)+1):
        for i in range(1, GRIDSIZE+1):
            diff = unew[j][i] - u[j][i]
            unorm +=diff*diff

    # Sync unorm
    unorm = MPI.COMM_WORLD.allreduce(unorm, op=MPI.SUM)

    # Overwrite u with the new field
    for j in range(1, (GRIDSIZE//n_ranks)+1):
        for i in range(1, GRIDSIZE+1):
            u[j][i] = unew[j][i]

    return unorm

GRIDSIZE = 10

u = np.zeros((GRIDSIZE+2, GRIDSIZE+2))
unew = np.zeros((GRIDSIZE+2, GRIDSIZE+2))
rho = np.zeros((GRIDSIZE+2, GRIDSIZE+2))

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()
my_j_max = GRIDSIZE // n_ranks

# Set up parameters
h = 0.1
hsq = h*h

# Initialise the u and rho field to 0
# We are now parallelizing the j-art, so we will do i
# steps in parallel.
for j in range(my_j_max+2):
    for i in range(GRIDSIZE+2):
        u[j][i] = 0.0
        rho[j][i] = 0.0

if rank == 0:
    u[1][1] = 10

# Run a single iteration first
unorm = poisson_step(GRIDSIZE, u, unew, rho, hsq, rank, n_ranks)

if unorm == 112.5:
    print("Test Succeeded after 1 iteration")
else:
    print("Test Failed after 1 iteration")
    print("Norm", unorm)

for i in range(1, 10):
    unorm = poisson_step(GRIDSIZE, u, unew, rho, hsq, rank, n_ranks)

if abs(unorm - 0.208634816) < 1e-6:
    print("Test Succeeded after 10 iterations")
else:
    print("Test Failed after 10 iterations")
    print("Norm", unorm)


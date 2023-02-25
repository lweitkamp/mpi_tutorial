from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()

recvbuffer = MPI.COMM_WORLD.gather(rank, root=0)

if rank == 0:
    print(recvbuffer)

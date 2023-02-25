from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()


if rank == 0:
    for i in range(1, n_ranks):
        message = MPI.COMM_WORLD.recv(source=i, tag=0)
        print(message)

else:
    message = f"Hello World from rank {rank}"
    MPI.COMM_WORLD.send(message, dest=0, tag=0)

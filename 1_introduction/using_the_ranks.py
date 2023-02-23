from mpi4py import MPI

def rank_programming(a: int, b: int, rank: int):
    if rank == 0:
        print(f"a={a}, b={b}")
        print(f"a-b={a-b}")
    elif rank == 1:
        print(f"a+b={a+b}")
    elif rank == 2:
        print(f"a*b={a*b}")
    else:
        pass


if __name__ == "__main__":
    a: int = 5
    b: int = 6

    rank = MPI.COMM_WORLD.Get_rank()
    assert MPI.COMM_WORLD.Get_size() == 3, "Expecting exactly 3 ranks."
    rank_programming(a, b, rank)
    

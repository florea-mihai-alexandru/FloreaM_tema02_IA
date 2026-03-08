import numpy as np

if __name__ == '__main__':
    np.random.seed(1)

    A = np.array([np.random.randint(1, 100) for _ in range(12)]).reshape(4,3)

    B = np.array([np.random.randint(1, 100) for _ in range(15)]).reshape(3,5)

    print(f"Array A:\n{A}, \nB:\n{B}")

    C = A@B

    print(f"C:\n{C}")

    print(f"Sum = {C.sum()}")

    print(f"Mean = {C.mean(axis=0)}")

    print(f"Max = {C.max()}")

    M = np.array([np.random.randint(1, 100) for _ in range(9)]).reshape(3, 3)
    print(f"M:\n{M}")
    inv = np.linalg.inv(M)
    print(f"Inverse:\n{inv}")
    det = np.linalg.det(M)
    print(f"Determinant:\n{det}")
    prod = M@inv
    print(f"Product:\n{prod}")
    if np.allclose(prod,np.identity(3)):
        print("Close")
    else:
        print("not Close")

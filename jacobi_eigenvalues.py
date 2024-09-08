import numpy as np

def jacobi_eigenvalues(A, eps=1e-7, max_iter=10000):
    """
    Jacobi algorithm to compute eigenvalues of a symetrical matrix whose values are real

    :param A: Input symetrical matrix whose shape is (n, n)
    :param eps: epserance threshold for algorithm convergence (default : 1e-7)
    :param max_iter: Maximum iteration number (par défaut : 100)
    :return: (eigen_values, eigen_vectors)
    """
    
    # assert input matrix is symetrical
    n = A.shape[0]
    assert np.allclose(A, A.T), "Input matrix must be symetrical"

    # Cumulative rotation matrix
    V = np.eye(n)

    for iteration in range(max_iter):
        # Find the max value outside the diagonal
        max_val = 0
        p = 0
        q = 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j

        # Check for convergence
        if max_val < eps:
            break

        # Compute Jacobi's rotation angle
        if A[p, p] == A[q, q]:
            theta = np.pi / 4
        else:
            tau = (A[q, q] - A[p, p]) / (2 * A[p, q])
            if tau >= 0:
                t = 1 / (tau + np.sqrt(1 + tau ** 2))
            else:
                t = 1 / (tau - np.sqrt(1 + tau ** 2))
            theta = np.arctan(t)

        # Rotation matrix
        cos = np.cos(theta)
        sin = np.sin(theta)

        # Update matrix A by applying Jacobi's rotation
        A_pp = A[p, p]
        A_qq = A[q, q]
        A_pq = A[p, q]

        A[p, p] = cos**2 * A_pp - 2 * sin * cos * A_pq + sin**2 * A_qq
        A[q, q] = sin**2 * A_pp + 2 * sin * cos * A_pq + cos**2 * A_qq
        A[p, q] = A[q, p] = 0

        for i in range(n):
            if i != p and i != q:
                A_ip = A[i, p]
                A_iq = A[i, q]
                A[i, p] = A[p, i] = cos * A_ip - sin * A_iq
                A[i, q] = A[q, i] = sin * A_ip + cos * A_iq

        # Update eigen vectors matrix
        for i in range(n):
            V_ip = V[i, p]
            V_iq = V[i, q]
            V[i, p] = cos * V_ip - sin * V_iq
            V[i, q] = sin * V_ip + cos * V_iq

    # The eigen values are located on the diagonal of A
    eigen_values = np.diagonal(A)
    eigen_vectors = V

    return eigen_values, eigen_vectors
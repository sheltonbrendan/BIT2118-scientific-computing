# Task 09: Eigenvalues and Eigenvectors

Program: [`code/Task_09_eigenvalues.py`](../code/Task_09_eigenvalues.py) · Output: [`outputs/Task_09_eigenvalues_output.txt`](../outputs/Task_09_eigenvalues_output.txt)

## B. Inputs and mathematical operation
- **Inputs:** 4-node adjacency matrix.
- **Operation:** `np.linalg.eig`, dominant eigenpair, normalised eigenvector as importance; check Av = λv.

## C. Parameter change
Add a link A–D: the network becomes fully connected, dominant eigenvalue 2.5616 → 3.0000, and all centralities become 0.25.

Code: [`code/extensions/Task_09_extension.py`](../code/extensions/Task_09_extension.py) · Output: [`outputs/Task_09_extension_output.txt`](../outputs/Task_09_extension_output.txt)

## D. Meaning of the output
λ = 2.5616. B and C (0.2808) are most influential because they connect to every other node; A and D (0.2192) have fewer links. Verification error ~1e-15.

## E. Related real-world case
- **Case:** PageRank of four web pages (damping 0.85).
- **Assumptions / input data:** Links P1→P2,P3; P2→P3; P3→P1; P4→P3. Google matrix G = 0.85·M + 0.15/4.
- **Output:** Dominant eigenvalue 1.0; PageRank P1 0.3725, P2 0.1958, P3 0.3941, P4 0.0375.
- **Interpretation:** P3 ranks highest (three inbound links). P4 has no inbound links, so it only receives the teleport share 0.15/4 = 0.0375.

import math

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Solve f(x)=0 using Bisection Method.
    
    Parameters:
        f (function): Function f(x)
        a (float): Left interval
        b (float): Right interval
        tol (float): Tolerance
        max_iter (int): Maximum iterations
    
    Returns:
        float: Approximated root
    """
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    for i in range(max_iter):
        c = (a + b) / 2
        print(f"Iteration {i+1}: c = {c:.6f}, f(c) = {f(c):.6f}")
        
        if abs(f(c)) < tol or (b - a)/2 < tol:
            print("Converged!")
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    raise Exception("Did not converge within maximum iterations")

# -----------------------------
# Example Problem: f(x) = cos(x) - x
# -----------------------------
if __name__ == "__main__":
    f = lambda x: math.cos(x) - x
    a, b = 0, 1  # initial interval
    root = bisection_method(f, a, b)
    print("Approximate Root:", root)

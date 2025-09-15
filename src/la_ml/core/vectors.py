def add_vectors(v: list[float], w: list[float])-> list[float]:
    return [vi + wi for vi, wi in zip(v,w)]

def substract_vectors(v: list[float], w: list[float])-> list[float]:
    return [vi - wi for vi, wi in zip(v,w)]

def dot_product_vectors(v: list[float], w: list[float])-> list[float]:
    return sum([vi * wi for vi, wi in zip(v,w)])

def euclidean_norm_vector(v: list[float])-> list[float]:
    return (sum(vi**2.0 for vi in v))**0.5

def scalar_multiply_vector(v: list[float], scalar: float)-> list[float]:
    return [scalar * vi for vi in v]

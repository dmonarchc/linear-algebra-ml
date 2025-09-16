import pytest
from la_ml.core.vectors import add_vectors
from la_ml.core.vectors import subtract_vectors
from la_ml.core.vectors import dot_product_vectors
from la_ml.core.vectors import euclidean_norm_vector
from la_ml.core.vectors import scalar_multiply_vector
from la_ml.core.vectors import hadamard

def test_add_vectors():
    """Add two vectors element-wise"""
    v = [1.0,2.0,3.0]
    w = [4.0,5.0,6.0]
    result = add_vectors(v, w)
    assert result == [5.0,7.0,9.0]

def test_subtract_vectors():
    """Subtract two vectors element-wise"""
    v = [1.0,2.0,3.0]
    w = [4.0,5.0,6.0]
    result = subtract_vectors(v, w)
    assert result == [-3.0,-3.0,-3.0]

def test_dot_product_vectors():
    """Dot product of two vectors"""
    v = [1.0, 2.0, 3.0]
    w = [4.0, 5.0, 6.0]
    result = dot_product_vectors(v, w)
    assert result == 32.0 

def test_hadamard():
    """Hadamard"""
    v = [1.0, 2.0, 3.0]
    w = [4.0, 5.0, 6.0]
    result = hadamard(v, w)
    assert result == [4.0, 10.0, 18.0]

def test_euclidean_norm_vector():
    """Euclidean norm for a vector"""
    v = [1.0, 2.0, 3.0]
    result = euclidean_norm_vector(v)
    assert result == 14**0.5

def test_scalar_multiply_vector():
    """Scalar multiply for a vector"""
    v = [1.0, 2.0, 3.0]
    scalar = 5.0
    result = scalar_multiply_vector(v, scalar)
    assert result == [5.0, 10.0, 15.0]

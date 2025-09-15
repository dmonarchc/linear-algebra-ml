# Linear Algebra for Machine Learning

This repository is a **learning project** focused on building the foundations of linear algebra from scratch and applying them to **Machine Learning**, with a step-by-step implementation of **Principal Component Analysis (PCA)**.

The goal is not only to practice programming in Python but also to deeply understand the mathematics behind vector and matrix operations that power modern ML libraries.

---

## 📂 Project Structure

```
linear-algebra-ml/
├─ data/          # small datasets for experiments
├─ docs/          # documentation and diagrams
├─ notebooks/     # Jupyter notebooks for exploration
├─ scripts/       # CLI scripts to run pipelines
├─ tests/         # unit and integration tests
└─ src/
   └─ la_ml/   # main package
      ├─ core/        # pure math: vectors, matrices, stats, decomposition
      ├─ pca/         # PCA algorithm built on top of core
      ├─ adapters/    # I/O, NumPy/Sklearn bridges, visualization
      └─ app/         # pipelines orchestrating the steps
```

---

## 🎯 Learning Objectives
- Implement basic **vector** and **matrix** operations manually.
- Build your own **mini linear algebra library** in Python.
- Understand and implement **covariance** and **eigendecomposition**.
- Develop **PCA from scratch** and validate results against scikit-learn.
- Learn to separate **pure math logic** from **I/O and visualization**.

---

## 🛠 Tech Stack
- **Language**: Python 3.10+
- **Core**: pure Python (lists, loops) for learning purposes.
- **Optional**: NumPy, Matplotlib, scikit-learn (for comparison and acceleration).
- **Testing**: pytest.

---

## 🚀 Roadmap

- [x] **Stage 0**: Project setup (environment, repo, initial docs).  
- [x] **Stage 1**: Vector operations (sum, dot, norm, scaling).  
- [ ] **Stage 2**: Matrix operations (transpose, multiplication, shape validation).  
- [ ] **Stage 3**: Advanced ops (determinant, inverse, eigenvalues/vectors).  
- [ ] **Stage 4**: Data preprocessing (centering, covariance matrix).  
- [ ] **Stage 5**: PCA implementation (fit, transform, explained variance).  
- [ ] **Stage 6**: Optimization with NumPy + comparison with scikit-learn.  
- [ ] **Stage 7**: Extensions (SVD, Iris/MNIST datasets, explanatory notebooks).  

---

## 📚 References
- *Linear Algebra and Its Applications* – Gilbert Strang  
- *Pattern Recognition and Machine Learning* – Christopher M. Bishop  
- [Scikit-Learn PCA Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)  
- [NumPy Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)

---

## 📌 Notes
This is a **learning-oriented project**, not a production-ready library.  
The main goal is to practice **modular design, mathematics, and coding discipline** while reinforcing linear algebra concepts used in machine learning.

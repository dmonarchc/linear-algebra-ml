# Arquitectura del proyecto

## Capas
- **core/**: lógica matemática pura (sin I/O).
- **pca/**: algoritmo PCA usando core/.
- **adapters/**: I/O, puentes con NumPy/Sklearn, visualización.
- **app/**: pipelines que orquestan casos de uso.

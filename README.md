strkernels
=======
**strkernels** is a Python package compatible with Scikit-learn that implements string kernels.

String kernels are functions that return a value representing how similar two input strings are. They are widely used in machine learning methods for text and biological sequence analyses.

The prominent aspect of string kernels is that the prior extraction and selection of sequence features are unnecessary. The sample symbol sequences are inputs to the kernel function, automatically finding the distinguishing string features.

In this first realease, the available string kernels are:
- Fixed Degree String Kernel
- Subsequence String Kernel


## Basic usage

Install with pip:
```
pip install strkernels
```

Import and create a kernel:
```python
from strkernels import SubsequenceStringKernel
subsequence_kernel = SubsequenceStringKernel(maxlen=3, ssk_lambda=0.5)
```

Example data:
```python
import numpy as np
strings = np.array(["ATCG", "ATGG", "TACG", "GCTA"])
```

Compute the kernel matrix:
```python
kernel_matrix = subsequence_kernel(strings, strings)
print(kernel_matrix)
```

Or use the kernel object with Scikit-learn:
```python
from sklearn.svm import SVC
clf = SVC(kernel=subsequence_kernel)

# train the classifier
clf.fit(X_train, y_train)

# make predictions using the classifier
predictions = clf.predict(X_test)
```
## Documentation

[Refer to the documentation for comprehensive examples of applying string kernels to biological sequences.](docs/index.md)

## Reference

If you use or discuss this package, please cite:

Barbosa, D.F., Rocha, M., Kashiwabara, A.Y. (2024). strkernels: a optimized string kernels Python package. *Under development*. 

## License

[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)


## Contact

To report bugs, to ask for help and to give any feedback, please contact denilsonfbar@gmail.com

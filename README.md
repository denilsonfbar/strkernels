strkernels
=======
**strkernels** is a Python package compatible with Scikit-learn that implements string kernels.

String kernels are functions that return a value representing how similar two input strings are. They are widely used in machine learning methods for text and biological sequence analysis.

The prominent aspect of string kernels is that the prior extraction and selection of sequence features are unnecessary. The sample symbol sequences are inputs to the kernel function, automatically finding the distinguishing string features.

Currently, the available string kernels are:
- Locality Improved (Zien *et al.* 2000)
- Subsequence (Lodhi *et al.* 2002)
- Spectrum (Leslie *et al.* 2002)
- Weighted Degree (Ratsch *et al.* 2004)
- Fixed Degree (Sonnenburg *et al.* 2010)


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
y = np.array([-1, -1, 1, 1])
```

Compute the kernel matrix:
```python
kernel_matrix = subsequence_kernel(strings, strings)

print(kernel_matrix)
```
```
[[1.         0.74037191 0.91640867 0.79256966]
 [0.74037191 1.         0.68420576 0.65356968]
 [0.91640867 0.68420576 1.         0.84210526]
 [0.79256966 0.65356968 0.84210526 1.        ]]
```

Or use the kernel object with Scikit-learn:
```python
from sklearn.svm import SVC
clf = SVC(kernel=subsequence_kernel)

# train the classifier
clf.fit(strings, y)

# make predictions using the classifier
predictions = clf.predict(strings)

print(predictions)
```

```
[-1 -1  1  1]
```


## Documentation

[Refer to the documentation for comprehensive examples of applying string kernels to biological sequences.](https://github.com/denilsonfbar/strkernels/tree/main/docs)

## Reference

If you use or discuss this package, please cite:

Barbosa, D.F., Rocha, M., Kashiwabara, A.Y. (2024). strkernels: a optimized string kernels Python package. *Under development*. 

## License

[GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.html)


## Contact

To report bugs, to ask for help and to give any feedback, please contact denilsonfbar@gmail.com


# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


from .string_kernel import StringKernel


class LinearStringKernel(StringKernel):
    """
    The standard linear kernel for input strings.
    """

    def __init__(self, **kernel_params):

        # base class constructor
        super().__init__(**kernel_params)

        self._kernel_name = 'LinearStringKernel'
        

    def __call__(self, X_left, X_right, **kernel_params):

        # base class __call__ function
        super().__call__(X_left, X_right, **kernel_params)

        """
        The Shogun kernel object is created here and not in the constructor 
        because the Sklearn GridSearchCV executes the constructor only once 
        and makes copies of the created kernel object to perform the 
        cross-validation executions in parallel.
        """
        from .libshogun.shogun import LinearStringKernel
        self._shogun_kernel_obj = LinearStringKernel(self._X_left_sg, self._X_right_sg)

        return self._shogun_kernel_obj.get_kernel_matrix()

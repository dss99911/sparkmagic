# Copyright (c) 2015  aggftw@gmail.com
# Distributed under the terms of the Modified BSD License.
from sparkmagic.utils.constants import LANG_PYTHON
from sparkmagic.kernels.wrapperkernel.sparkkernelbase import SparkKernelBase


class PySpark3Kernel(SparkKernelBase):
    def __init__(self, **kwargs):
        implementation = "PySpark3"
        implementation_version = "1.0"
        language = LANG_PYTHON
        language_version = "0.1"
        language_info = {
            "name": "pyspark",
            "mimetype": "text/x-python",
            "codemirror_mode": {"name": "python", "version": 3},
            "file_extension": ".py",
            "pygments_lexer": "python3",
        }

        session_language = LANG_PYTHON

        super(PySpark3Kernel, self).__init__(
            implementation,
            implementation_version,
            language,
            language_version,
            language_info,
            session_language,
            "python_temp",
            **kwargs
        )


if __name__ == "__main__":
    from ipykernel.kernelapp import IPKernelApp

    IPKernelApp.launch_instance(kernel_class=PySpark3Kernel)

# How to use 2nd kernel with different endpoint

1. git clone https://github.com/dss99911/sparkmagic.git
2. git checkout add_2nd_kernel
3. pip install -e sparkmagic
4. jupyter-kernelspec install sparkmagic/kernels/pyspark2kernel
5. add 'kernel_python2_credentials' on .sparkmagic/conf.json
6. add session_configs.name = {your-name}

```shell
git clone https://github.com/dss99911/sparkmagic.git
cd sparkmagic
pip install -e sparkmagic
sudo jupyter-kernelspec install sparkmagic/sparkmagic/kernels/pysparkkernel
sudo jupyter-kernelspec install sparkmagic/sparkmagic/kernels/pyspark2kernel
sudo jupyter-kernelspec install sparkmagic/sparkmagic/kernels/pyspark3kernel

```


# Change kernel name
1. find the file below on your local path.
  - https://github.com/dss99911/sparkmagic/blob/add_2nd_kernel/sparkmagic/sparkmagic/kernels/pyspark2kernel/kernel.json
2. change 'display_name'

# Custom Spark Magic

## Features
- 3 kernel to connect different cluster
- connection by EMR cluster name
  - set cluster_name on config
- connection by url
  - set url on config
  - if cluster_name is set, url is ignored.

## Install
```shell
git clone https://github.com/dss99911/sparkmagic.git
cd sparkmagic
git checkout add_2nd_kernel
pip install -e sparkmagic
sudo jupyter-kernelspec install sparkmagic/sparkmagic/kernels/pysparkkernel
sudo jupyter-kernelspec install sparkmagic/sparkmagic/kernels/pyspark2kernel
sudo jupyter-kernelspec install sparkmagic/sparkmagic/kernels/pyspark3kernel
```

## Config
add the json below on `~/.sparkmagic/conf.json`
```json
{
  "kernel_python_dev_credentials": {
    "cluster_name": "Dev Cluster V14",
    "username": "",
    "password": "",
    "url": "",
    "auth": "None"
  },
  "kernel_python_ds_credentials": {
    "cluster_name": "DS_CLUSTER",
    "username": "",
    "password": "",
    "url": "",
    "auth": "None"
  },
  "kernel_python_temp_credentials": {
    "cluster_name": "",
    "username": "",
    "password": "",
    "url": "http://10.50.7.81:8998",
    "auth": "None"
  }
}
```

## TODO
session_configs.name
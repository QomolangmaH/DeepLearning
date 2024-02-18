"""This package introduces the various data structures of PyTorch
- Tensor：
    Tensor is the most basic data structure in PyTorch, similar to a multidimensional array. It can represent scalars,
    vectors, matrices, or arrays of any dimension.
- Variable:
    Variable is a wrapper for Tensor used for automatic differentiation. Variable automatically tracks and  records
    operations on it, thus building a computational graph and supporting automatic differentiation. In PyTorch  0.4.0
    and later versions, Variable has been deprecated, and Tensor can be directly used for automatic differentiation.
- Dataset:
    Dataset is an abstract class used to represent a dataset. By inheriting from the Dataset class, custom datasets can
    be defined and functions for data loading, preprocessing, and sample retrieval can be implemented. PyTorch provides
    some built-in dataset classes, such as MNIST, CIFAR-10, etc., for conveniently loading commonly used datasets.
- DataLoader:
    DataLoader is used to load data from the Dataset in batches and provides multi-threading and multi-processing data
    prefetching. It can efficiently load large-scale datasets and support operations such as random shuffling of data,
    parallel loading, and data augmentation.
- Module:
    Module is the base class for building models in PyTorch. By inheriting from the Module class, one can define their
    own models and implement methods for forward and backward propagation. Module provides functionality for parameter
    management, model saving and loading, making model training and deployment convenient.
"""
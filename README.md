# Specify the number of cores
https://github.com/fchollet/keras/issues/4314
```
config = tf.ConfigProto(intra_op_parallelism_threads=1, inter_op_parallelism_threads=1, \
                        allow_soft_placement=True, device_count = {'CPU': 1})
session = tf.Session(config=config)
or
with tf.Session(config=config) as sess:
```

# Change data type
https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html
```
>>> x = np.array([1, 2, 2.5])
>>> x
array([ 1. ,  2. ,  2.5])

>>> x.astype(int)
array([1, 2, 2])
```

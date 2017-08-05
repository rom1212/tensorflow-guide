#!/bin/bash
set -ex
for dir in 600000.ss-2 600000.ss-3 600000.ss-4 600000.ss-5 600000.ss-6 600000.ss-7 
do
    echo dir: $dir

    python mnist_deep.py --data_dir=$dir --iter=2000
    python mnist_deep.py --data_dir=$dir --iter=2000
    python mnist_deep.py --data_dir=$dir --iter=2000

    python mnist_deep.py --data_dir=$dir --iter=5000
    python mnist_deep.py --data_dir=$dir --iter=5000
    python mnist_deep.py --data_dir=$dir --iter=5000


    python mnist_deep.py --data_dir=$dir --iter=10000
    python mnist_deep.py --data_dir=$dir --iter=10000
    python mnist_deep.py --data_dir=$dir --iter=10000

    python mnist_deep.py --data_dir=$dir --iter=20000
    python mnist_deep.py --data_dir=$dir --iter=20000
    python mnist_deep.py --data_dir=$dir --iter=20000
done

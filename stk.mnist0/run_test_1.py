#!/usr/bin/python

import argparse
import sys
import mnist_softmax

FLAGS = None
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  print('FLAGS:', FLAGS, ', unparsed:', unparsed)

  mnist_softmax.FLAGS = FLAGS
  mnist_softmax.main([sys.argv[0]] + unparsed)

  # tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

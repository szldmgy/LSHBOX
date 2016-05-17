#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylshbox_example2.py
import pylshbox
import numpy as np
import time
print 'prepare test data'
float_mat = np.random.randn(100000, 192)
float_query = float_mat[1, :]
print ''
print 'Test itqLsh'
print ''
print 'First time, need to constructing index.'  # About 1.5s.
start = time.time()
itq_mat = pylshbox.itqlsh()
itq_mat.init_mat(float_mat.tolist(), 'pyitq.lsh', 521, 5, 8, 100, 50)
result = itq_mat.query(float_query.tolist(), 2, 10)
indices, dists = result[0], result[1]
for i in range(len(indices)):
    print indices[i], '\t', dists[i]
print 'Elapsed time is %f seconds.' % (time.time() - start)
print ''
print 'Second time, no need to re-indexing.'  # About 0.05s.
start = time.time()
itq_mat2 = pylshbox.itqlsh()
itq_mat2.init_mat(float_mat.tolist(), 'pyitq.lsh')
result = itq_mat2.query(float_query.tolist(), 2, 10)
indices, dists = result[0], result[1]
for i in range(len(indices)):
    print indices[i], '\t', dists[i]
print 'Elapsed time is %f seconds.' % (time.time() - start)


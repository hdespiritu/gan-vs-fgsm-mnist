#from multiprocessing import Pool, TimeoutError #(SLOW)
import os
#import threading
import time
from random import random
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

def worker(i):
    work_name = ''#threading.currentThread().getName()
    print work_name, 'Starting'
    w_time = time.time()
    """thread worker fxn"""
    sleep_val = (5*random())
    time.sleep(sleep_val)
    print 'Worker' + i +": ("+work_name+") exiting - " +str(time.time() - w_time)
    return sleep_val

num_tasks=100
then = time.time()
#################################################
#best approach??
#################################################
#pool = ThreadPoolExecutor()
#futures = [pool.submit(worker, str(i)) for i in range(num_tasks)]
#results = [r.result() for r in as_completed(futures)]
#print "Threadpool done in %s" % (time.time()-then)


#################################################
#best approach??
#################################################
pool = ThreadPoolExecutor()
results = list(pool.map(worker, [str(i) for i in range(num_tasks)]))
pool.shutdown()
#futures = [pool.submit(worker, str(i)) for i in range(num_tasks)]
#results = [r.result() for r in as_completed(futures)]
print "Threadpool done in %s" % (time.time()-then)
print('results[:10] = {}'.format(results[:10]))
#################################################
#slow
#################################################
#pool = Pool()
#pool.map(worker, [str(i) for i in range(num_tasks)])
#print "Processpool done in %s" % (time.time()-then)


#################################################
#incorrect output
#################################################
#threads = []
#for i in range(num_tasks):
#    t = threading.Thread(target=worker, args=(str(i+1),))
#    threads.append(t)
#    t.start()

#print "Threading done in %s" % (time.time()-then)

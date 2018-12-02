



'''
#
'''
import numpy as np




'''
#
#
#   Notes:
#       dataset1_v3.npy is a proper dataset, 
#           because the cache hit rate is about 25%, using LRU
'''
def fetchData():

    data = np.load('dataset1_v3.npy')
    print('data.shape: \t', data.shape)

    return 0






if __name__ == '__main__':

    print('*** BuildData ***')

    fetchData()
    #np.random.zipf()

# END OF FILE
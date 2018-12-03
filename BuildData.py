



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

    return data

def testData():

    dataR = fetchData().reshape(-1, )
    print('dataR.shape: \t', dataR.shape)

    LEN = 1000
    START = 3333
    LookBack = 20

    Pr = []
    for i in range(LookBack):
        start = START + i
        data_tmp = dataR[start:start+LEN]
        mask_tmp = (data_tmp == 1)
        Pr.append(data_tmp[mask_tmp].shape[0])
    print('Pr: \n', Pr)



    return 0




if __name__ == '__main__':

    print('*** BuildData ***')

    #fetchData()
    testData()
    #np.random.zipf()

# END OF FILE




'''
#
'''
import numpy as np
#import seq2seq
import matplotlib.pyplot as plt



'''
'''
LookBack = 20
ForecastStep = 1

ClassNum = 50


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



'''
#
'''
def calx(data):
    assert data.ndim == 2
    #
    N = 1000
    END = data.shape[0]

    x = np.zeros((END-N, ClassNum))
    for i in range(N, END):

        for j in range(ClassNum):
            data_tmp = data[i:i+N, j]
            mask_tmp = (data_tmp==1)
            x[i-N, j] = data_tmp[mask_tmp].shape[0]

    x = x / N

    return x




'''
#
'''
def cmpt_Xti():

    print('### Starting compute Xti')
    data = np.load('dataset1_v3.npy')
    requestsLEN = data.shape[0] * data.shape[1]
    data = data.reshape(requestsLEN, )
    print('data.shape: \t', data.shape)
    # OneHot
    data_OneHot = np.eye(ClassNum)[data]
    print('data_OneHot.shape: \t', data_OneHot.shape)

    #
    X = np.zeros((requestsLEN, ClassNum))
    print('X.shape = ', X.shape)
    '''
    '''
    historyLEN = 1000
    for t in range(historyLEN-1, requestsLEN):
        for i in range(0, ClassNum):
            data_OneHot_tmp = data_OneHot[t-historyLEN+1:t, i]
            mask_tmp = (data_OneHot_tmp==1)

            X[t, i] = data_OneHot_tmp[mask_tmp].shape[0]
    #
    X = X / historyLEN

    SaveName = 'dataComputed/' + 'Xti'
    np.savez_compressed(SaveName, Xti=X)

    print('compute Xti and save successfully!!')

    return X

def show_Xti():

    Xti = np.load('dataComputed/Xti.npz')['Xti']
    print('Xti.shape = ', Xti.shape)

    nrows = 3
    ID = 24

    t = np.arange(Xti.shape[0])


    plt.figure(1)
    #plt.set_title('ObjectID = '+str(ID), fontsize=64)
    plt.subplot(311)
    plt.title('ObjectID = '+str(ID), fontsize=12)
    plt.plot(t, Xti[:, ID], linewidth=1.2)
    plt.ylabel('probability', fontsize=10)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.grid(True, linestyle='-.')
    #plt.set_title('ObjectID = '+str(ID), fontsize=64)
    #plt.set_xlabel('time', fontsize=48)
    #plt.set_ylabel('probability', fontsize=48)

    plt.subplot(312)
    plt.plot(t[12000:20000], Xti[:, ID][12000:20000], linewidth=1.2)
    plt.ylabel('probability', fontsize=10)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.grid(True, linestyle='-.')

    plt.subplot(313)
    plt.plot(t[12000:12800], Xti[:, ID][12000:12800], linewidth=1.2)
    plt.ylabel('probability', fontsize=10)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.grid(True, linestyle='-.')

    plt.xlabel('time', fontsize=10)

    SaveName = 'figurePloted/' + 'show_Xti.png'
    plt.savefig(SaveName, dpi=256)

    return 0




'''
#   construct x Sequence
#   Parameters:
#       x:              an array, shape=(T, 1), t=0,1,...,T-1
#       look_back:      a scalar
#       forecast_step:  a scaler
#   Return:
#       history:        an array, shape=(-1, look_back, 1)
'''
def consSeqx(x, look_back=168, forecast_step=4, testFlag=False):

    assert x.ndim == 2
    T = x.shape[0] # the length of x

    history = []
    step = 1 #
    # if it is for test
    #   evary another forecast_step, make a forecast
    if testFlag:
        step = forecast_step
    for i in range(0, T-look_back+1, step):
        # look_back of one window of x
        win_x = list(x[i:i+look_back])
        history.append(win_x)

    history = np.array(history)
    return history




'''
#   construct y Sequence
#   Parameters:
#       y:              an array, shape=(T+forecast_step, 1), t=0,...,T+forecat_step-1
#       look_back:      a scalar
#       forecast_step:  a scaler
#   Return:
#       label:          an array, shape=(-1, forecast_step, 1)
'''
def consSeqy(y, look_back=168, forecast_step=4, testFlag=False):

    assert y.ndim == 2
    T = y.shape[0] # the length of y, actually, T=T+forecat_step

    label = []
    step = 1 #
    # if it is for test
    #   evary another forecast_step, make a forecast
    if testFlag:
        step = forecast_step
    for i in range(look_back, T-forecast_step+1, step):
        win_y = list(y[i:i+forecast_step])
        label.append(win_y)

    label = np.array(label)
    return label





'''
'''
def consXY():
    print('*** consXY ***')
    data = np.load('dataset1_v3.npy')
    requestsLEN = data.shape[0] * data.shape[1]
    data = data.reshape(requestsLEN, )
    print('data.shape: \t', data.shape)

    ClassNum = 50
    data_OneHot = np.eye(ClassNum)[data]
    print('data_OneHot.shape: \t', data_OneHot.shape)
    #res = np.argmax(data_OneHot, axis=1)
    #print(res == data)
    N = 1000
    x = calx(data_OneHot)
    print('x.shape: \t', x.shape)
    print(x)
    '''
    xTrain = data_OneHot[:-ForecastStep]
    yTrain = data_OneHot
    x_train = consSeqx(xTrain, LookBack, ForecastStep)
    y_train = consSeqy(yTrain, LookBack, ForecastStep)
    print('x_train.shape: \t', x_train.shape)
    print('y_train.shape: \t', y_train.shape)

    x_test = consSeqx(xTrain, LookBack, ForecastStep, testFlag=True)
    y_test = consSeqy(yTrain, LookBack, ForecastStep, testFlag=True)
    print('x_test.shape: \t', x_test.shape)
    print('y_test.shape: \t', y_test.shape)

    print('*** consXY Successfully !! ***')

    return x_train, y_train, x_test, y_test
    '''
    xTrain = x[:-ForecastStep]
    yTrain = data_OneHot[N:]
    x_train = consSeqx(xTrain, LookBack, ForecastStep)
    y_train = consSeqy(yTrain, LookBack, ForecastStep)
    print('x_train.shape: \t', x_train.shape)
    print('y_train.shape: \t', y_train.shape)

    x_test = consSeqx(xTrain, LookBack, ForecastStep, testFlag=True)
    y_test = consSeqy(yTrain, LookBack, ForecastStep, testFlag=True)
    print('x_test.shape: \t', x_test.shape)
    print('y_test.shape: \t', y_test.shape)

    print('*** consXY Successfully !! ***')

    return x_train, y_train, x_test, y_test




if __name__ == '__main__':

    print('*** BuildData ***')

    #fetchData()
    #testData()
    #np.random.zipf()
    #cmpt_Xti()
    show_Xti()

# END OF FILE

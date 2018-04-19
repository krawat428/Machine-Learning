from PIL import Image
import numpy as np
np.seterr(over='ignore')
import matplotlib.pyplot as plt
import time 
from collections import Counter

def createExamples():
    NumberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for num in numbersWeHave:
        for version in versionsWeHave:
            imageFilePath = 'images/numbers/'+str(num)+"."+str(version)+".png"
            ei=Image.open(imageFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            lineToWrite = str(num)+'::'+eiar1+"\n"
            NumberArrayExamples.write(lineToWrite)



def black_white(imageArray):
    balanceAr = []
    newAr = imageArray
    total=0
    for row in imageArray:
        for pix in row:
            avgNum = (pix[0]+pix[1]+pix[2])/3
            balanceAr.append(avgNum)
    for n in balanceAr:
        total+=n
    balance=total/len(balanceAr)

    

    for row in newAr:
        for pix in row:
            avgNum=(pix[0]+pix[1]+pix[2])/3
            if avgNum > balance:
                pix[0] = 255
                pix[1] = 255
                pix[2] = 255
                pix[3] = 255
            else:
                pix[0] = 0
                pix[1] = 0
                pix[2] = 0
                pix[3] = 255
    return newAr

def whatNumIsThis(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixInQ  = inQuestion.split('],')

            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x += 1
    print(matchedAr)
    x = Counter(matchedAr)
    print(x)

    # Line Graph indication method
    '''graphX = []
    graphY = []
    for eachThing in x:
        print(eachThing)
        graphX.append(eachThing)
        print(x[eachThing])
        graphY.append(x[eachThing])
        
    fig = plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)
    xloc = plt.MaxNLocator(12)

    ax2.xaxis.set_major_locator(xloc)
    
    plt.show()'''

    hN=0
    hV=0
    for n in x:
        if x[n]>hV:
            hV=x[n]
            hN=n
    if hV<350:
        good=False
        return hV
    else:
        good=True
           
    print('\n\n\nthe Number Is ->{}'.format(hN))
    
whatNumIsThis('images/test.png')
                    
            
                                                        
                                                            
'''
i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/k.png')
iar4 = np.array(i4)


black_white(iar)
black_white(iar2)
black_white(iar3)
black_white(iar4)
fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
'''

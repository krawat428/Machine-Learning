from PIL import Image
import numpy as np
np.seterr(over='ignore')
import matplotlib.pyplot as plt



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

                    
            
                                                        
                                                            

i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
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


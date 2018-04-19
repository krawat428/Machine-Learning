from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time 

i = Image.open('images/numbers/y0.5.png')
iar = np.asarray(i)

#this image is of 8 by 8 pixel length
# 255 is actualy 256 as start from 0 so image saved as 256 bit map  
#print(iar)
plt.imshow(iar)
plt.show()
i.close()

import pickle

with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\1.pickle" , "rb") as f1:
    date_list_1 = pickle.load(f1)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\2.pickle" , "rb") as f2:
    date_list_2 = pickle.load(f2)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\3.pickle" , "rb") as f3:
    date_list_3 = pickle.load(f3)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\4.pickle" , "rb") as f4:
    date_list_4 = pickle.load(f4)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\5.pickle" , "rb") as f5:
    date_list_5 = pickle.load(f5)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\6.pickle" , "rb") as f6:
    date_list_6 = pickle.load(f6)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\7.pickle" , "rb") as f7:
    date_list_7 = pickle.load(f7)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\8.pickle" , "rb") as f8:
    date_list_8 = pickle.load(f8)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\9.pickle" , "rb") as f9:
    date_list_9 = pickle.load(f9)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\10.pickle" , "rb") as f10:
    date_list_10 = pickle.load(f10)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\11.pickle" , "rb") as f11:
    date_list_11 = pickle.load(f11)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\12.pickle" , "rb") as f12:
    date_list_12 = pickle.load(f12)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\13.pickle" , "rb") as f13:
    date_list_13 = pickle.load(f13)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\14.pickle" , "rb") as f14:
    date_list_14 = pickle.load(f14)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\15.pickle" , "rb") as f15:
    date_list_15 = pickle.load(f15)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\16.pickle" , "rb") as f16:
    date_list_16 = pickle.load(f16)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\17.pickle" , "rb") as f17:
    date_list_17 = pickle.load(f17)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\18.pickle" , "rb") as f18:
    date_list_18 = pickle.load(f18)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\19.pickle" , "rb") as f19:
    date_list_19 = pickle.load(f19)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\20.pickle" , "rb") as f20:
    date_list_20 = pickle.load(f20)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\21.pickle" , "rb") as f21:
    date_list_21 = pickle.load(f21)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\22.pickle" , "rb") as f22:
    date_list_22 = pickle.load(f22)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\23.pickle" , "rb") as f23:
    date_list_23 = pickle.load(f23)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\24.pickle" , "rb") as f24:
    date_list_24 = pickle.load(f24)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\25.pickle" , "rb") as f25:
    date_list_25 = pickle.load(f25)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\26.pickle" , "rb") as f26:
    date_list_26 = pickle.load(f26)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\27.pickle" , "rb") as f27:
    date_list_27 = pickle.load(f27)
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\28.pickle" , "rb") as f28:
    date_list_28 = pickle.load(f28)
'''
with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\2019-11-17_130.pickle" , "rb") as f9:
    date_list_9 = pickle.load(f9)

with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\2019-11-17_155.pickle" , "rb") as f10:
    date_list_10 = pickle.load(f10)    

with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\2019-11-17_130.pickle" , "rb") as f11:
    date_list_11 = pickle.load(f11)

with open ("C:\\MLGame-master\\games\\arkanoid\\log\\test2\\2019-11-17_140.pickle" , "rb") as f12:
    date_list_12 = pickle.load(f12)
'''
Frame = [ ]
Status = [ ]
Ballposition = [ ]
Platformposition = [ ]
Bricks = [ ]

for i in range (0,len(date_list_1)):
    Frame.append(date_list_1[i].frame)
    Status.append(date_list_1[i].status)
    Ballposition.append(date_list_1[i].ball)
    Platformposition.append(date_list_1[i].platform)
    Bricks.append(date_list_1[i].bricks)

for i in range (0,len(date_list_2)):
    Frame.append(date_list_2[i].frame)
    Status.append(date_list_2[i].status)
    Ballposition.append(date_list_2[i].ball)
    Platformposition.append(date_list_2[i].platform)
    Bricks.append(date_list_2[i].bricks)
for i in range (0,len(date_list_3)):
    Frame.append(date_list_3[i].frame)
    Status.append(date_list_3[i].status)
    Ballposition.append(date_list_3[i].ball)
    Platformposition.append(date_list_3[i].platform)
    Bricks.append(date_list_3[i].bricks)

for i in range (0,len(date_list_4)):
    Frame.append(date_list_4[i].frame)
    Status.append(date_list_4[i].status)
    Ballposition.append(date_list_4[i].ball)
    Platformposition.append(date_list_4[i].platform)
    Bricks.append(date_list_4[i].bricks)
for i in range (0,len(date_list_5)):
    Frame.append(date_list_5[i].frame)
    Status.append(date_list_5[i].status)
    Ballposition.append(date_list_5[i].ball)
    Platformposition.append(date_list_5[i].platform)
    Bricks.append(date_list_5[i].bricks)

for i in range (0,len(date_list_6)):
    Frame.append(date_list_6[i].frame)
    Status.append(date_list_6[i].status)
    Ballposition.append(date_list_6[i].ball)
    Platformposition.append(date_list_6[i].platform)
    Bricks.append(date_list_6[i].bricks)
for i in range (0,len(date_list_7)):
    Frame.append(date_list_7[i].frame)
    Status.append(date_list_7[i].status)
    Ballposition.append(date_list_7[i].ball)
    Platformposition.append(date_list_7[i].platform)
    Bricks.append(date_list_7[i].bricks)

for i in range (0,len(date_list_8)):
    Frame.append(date_list_8[i].frame)
    Status.append(date_list_8[i].status)
    Ballposition.append(date_list_8[i].ball)
    Platformposition.append(date_list_8[i].platform)
    Bricks.append(date_list_8[i].bricks)

for i in range (0,len(date_list_9)):
    Frame.append(date_list_9[i].frame)
    Status.append(date_list_9[i].status)
    Ballposition.append(date_list_9[i].ball)
    Platformposition.append(date_list_9[i].platform)
    Bricks.append(date_list_9[i].bricks)

for i in range (0,len(date_list_10)):
    Frame.append(date_list_10[i].frame)
    Status.append(date_list_10[i].status)
    Ballposition.append(date_list_10[i].ball)
    Platformposition.append(date_list_10[i].platform)
    Bricks.append(date_list_10[i].bricks)

for i in range (0,len(date_list_11)):
    Frame.append(date_list_11[i].frame)
    Status.append(date_list_11[i].status)
    Ballposition.append(date_list_11[i].ball)
    Platformposition.append(date_list_11[i].platform)
    Bricks.append(date_list_11[i].bricks)

for i in range (0,len(date_list_12)):
    Frame.append(date_list_12[i].frame)
    Status.append(date_list_12[i].status)
    Ballposition.append(date_list_12[i].ball)
    Platformposition.append(date_list_12[i].platform)
    Bricks.append(date_list_12[i].bricks)

for i in range (0,len(date_list_13)):
    Frame.append(date_list_13[i].frame)
    Status.append(date_list_13[i].status)
    Ballposition.append(date_list_13[i].ball)
    Platformposition.append(date_list_13[i].platform)
    Bricks.append(date_list_13[i].bricks)
for i in range (0,len(date_list_14)):
    Frame.append(date_list_14[i].frame)
    Status.append(date_list_14[i].status)
    Ballposition.append(date_list_14[i].ball)
    Platformposition.append(date_list_14[i].platform)
    Bricks.append(date_list_14[i].bricks)
for i in range (0,len(date_list_15)):
    Frame.append(date_list_15[i].frame)
    Status.append(date_list_15[i].status)
    Ballposition.append(date_list_15[i].ball)
    Platformposition.append(date_list_15[i].platform)
    Bricks.append(date_list_15[i].bricks)
for i in range (0,len(date_list_16)):
    Frame.append(date_list_16[i].frame)
    Status.append(date_list_16[i].status)
    Ballposition.append(date_list_16[i].ball)
    Platformposition.append(date_list_16[i].platform)
    Bricks.append(date_list_16[i].bricks)
for i in range (0,len(date_list_17)):
    Frame.append(date_list_17[i].frame)
    Status.append(date_list_17[i].status)
    Ballposition.append(date_list_17[i].ball)
    Platformposition.append(date_list_17[i].platform)
    Bricks.append(date_list_17[i].bricks)
for i in range (0,len(date_list_18)):
    Frame.append(date_list_18[i].frame)
    Status.append(date_list_18[i].status)
    Ballposition.append(date_list_18[i].ball)
    Platformposition.append(date_list_18[i].platform)
    Bricks.append(date_list_18[i].bricks)
for i in range (0,len(date_list_18)):
    Frame.append(date_list_18[i].frame)
    Status.append(date_list_18[i].status)
    Ballposition.append(date_list_18[i].ball)
    Platformposition.append(date_list_18[i].platform)
    Bricks.append(date_list_18[i].bricks)
for i in range (0,len(date_list_19)):
    Frame.append(date_list_19[i].frame)
    Status.append(date_list_19[i].status)
    Ballposition.append(date_list_19[i].ball)
    Platformposition.append(date_list_19[i].platform)
    Bricks.append(date_list_19[i].bricks)
for i in range (0,len(date_list_20)):
    Frame.append(date_list_20[i].frame)
    Status.append(date_list_20[i].status)
    Ballposition.append(date_list_20[i].ball)
    Platformposition.append(date_list_20[i].platform)
    Bricks.append(date_list_20[i].bricks)    
for i in range (0,len(date_list_21)):
    Frame.append(date_list_21[i].frame)
    Status.append(date_list_21[i].status)
    Ballposition.append(date_list_21[i].ball)
    Platformposition.append(date_list_21[i].platform)
    Bricks.append(date_list_21[i].bricks)       
for i in range (0,len(date_list_22)):
    Frame.append(date_list_22[i].frame)
    Status.append(date_list_22[i].status)
    Ballposition.append(date_list_22[i].ball)
    Platformposition.append(date_list_22[i].platform)
    Bricks.append(date_list_22[i].bricks)   
for i in range (0,len(date_list_23)):
    Frame.append(date_list_23[i].frame)
    Status.append(date_list_23[i].status)
    Ballposition.append(date_list_23[i].ball)
    Platformposition.append(date_list_23[i].platform)
    Bricks.append(date_list_23[i].bricks)   
for i in range (0,len(date_list_24)):
    Frame.append(date_list_24[i].frame)
    Status.append(date_list_24[i].status)
    Ballposition.append(date_list_24[i].ball)
    Platformposition.append(date_list_24[i].platform)
    Bricks.append(date_list_24[i].bricks)   
for i in range (0,len(date_list_25)):
    Frame.append(date_list_25[i].frame)
    Status.append(date_list_25[i].status)
    Ballposition.append(date_list_25[i].ball)
    Platformposition.append(date_list_25[i].platform)
    Bricks.append(date_list_25[i].bricks)   
for i in range (0,len(date_list_26)):
    Frame.append(date_list_26[i].frame)
    Status.append(date_list_26[i].status)
    Ballposition.append(date_list_26[i].ball)
    Platformposition.append(date_list_26[i].platform)
    Bricks.append(date_list_26[i].bricks)   
for i in range (0,len(date_list_27)):
    Frame.append(date_list_27[i].frame)
    Status.append(date_list_27[i].status)
    Ballposition.append(date_list_27[i].ball)
    Platformposition.append(date_list_27[i].platform)
    Bricks.append(date_list_27[i].bricks)   
for i in range (0,len(date_list_28)):
    Frame.append(date_list_28[i].frame)
    Status.append(date_list_28[i].status)
    Ballposition.append(date_list_28[i].ball)
    Platformposition.append(date_list_28[i].platform)
    Bricks.append(date_list_28[i].bricks)       
#----------------------------------------------------------------------------------------------------------------------------
import numpy as np
PlatX = np.array(Platformposition)[:,0][:,np.newaxis]
PlatX_next = PlatX[1:,:]
instruct = (PlatX_next - PlatX[0:len(PlatX_next),0][:, np.newaxis])/5

BallX = np.array(Ballposition)[:,0][:,np.newaxis]
BallX_next = BallX[1:,:]
vx = (BallX_next - BallX[0:len(BallX_next),0][:,np.newaxis])

BallY = np.array(Ballposition)[:,1][:,np.newaxis]
BallY_next = BallY[1:,:]
vy = (BallY_next - BallY[0:len(BallY_next),0][:,np.newaxis])

Ballarray = np.array(Ballposition[:-1])
x = np.hstack((Ballarray , PlatX[0:-1,0][:,np.newaxis],vx,vy))

y = instruct

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=999)

#----------------------------------------------------------------------------------------------------------------------------
from sklearn.svm import SVR

svr = SVR(gamma=0.001,C = 1,epsilon = 0.1,kernel = 'rbf')

svr.fit(x_train,y_train)

ysvr_bef_scaler = svr.predict(x_test)

from sklearn.metrics import r2_score

R2 = r2_score(y_test,ysvr_bef_scaler)
print('R2 = ',R2)
#----------------------------------------------------------------------------------------------------------------------------
'''
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train_stdnorm = scaler.transform(x_train)
knn.fit(x_train_stdnorm ,y_train)
x_test_stdnorm = scaler.transform(x_test)
yknn_aft_scaler = knn.predict(x_test_stdnorm)
acc_knn_aft_scaler = accuracy_score(yknn_aft_scaler,y_test)
'''

#----------------------------------------------------------------------------------------------------------------------------
filename = "C:\\MLGame-master\\SVM.sav"
pickle.dump(svr , open(filename , 'wb'))
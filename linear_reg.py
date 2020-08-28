import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import matplotlib



def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
    plt.savefig('plot1reg.png')
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.savefig('pq.png')
    # function to show plot 
    
    

def main(x,y): 
    # observations 

    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb_0 = {} nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
  


 


#print(df2.head())
#print(len(df2))
df1 = pd.read_csv('/home/codersarts/Downloads/machine-learning-programming-assignments-coursera-andrew-ng-master/machine-learning-ex1/ex1/lin_reg/ex1data1.txt',sep = ',',header = None)
#df2 = pd.read_csv('ex1data2.txt',sep = ',',header = None)
 
x = np.array(df1[0]) 
y = np.array(df1[1])
main(x,y)

#Import libraries #%matplotlib inline
import  matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import tree
from  sklearn.ensemble import RandomForestClassifier
from  sklearn.tree import DecisionTreeRegressor
from  sklearn.ensemble import RandomForestRegressor
from  IPython.display import display
import statsmodels.api  as sm 
# Import make_regression method to generate artificial data samples
from  sklearn.datasets import make_regression
 
n_samples = 100 # Number of samples
n_features = 6  
n_informative = 3 # Number of informative features i.e. actual features which influence the  output 
X, y,coef = make_regression(n_samples=n_samples, n_features=n_features,  n_informative=n_informative, random_state=None, shuffle=False,noise=20,coef=True) 
#Make a data frame and create basic visualizations
df1 = pd.DataFrame(data=X,columns=['X'+str(i) for i in range(1,n_features+1)])
df2=pd.DataFrame(data=y,columns=['y'])
df=pd.concat([df1,df2],axis=1)
df.head(10)
display(df) 
#Scatter plots
with plt.style.context(('seaborn-dark')):
    for i,col in enumerate(df.columns[:-1]): 
        plt.figure(figsize=(6,4)) 
        plt.grid(True)  
        plt.xlabel('Feature:'+col,fontsize=12)  
        plt.ylabel('Output: y',fontsize=12)  
        plt.scatter(df[col],df['y'],c='red',s=50,alpha=0.6)  
        plt.show()
with plt.style.context(('fivethirtyeight')):
    for i,col in enumerate(df.columns[:-1]): 
        plt.figure(figsize=(6,4))  
        plt.grid(True)  
        plt.xlabel('Feature:'+col,fontsize=12)  
        plt.ylabel('Output: y',fontsize=12)  
        plt.hist(df[col],alpha=0.6,facecolor='g')  
        plt.show() 
tree_model = tree.DecisionTreeRegressor(max_depth=5,random_state=None)
tree_model.fit(X,y) 
DecisionTreeRegressor(criterion='mse', max_depth=5, max_features=1.0,  max_leaf_nodes=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, random_state=None, splitter='best') 
print("Relative importance of the features: ",tree_model.feature_importances_)
with  plt.style.context('dark_background'):
    plt.figure(figsize=(10,7))
    plt.grid(True)
    plt.yticks(range(n_features+1,1,- 1),df.columns[:-1],fontsize=20)
    plt.xlabel("Relative (normalized) importance of  parameters",fontsize=15)
    plt.ylabel("Features\n",fontsize=20)  
    plt.barh(range(n_features+1,1,-1),width=tree_model.feature_importances_,height=0.5)
    plt.show() 
print("Regression coefficient:",tree_model.score(X,y)) 
model = RandomForestRegressor(max_depth=5, random_state=None,max_features=1.0,max_leaf_nodes=5,n_estimators=100)
model.fit(X, y) 
RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=5,  max_features=1.0, max_leaf_nodes=5, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0,n_estimators=100, n_jobs=1, oob_score=False,random_state=None, verbose=0, warm_start=False) 
print("Relative importance of the features: ",model.feature_importances_)
with  plt.style.context('dark_background'): 
    plt.figure(figsize=(10,7))
    plt.grid(True)
    plt.yticks(range(n_features+1,1,- 1),df.columns[:-1],fontsize=20)
    plt.xlabel("Relative (normalized) importance of  parameters",fontsize=15)
    plt.ylabel("Features\n",fontsize=20)  
    plt.barh(range(n_features+1,1,-1),width=model.feature_importances_,height=0.5)
    plt.show()
print("Regression coefficient:",model.score(X,y)) 
Xs=sm.add_constant(X)
stat_model = sm.OLS(y,Xs)
stat_result = stat_model.fit() 
print(stat_result.summary()) 
rf_coef=np.array(coef)
stat_coef=np.array(stat_result.params[1:])
df_coef = pd.DataFrame(data=[rf_coef,stat_coef],columns=df.columns[:- 1],index=['True Regressors', 'OLS method estimation'])
df_coef
df_importance = pd.DataFrame(data=[model.feature_importances_,stat_result.tvalues[1:]/sum(stat_result.tvalues[1:])], columns=df.columns[:-1], index=['RF Regressor relative importance', 'OLS method normalized  tstatistic']) 
df_importance 

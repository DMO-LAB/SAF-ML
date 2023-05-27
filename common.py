import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway,ttest_ind
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

class utils():
    def __init__(self) -> None:
        pass

    def scatterplot(self,x,y,x_label,y_label,colors):
        slope, intercept = np.polyfit(x, y, 1)
        plt.grid(True)
        plt.scatter(x,y,c=colors,s=40.0,edgecolors='black')
        plt.plot(x, slope * np.array(x) + intercept, color='black',linewidth=1)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title( y_label+' vs '+x_label)
        plt.show()
    
    def get_info(self,x,y):
        t_statistic, p_value = ttest_ind(x, y)
        f_statistic, p_value = f_oneway(x, y)
        return {'p_value':p_value,'t_statistic':t_statistic,'f_statistic':f_statistic,'corrcof':np.corrcoef(x.flatten(),y.flatten())[0, 1]}

    def showAllPlot(self,properties,fuelpro,y,y_label,colors):
        for property in properties:
            myutils = utils()
            X = fuelpro[:,properties.index(property)]
            info = myutils.get_info(X.flatten(),y.flatten())
            print(info)
            myutils.scatterplot(X,y,x_label=property,y_label=y_label,colors=colors)

    def showCorrelation(self,fuelpro,properties):
        df_phy_data = pd.DataFrame(fuelpro, columns = list(properties))
        sns.heatmap(df_phy_data.corr().abs())

    def showFeatureImportance(self,y,fuelpro,properties,title):
        colors=['green','blue','purple','red','orange','grey','pink','lightgreen','chocolate','violet','magenta','teal','cyan']
        feature_imArray = np.array([])
        for i in range(500):
            rfc = RandomForestRegressor(n_estimators=100)
            rfc.fit(fuelpro,y.ravel())
            # Compute feature importance scores
            importances = rfc.feature_importances_
            if(i == 0):
                feature_imArray = importances.reshape(1,-1)
            else:
                feature_imArray = np.concatenate((feature_imArray,importances.reshape(1,-1)),axis=0)
 
        performance = np.average(feature_imArray,axis=0)
        error = np.std(feature_imArray,axis=0)

        feature_importance = pd.DataFrame(properties, columns = ["feature"])
        feature_importance["importance"] = performance
        feature_importance["error"] = error

        feature_importance = feature_importance.sort_values(by = ["importance"], ascending=True)
        ax = feature_importance.plot.barh(x='feature', y='importance',xerr=feature_importance["error"].to_numpy(),color=colors)
        ax.set_xlabel('feature importance')
        ax.set_title(title)
        plt.legend('', frameon=False)
        plt.show()


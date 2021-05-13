#%%


def predict_result(l):
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import StandardScaler
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    df = pd.read_csv("BTC\Bitcoin_dataset_updated.csv")
    df.drop("Date", axis=1, inplace=True)

    df.fillna(method="ffill", inplace=True)
    df.isnull().sum()

    y = df["BTC price [USD]"]
    X = df.drop("BTC price [USD]", axis=1)

    X = StandardScaler().fit_transform(X)

    regressor = DecisionTreeRegressor(random_state=0, max_depth=3)
    regressor.fit(X, y)
    return regressor.predict(np.array(l).reshape(1, -1))[0]

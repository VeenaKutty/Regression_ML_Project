
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_data(path):
    df = pd.read_csv(path)
    return df


def clean_data(df):
    df.replace("?", np.nan, inplace=True)
    df.dropna(inplace=True)

    for col in df.columns:
        try:
            df[col] = df[col].astype(float)
        except:
            pass

    return df


def encode_data(df):
    le = LabelEncoder()

    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    return df


def split_features_target(df, target="price"):
    X = df.drop(target, axis=1)
    y = df[target]
    return X, y


def scale_data(X_train, X_test):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled
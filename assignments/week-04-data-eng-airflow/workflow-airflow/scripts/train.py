from pathlib import Path

import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from joblib import dump

target = 'Weekly_Sales'
numeric_features = ['CPI', 'MarkDown1']
categorical_features = ['Dept', 'IsHoliday']

path = Path(__file__).parent.parent.resolve()
df = pd.read_csv(path.joinpath('dat/train-store1.csv'))
X, y = df.drop(columns=target), df[target]

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")), 
    ("scaler", MinMaxScaler())
])
categorical_transformer = OneHotEncoder(handle_unknown='ignore')
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", LinearRegression())
        ]
    )
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"X_train size {X_train.shape}, y_train size {y_train.shape}")
print(f"X_test size {X_test.shape}, y_test size {y_test.shape}")

model.fit(X_train, y_train)

print("model score: %.3f" % model.score(X_test, y_test))
model_path = path.joinpath("models/train-store1.joblib")
if not model_path.exists():
    model_path.parent.mkdir(parents=True, exist_ok=True)
dump(model, model_path) 

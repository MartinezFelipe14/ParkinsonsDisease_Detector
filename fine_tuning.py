<<<<<<< HEAD
from skopt import gp_minimize
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
import os

# Carregar base de dados
diretorio_atual = os.getcwd()

caminho_dataset = os.path.join(diretorio_atual, 'datasets', 'parkinsons.data')

df = pd.read_csv(caminho_dataset)

X = df.drop(['status', 'name', 'APQ', 'D2',
            'Fhi(Hz)', 'Flo(Hz)', 'Fo(Hz)',
             'PPQ', 'RAP', 'spread1', 'spread2'], axis=1)

y = df['status']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)


def treinar_modelo(params):
    learning_rate = params[0]
    min_child_weight = params[1]
    max_depth = params[2]
    colsample_bytree = params[3]
    gamma = params[4]
    scale_pos_weight = params[5]

    print(params, '\n')

    pipe = Pipeline(steps=[('StandardScaler', StandardScaler()),
                           ('MinMaxScaler', MinMaxScaler()),
                           ('XGBClassifier', XGBClassifier(learning_rate=learning_rate, min_child_weight=min_child_weight,
                                                           max_depth=max_depth, colsample_bytree=colsample_bytree,
                                                           gamma=gamma, scale_pos_weight=scale_pos_weight, n_estimators=50))])  # número de arvores é definido como fixo, no caso igual a 50

    pipe.fit(X_treino, y_treino)

    proba = pipe.predict_proba(X_teste)[:, 1]

    # multiplicado por -1 porque é preciso minimizar a negativa do auc não o próprio auc
    return -1 * roc_auc_score(y_teste, proba)


space = [(1e-3, 1, 'log-uniform'),  # learning_rate, log-uniform dá mais importância para números menores
         (1, 10),  # min_child_weight
         (3, 10),  # max_depth
         (0.5, 1.0),  # colsample_bytree
         (0, 5),  # gamma
         (1, 10)]  # scale_pos_weight

# resultado = dummy_minimize(treinar_modelo, space, random_state=1, verbose=1, n_calls=30)
# resultado.x


resultados_gp = gp_minimize(treinar_modelo, space,
                            verbose=1, n_calls=50, n_random_starts=10)

print(f'resultado: {resultados_gp.x}')
=======
from skopt import gp_minimize
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
import os

# Carregar base de dados
diretorio_atual = os.getcwd()

caminho_dataset = os.path.join(diretorio_atual, 'datasets', 'parkinsons.data')

df = pd.read_csv(caminho_dataset)

X = df.drop(['status', 'name', 'APQ', 'D2',
            'Fhi(Hz)', 'Flo(Hz)', 'Fo(Hz)',
             'PPQ', 'RAP', 'spread1', 'spread2'], axis=1)

y = df['status']

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)


def treinar_modelo(params):
    learning_rate = params[0]
    min_child_weight = params[1]
    max_depth = params[2]
    colsample_bytree = params[3]
    gamma = params[4]
    scale_pos_weight = params[5]

    print(params, '\n')

    pipe = Pipeline(steps=[('StandardScaler', StandardScaler()),
                           ('MinMaxScaler', MinMaxScaler()),
                           ('XGBClassifier', XGBClassifier(learning_rate=learning_rate, min_child_weight=min_child_weight,
                                                           max_depth=max_depth, colsample_bytree=colsample_bytree,
                                                           gamma=gamma, scale_pos_weight=scale_pos_weight, n_estimators=50))])  # número de arvores é definido como fixo, no caso igual a 50

    pipe.fit(X_treino, y_treino)

    proba = pipe.predict_proba(X_teste)[:, 1]

    # multiplicado por -1 porque é preciso minimizar a negativa do auc não o próprio auc
    return -1 * roc_auc_score(y_teste, proba)


space = [(1e-3, 1, 'log-uniform'),  # learning_rate, log-uniform dá mais importância para números menores
         (1, 10),  # min_child_weight
         (3, 10),  # max_depth
         (0.5, 1.0),  # colsample_bytree
         (0, 5),  # gamma
         (1, 10)]  # scale_pos_weight

# resultado = dummy_minimize(treinar_modelo, space, random_state=1, verbose=1, n_calls=30)
# resultado.x


resultados_gp = gp_minimize(treinar_modelo, space,
                            verbose=1, n_calls=50, n_random_starts=10)

print(f'resultado: {resultados_gp.x}')
>>>>>>> f9b07a9 (update gitignore)

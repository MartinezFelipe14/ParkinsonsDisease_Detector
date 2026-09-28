import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier


def preprocess(caminho_dataset):
    # carregar a base de dados e colocar na variável df
    df = pd.read_csv(caminho_dataset)

    # colocar as outras colunas para prever o y excluindo colunas que não tem no dataset final
    X = df.drop(['status', 'name', 'APQ', 'D2',
                'Fhi(Hz)', 'Flo(Hz)', 'Fo(Hz)',
                 'PPQ', 'RAP', 'spread1', 'spread2'], axis=1)

    # colocar a coluna a ser prevista em y
    y = df['status']

    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.2)

    # definir os processos a serem feitos nos dados
    pipe = Pipeline(steps=[('StandardScaler', StandardScaler()),
                           ('MinMaxScaler', MinMaxScaler()),
                           ('XGBClassifier', XGBClassifier(learning_rate=0.18740935969636607, min_child_weight=5, n_estimators=50,
                                                           max_depth=3, colsample_bytree=1.0, gamma=1.0, scale_pos_weight=7))])

    '''
    resultados da otimização de hiperparâmetros bayesiana com n_estimators=50:
    learning_rate, min_child_weight, max_depth, colsample_bytree,
    gamma, scale_pos_weight, n_estimators=50
    [0.18740935969636607, 5, 3, 1.0, 0, 7]
    '''

    return pipe, X_treino, X_teste, y_treino, y_teste


def preprocess_new_data(caminho_novo_dataset):

    novos_dados = pd.read_csv(caminho_novo_dataset)

    previsao_final = novos_dados[[
        'subject#', 'age', 'sex', 'test_time']]

    # tirar as informações não foram treinadas
    novos_dados = novos_dados.drop(
        ['subject#', 'age', 'sex', 'test_time', 'motor_UPDRS', 'total_UPDRS', 'Jitter:PPQ5',
            'Jitter:RAP', 'Shimmer:APQ11'], axis=1)

    return novos_dados, previsao_final

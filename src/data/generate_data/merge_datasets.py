# -*- coding: utf-8 -*-
"""
merge_datasets.py
Une EdgeServers + Users em um único dataset (sem Applications por enquanto).
"""

import pandas as pd
import core.constants as C
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def merge_logs():
    # Carregar CSVs
    df_user = pd.read_csv(C.USERS_CSV)
    df_edge = pd.read_csv(C.EDGE_SERVERS_CSV)

    # Ajustar colunas chave (garanta que existem no CSV gerado pelo EdgeSimPy)
    df_user.rename(columns={"ID": "user_id"}, inplace=True)
    df_edge.rename(columns={"ID": "server_id"}, inplace=True)

    # Merge simplificado só para juntar usuários e servidores
    # (aqui fazemos um "cartesian join" só para exemplo; depois Applications dará o vínculo real)
    merged = df_user.assign(key=1).merge(df_edge.assign(key=1), on="key").drop("key", axis=1)

    # Salvar dataset final
    output_file = os.path.join(C.DATA_DIR, "symfony_dataset_partial.csv")
    merged.to_csv(output_file, index=False, encoding="utf-8")

    print(f"✅ Dataset parcial salvo em {output_file}")
    print("🔎 Preview:")
    print(merged.head())

if __name__ == "__main__":
    merge_logs()

# -*- coding: utf-8 -*-
"""
constants.py
Arquivo central para armazenar constantes do Symphony Project.
"""

import os

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Sobe um nível para src
DATA_DIR = os.path.join(BASE_DIR, "data/csv")

# Garantir que o diretório de dados existe
os.makedirs(DATA_DIR, exist_ok=True)

# Arquivos de saída
EDGE_SERVERS_CSV = os.path.join(DATA_DIR, "edge_servers_log.csv")
USERS_CSV = os.path.join(DATA_DIR, "users_log.csv")
APPLICATIONS_CSV = os.path.join(DATA_DIR, "applications_log.csv")

# Parâmetros padrão de simulação
DEFAULT_TICK_DURATION = 1
DEFAULT_TICK_UNIT = "seconds"
DEFAULT_SIMULATION_STEPS = 20
DEFAULT_RESOURCE_MANAGEMENT_ALGORITHM = lambda parameters: None  # Placeholder
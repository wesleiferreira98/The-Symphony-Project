from edge_sim_py import *
import pandas as pd
import sys
import core.constants as C  # importa o módulo de constantes

# Criar simulador
simulator = Simulator(
    tick_duration=C.DEFAULT_TICK_DURATION,
    tick_unit=C.DEFAULT_TICK_UNIT,
    stopping_criterion=lambda model: model.schedule.steps >= C.DEFAULT_SIMULATION_STEPS,
    resource_management_algorithm=C.DEFAULT_RESOURCE_MANAGEMENT_ALGORITHM
)

# Inicializar topologia
simulator.initialize(
    input_file="https://raw.githubusercontent.com/EdgeSimPy/edgesimpy-tutorials/master/datasets/sample_dataset1.json"
)

# Executar simulação
simulator.run_model()
print("Keys disponíveis:", simulator.agent_metrics.keys())

# Salvar logs usando os caminhos centralizados
if "EdgeServer" in simulator.agent_metrics:
    pd.DataFrame(simulator.agent_metrics["EdgeServer"]).to_csv(C.EDGE_SERVERS_CSV, index=False, encoding="utf-8")

if "User" in simulator.agent_metrics:
    pd.DataFrame(simulator.agent_metrics["User"]).to_csv(C.USERS_CSV, index=False, encoding="utf-8")

if "Application" in simulator.agent_metrics:
    pd.DataFrame(simulator.agent_metrics["Application"]).to_csv(C.APPLICATIONS_CSV, index=False, encoding="utf-8")

print("✅ Logs salvos em:", C.DATA_DIR)

from core.buildHam import QHO
from core.encodeHam import h2zixy
from core.VQEHam import runVQE, Two_Qubit_HEA, Two_Qubit_UniversalAnsatz, Four_Qubit_HEA
import pandas as pd

def multiRuns(runs, H, ansatz, paramnums,fname):
    multires = []
    if ansatz == Two_Qubit_HEA or ansatz == Two_Qubit_UniversalAnsatz:
        save = H["II"]
        del(H["II"])
    elif ansatz == Four_Qubit_HEA:
        save = H["IIII"]
        del(H["IIII"])
    for i in range(runs):
        print("\n_____Multi-Run: Iteration "+str(i)+"_____\n")
        results = runVQE(H,ansatz,paramnums)
        multires.append([results[0] + save,results[1]])
    lowvals = [i[0] for i in multires]
    runtimes = [i[1] for i in multires]
    dict = {'Lowest Values':lowvals, 'Run Times (s)':runtimes}
    df = pd.DataFrame(dict)
    df.to_csv(fname+'.csv')

    return multires

check = multiRuns(1,h2zixy(QHO(4,"pos")),Two_Qubit_HEA,8,"genData/trialrun")
from causallearn.utils.TXT2GeneralGraph import txt2generalgraph
import causallearn.graph.AdjacencyConfusion as AdjConf
import causallearn.graph.ArrowConfusion as ArrConf

import tetrad_cmd_algs as tc

t = txt2generalgraph("test_files/graph20.6.6000.txt")
path = "test_files/data20.6.6000.txt"

g = tc.pcmax(path, 0.05)
# g = tc.fges(path, 2)
# g = tc.grasp(path, 2)
# g = tc.boss(path, 2)
# g = tc.rges(path, 2)
print(g)

ACpc = AdjConf.AdjacencyConfusion(t, g)
ArrCpc = ArrConf.ArrowConfusion(t, g)

print("AP", ACpc.get_adj_precision())
print("AR", ACpc.get_adj_recall())
print("AHP", ArrCpc.get_arrows_precision())
print("AHPCE", ArrCpc.get_arrows_precision_ce())
print("AHR", ArrCpc.get_arrows_recall())
print("AHRCE", ArrCpc.get_arrows_recall_ce())

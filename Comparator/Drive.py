import sys
# from pyemd import emd
from gensim.models.keyedvectors import KeyedVectors
import Tools

model = sys.argv[1]

word_vectors = KeyedVectors.load_word2vec_format(model)
word_vectors.init_sims(replace=True)

bug_r_files = [
    "bug_reports/bugreport0",
    "bug_reports/bugreport1",
    "bug_reports/bugreport2" # ,
    # "bug_reports/bugreport3",
    # "bug_reports/bugreport4"
]

bug_report_step_arr = []

for filename in bug_r_files:
    report_arr = []
    with open(filename , 'r') as file:
        for step in file.readlines():
            report_arr.append(Tools.preprocess(step))
    bug_report_step_arr.append(report_arr)

# similarity = word_vectors.wmdistance(bug_report_step_arr[0][0], bug_report_step_arr[2][0])
# print("{:.4f}".format(similarity))
# similarity = word_vectors.wmdistance(bug_report_step_arr[0][1], bug_report_step_arr[2][1])
# print("{:.4f}".format(similarity))

sim_arr_map = []

for bug_report_i in range(len(bug_report_step_arr) - 1):
    i_arr = []

    for step_j in bug_report_step_arr[bug_report_i]:
        j_arr = []

        for other_report_k in range(bug_report_i + 1, len(bug_report_step_arr)):
            k_arr = []

            for other_step_l in bug_report_step_arr[other_report_k]:
                similarity = word_vectors.wmdistance(step_j, other_step_l)
                k_arr.append(similarity)

            j_arr.append(k_arr)

        i_arr.append(j_arr)

    sim_arr_map.append(i_arr)

print(sim_arr_map)
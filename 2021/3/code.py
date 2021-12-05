import pandas as pd

dt = pd.read_csv("2021/3/data.csv", header=None, names = ["binary"], dtype = {"binary":str})
# dt = pd.read_csv("2021/3/data_sample.csv", header=None, names = ["binary"], dtype = {"binary":str})
ncols = len(dt["binary"][0])
bits = dt['binary'].str.split('', ncols, expand=True)[[x for x in range(1, ncols + 1)]]
bits.columns = ["c" + str(col_num) for col_num in bits.columns]

# ---- part 1 ----
gamma_binary = "".join([n for n in bits.mode().iloc[0]])
gamma_decimal = int(gamma_binary, 2)

def flip(x):
    if str(x) == "1":
        return "0"
    else:
        return "1"

epsilon_binary = "".join([flip(x) for x in str(gamma_binary)])
epsilon_decimal = int(str(epsilon_binary), 2)

gamma_decimal * epsilon_decimal 

# ---- part 2 ----
def filter_common(col_name, bits_filter, least=False):
    if bits_filter.shape[0] == 1:
        return bits_filter

    most_common = bits_filter[col_name].mode()
    
    if most_common.shape[0] > 1: # there is a tie
        most_common = "1"
    else:
        most_common = str(most_common[0])    
    
    if least:
        most_common = flip(most_common)
    
    is_common = list([x == most_common for x in bits_filter[col_name]])
    return bits_filter[is_common].reset_index(drop=True)    

# o2_generator
# keep numbers that match the most common, keep 1s if 0 and 1 are tied
col_names_todo = ["c" + str(x) for x in range(1, 13)]
for col_name in col_names_todo:
    o2_generator = filter_common(col_name, o2_generator)

o2_generator_binary = "".join([x for x in o2_generator.loc[0]])
o2_generator_decimal = int(str(o2_generator_binary), 2)

# co2_scrubber
# keep numbers that match the least common, keep 0s if 0 and 1 are tied
for col_name in col_names_todo:
    co2_scrubber = filter_common(col_name, co2_scrubber, least=True)

co2_scrubber_binary = "".join([x for x in co2_scrubber.loc[0]])
co2_scrubber_decimal = int(str(co2_scrubber_binary), 2)

# life_support
o2_generator_decimal * co2_scrubber_decimal

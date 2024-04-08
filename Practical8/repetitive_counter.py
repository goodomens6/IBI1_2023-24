import re
seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
first_form=re.findall(r'GTGTGT',seq)
second_form=re.findall(r'GTCTGT',seq)
print(len(first_form)+len(second_form))
with open('SLC6A4_HUMAN.fa', 'rt') as file_human:
    lines = file_human.readlines()
    human = "".join(lines[1:])
with open('SLC6A4_MOUSE.fa', 'rt') as file_mouse:
    lines = file_mouse.readlines()
    mouse = "".join(lines[1:])
with open('SLC6A4_RAT.fa', 'rt') as file_rat:
    lines = file_rat.readlines()
    rat = "".join(lines[1:])

with open('BLOSUM62.txt', 'rt') as file:
    lines = file.readlines()
amino_acids = lines[0].strip().split()
BLOSUM62 = {acid: {} for acid in amino_acids}
for i, line in enumerate(lines[1:], start=1):
    scores = line.strip().split()
    key = scores[0]
    for j, score in enumerate(scores[1:], start=1):
        BLOSUM62[amino_acids[j-1]][key] = int(scores[j])

def compare(seq1,seq2):
    score = 0
    aligned_length = 0
    for a, b in zip(seq1, seq2):
        if a in BLOSUM62 and b in BLOSUM62[a]:  # 确保氨基酸在BLOSUM62矩阵中
            score += BLOSUM62[a][b]
            aligned_length += 1
    if aligned_length > 0:
        average_score = score / aligned_length
    else:
        average_score = 0
    return average_score

def identical(seq1,seq2):
    min_length = min(len(seq1), len(seq2))
    seq1_changed = seq1[:min_length]
    seq2_changed= seq2[:min_length]
    identical_count=0
    for a, b in zip(seq1_changed, seq2_changed):
        if a == b:
            identical_count += 1        
    percent=str(identical_count/min_length*100)+"%"
    return percent

human_mouse1=compare(human,mouse)
human_rat1=compare(human,rat)
mouse_rat1=compare(mouse,rat)

human_mouse2=identical(human,mouse)
human_rat2=identical(human,rat)
mouse_rat2=identical(mouse,rat)

print("Alignment score between human sequence and mouse sequence:",human_mouse1)
print("Alignment score between human sequence and rat sequence:",human_rat1)
print("Alignment score between mouse sequence and rat sequence:",mouse_rat1)

print("Percentage of identical amino acid between human sequence and mouse sequence:",human_mouse2)
print("Percentage of identical amino acid between human sequence and rat sequence:",human_rat2)

# Mouse sequence and rat sequence are mostly related
# Mouse is a better model organism for human
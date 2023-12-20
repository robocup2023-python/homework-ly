file = open('codon.txt','r')
fileContent = file.readlines()
d = {}
for i in range(1,len(fileContent)):
    fc = fileContent[i].rstrip('\n')
    fc = fc.split(' ')
    d[fc[0]] = fc[1]
def transcript(dna:str) ->str:
     mrna = ''
     for i in dna:
        if(i=='A'):
            mrna = mrna + 'U'
        elif(i=='T'):
            mrna = mrna + 'A'
        elif(i=='C'):
            mrna = mrna + 'G'
        elif(i=='G'):
            mrna = mrna + 'C'
        else:
            raise TypeError('')
        return mrna
def translate(dna:str)->str:
    aa = ''
    mrna = transcript(dna)
    n = mrna.find('AUG')
    m = min(mrna.find('UAA'),mrna.find('UAG'),mrna.find('UGA'))
    if(n==-1):
        return ''
    while(n+2<m):
        aa = aa + d[mrna[n]+mrna[n+1]+mrna[n+2]]
        n += 3
    return aa
file = open('seq.fa','r')
name = ''
content = ''
seq_dict = {}
f = file.readlines()
for l in f:
    l = l.strip('\n')
    if(l.startswith('>')):
        l = l.strip('>')
        name = l
    else:
        content = l
        seq_dict[name] = content
protein_dict = {}
for i in seq_dict:
    protein_dict[i] = translate(seq_dict[i])
print(protein_dict)
#2019/04/08
#Yuki Tsushima
#tsushima@bi.c.titech.ac.jp

import sys

def decode(text, offset):
    length = len(text)
    #if too short
    if length < offset + 3:
        return ''
    peptide = ''
    CODON = {'TTT':'Phe', 'TTC':'Phe', 'TTA':'Leu', 'TTG':'Leu',\
             'TCT':'Ser', 'TCC':'Ser', 'TCA':'Ser', 'TCG':'Ser',\
             'TAT':'Tyr', 'TAC':'Tyr', 'TAA':'_'  , 'TAG':'_'  ,\
             'TGT':'Cys', 'TGC':'Cys', 'TGA':'_'  , 'TGG':'Trp',\
             'CTT':'Leu', 'CTC':'Leu', 'CTA':'Leu', 'CTG':'Leu',\
             'CCT':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro',\
             'CAT':'His', 'CAC':'His', 'CAA':'Gln', 'CAG':'Gln',\
             'CGT':'Arg', 'CGC':'Arg', 'CGA':'Arg', 'CGG':'Arg',\
             'ATT':'Ile', 'ATC':'Ile', 'ATA':'Ile', 'ATG':'Met',\
             'ACT':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr',\
             'AAT':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys',\
             'AGT':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg',\
             'GTT':'Val', 'GTC':'Val', 'GTA':'Val', 'GTG':'Val',\
             'GCT':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala',\
             'GAT':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu',\
             'GGT':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly'}
    start = offset
    end = start + 3
    try:
        #Skip to Met
        while end <= length:
            if CODON[text[start:end]] == 'Met':
                break
            start = end
            end = start + 3
        #Decode
        while end <= length:
            peptide = peptide + ' ' + CODON[text[start:end]]
            if peptide[len(peptide)-1] == '_':
                break
            start = end
            end = start + 3
        return peptide.strip()
    except (KeyError):
        sys.stderr.write('Unknown CODON Error\n')
        return ''

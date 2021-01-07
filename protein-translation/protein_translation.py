import re

code = {'AUG': 'Methionine',
 'UUU': 'Phenylalanine',
 'UUC': 'Phenylalanine',
 'UUA': 'Leucine',
 'UUG': 'Leucine',
 'UCU': 'Serine',
 'UCC': 'Serine',
 'UCA': 'Serine',
 'UCG': 'Serine',
 'UAU': 'Tyrosine',
 'UAC': 'Tyrosine',
 'UGU': 'Cysteine',
 'UGC': 'Cysteine',
 'UGG': 'Tryptophan',
 'UAA': 'STOP',
 'UAG': 'STOP',
 'UGA': 'STOP'}


def proteins(strand):
    proteinsList = []
    codons = re.findall('...',strand)
    for codon in codons:
        protein = code.get(codon)
        if not protein or protein == 'STOP':
            return proteinsList
        else:
            proteinsList.append(protein)

    return proteinsList

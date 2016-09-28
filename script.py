from Bio.Seq import Seq
from Bio.Data import CodonTable
from Bio.Alphabet import generic_dna
import argparse


def snp_away(dna, codons):
    snp = False
    for codon in codons:
        score = 0
        for num, nuc in enumerate(dna):
            if nuc == codon[num]:
                score += 1

        if score == 2:
            snp = True
        if score == 3:
            return False

    return snp


def highlight_residues(amino_acid, sequence):
    # get amino acid codon table
    standard_table = CodonTable.unambiguous_dna_by_name["Standard"]

    # find codons for input amino acid
    codons = []
    for key, value in standard_table.forward_table.iteritems():
        if value == amino_acid:
            codons.append(key)

    dna = Seq(sequence.read().strip(), generic_dna)

    # keep track of which residues are one nucleotide away
    highlighted = []
    for i in range(0, len(dna), 3):
        if len(dna[i:i+3]) == 3:
            if snp_away((dna[i:i+3]).upper(), codons):
                highlighted.append(i/3)

    # translate and mark amino acids
    prot = str(dna.translate())

    with open('out.txt', 'w') as outfile:
        for num, p in enumerate(prot):
            if num in highlighted:
                outfile.write("\'%s\'" % p)
            else:
                outfile.write(p)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find residues that are one SNP away from input amino acid.')
    parser.add_argument('sequence', type=file, help='Path to DNA sequence')
    parser.add_argument('amino_acid', help="One letter code for amino acid")
    # parser.add_argument('frame', type=int, help="Reading frame (1,2, or 3)")
    args = parser.parse_args()

    highlight_residues(**vars(args))

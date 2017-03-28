from __future__ import print_function
from Bio import SeqIO
from Bio.Data import CodonTable
import argparse


def snp_away(dna, codons):
    """ determines if codon is one SNP away from amino acid sequence """

    snp = False
    # ignore if codon has the same sequence as the amino acid
    if dna in codons:
        return False

    # score codon based on number of identical bases
    for codon in codons:
        score = 0
        for num, nuc in enumerate(dna):
            if nuc == codon[num]:
                score += 1

        # 2 identical bases means codon is one mutation away
        if score == 2:
            snp = True

    return snp


def highlight_residues(amino_acid, sequence):
    """ prints translated residues """

    # get amino acid codon table
    standard_table = CodonTable.unambiguous_dna_by_name["Standard"]

    # build codon list for input amino acid
    codons = []
    for key, value in standard_table.forward_table.items():
        if value == amino_acid:
            codons.append(key)

    # read in fasta file
    dna = SeqIO.read(sequence, 'fasta').seq

    # digest dna three bases at a time
    for i in range(0, len(dna), 3):
        current_nts = dna[i:i + 3]
        current_aas = str(current_nts.translate())

        # check if bases are one mutation away from input amino acid
        if snp_away(current_nts.upper(), codons):
            print("'" + current_aas.upper() + "'", end=" ")
        else:
            print(current_aas.upper(), end=" ")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find residues that are one SNP away from input amino acid.')
    parser.add_argument('sequence', type=argparse.FileType('r'), help='Path to DNA sequence')
    parser.add_argument('amino_acid', help='One letter code for amino acid')
    # TODO: reading frame specification
    args = parser.parse_args()

    highlight_residues(**vars(args))

from Bio import SeqIO
from Bio.Data import CodonTable
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

    dna = SeqIO.read(sequence, 'fasta').seq

    for i in range(0, len(dna), 3):
        current_nts = dna[i:i+3]
        current_aas = str(current_nts.translate())

        if snp_away(current_nts.upper(), codons):
            print current_aas.upper(),
        else:
            print current_aas,

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find residues that are one SNP away from input amino acid.')
    parser.add_argument('sequence', type=file, help='Path to DNA sequence')
    parser.add_argument('amino_acid', help="One letter code for amino acid")
    # parser.add_argument('frame', type=int, help="Reading frame (1,2, or 3)")
    args = parser.parse_args()

    highlight_residues(**vars(args))

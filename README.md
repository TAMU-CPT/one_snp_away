# One SNP Away [![Build Status](https://travis-ci.org/TAMU-CPT/one_snp_away.svg?branch=master)](https://travis-ci.org/TAMU-CPT/one_snp_away)

Given a FASTA sequence and a one letter amino acid code, this tool will output the translated sequence
and denote the residues that are one single nucleotide polymorphism (SNP) away from the 
input amino acid. This tool is available on Galaxy, but may also be run locally from the 
command line.

## Requirements
- Python 2.7, 3.3, 3.4, 3.5
- [biopython] (http://biopython.org/wiki/Biopython)

## Running in Galaxy
// provide link for galaxy

## Local installation
#### First, clone the repository and enter the directory:
```console
$ git clone git@github.com:TAMU-CPT/one_snp_away.git
$ cd one_snp_away
```
#### Install biopython
```console
$ pip install biopython
```
#### Run the script with the path to the FASTA file and a one letter amino acid code:
```console
$ python script.py path/to/fasta.fa P > output.txt
```
The example above was run with proline (P), and the output will appear in the file output.txt

#### Output:
The residues that are one SNP away from the input amino acid will be surrounded by single quotes.

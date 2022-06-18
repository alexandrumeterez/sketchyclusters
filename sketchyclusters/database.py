from Bio import SeqIO

def load_fasta(fasta_file):
    fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
    return fasta_sequences

print(next(load_fasta("/home/alex/data/uniprot22_reviewed/uniprot_sprot.fasta")))

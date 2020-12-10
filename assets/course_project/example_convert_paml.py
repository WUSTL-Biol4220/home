from Bio import SeqIO
from Bio.Data import CodonTable
# get codon table
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
# get stop codons
stop = standard_table.stop_codons
# get input filname
infn = 'all_E.fasta'
# get output filename
outfn = 'all_E.paml'
# create dictionary of sequences from input
d = SeqIO.to_dict(SeqIO.parse(infn,'fasta'))
# get number of sequences
n_seq = len(d)
# get number of sites
n_sites = len( d[next(iter(d))] )
# write phylip header ('n_seq n_sites')
s = str(n_seq) + ' ' + str(n_sites) + '\n'
# print phylip sequence entries
for k,v in d.items():
    # empty sequence content to populat
    seq = ''
    # get codons
    c1 = str(v.seq[0::3])
    c2 = str(v.seq[1::3])
    c3 = str(v.seq[2::3])
    # get num codons
    n_codons = min([len(c1), len(c2), len(c3)])
    # loop over codons
    for i in range(n_codons):
        # build each codon
        c123 = c1[i]+c2[i]+c3[i]
        # mask stop codons
        if c123 in stop:
            c123 = 'NNN'
        # concatenate codons into seq
        seq += c123
    # save sequence id + content
    s += k[:30] + '  ' + seq + '\n'

# open output file
outf = open(outfn, 'w')
# write output
outf.write(s)
# close output file
outf.close()

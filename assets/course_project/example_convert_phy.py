from Bio import SeqIO

# get input filname
infn = 'all_E.fasta'
# get output filename
outfn = 'all_E.phy'
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
    s += k[:30] + '  ' + str(v.seq) + '\n'

# open output file
outf = open(outfn, 'w')
# write output
outf.write(s)
# close output file
outf.close()

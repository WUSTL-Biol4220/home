# Lab 07

*Lab 07 GitHub Classroom link:* to be provided

This lab will focus on retrieving fasta formatted sequences from GenBank, one of NCBI's Entrez databases. These techniques are useful when you need to generate a dataset for a set of organisms and genes. Although these scripts will only download nucleotide sequence information, the scripts could easily be adapted to compile different kinds of datasets (e.g. amino acid sequences, gene annotation features).

The major components of this lab are:
1. BLAST
2. Basic uses for EDirect
3. Scripting with EDirect

---

## 1. BLAST

This section will demonstrate how to use BLAST (Basic Local Alignment Search Tool). The BLAST is often the first tool researchers use to identify *what* a sequence is and what it does. For example: do any known genes have similar content to this anonymous sequence? what is the expected function of this sequence? and, in what species do we find this gene?  To provide information that can help answer these types of questions, BLAST compares a query sequence to a database of target sequences, computes a BLAST score to assess how well the query and matches to each possible target sequence, and then returns those target sequences with the highest BLAST scores (sometimes called 'hits'). BLAST hits report the identities of matched sequences, the match scores, the significance scores, and so forth.

Most researchers use NCBI's online interface to submit BLAST queries against GenBank records (https://blast.ncbi.nlm.nih.gov/Blast.cgi). BLAST is also available as a [command line tool](https://www.ncbi.nlm.nih.gov/books/NBK279690/), which is useful for scripting. However, the command line tool requires the local installation of a (large!) GenBank database to be used effectively. That being said, we'll use the web tool today.

Now for a problem. Suppose one of your more mischevious friends gives you a fasta file that they allege contains a DNA sequence from their talking pet dinosaur. Could it be true!?

Print the content of your `dino_dna.fasta` to stdout, and then copy the printed text in your terminal to your clipboard. Next open the [BLAST website](https://blast.ncbi.nlm.nih.gov/Blast.cgi) and select the "Nucleotide BLAST" tool. Paste your text into the field entitled "Enter Query Sequence". At the bottom of the page, click "BLAST".

NCBI will then tell you that your BLAST search is underway (it normally takes 10-30 seconds to complete).


---

## 2. Basic uses for EDirect

The EDirect suite contains many useful Unix command-line tools, some of which we'll explore here. Visit the EDirect web page for the [EDirect Unix utilities](https://www.ncbi.nlm.nih.gov/books/NBK179288/) to learn more about the general uses for the tool suite. The [EDirect Examples](https://www.ncbi.nlm.nih.gov/books/NBK179288/#_chapter6_Examples_) section contains some especially useful practical techniques. EDirect commands do not have man-pages (`man`), but you can learn more about each command by calling it with the `--help` flag.

```console
$ esearch --help | head
esearch 13.9

Query Specification

  -db          Database name
  -query       Query string

Document Order

  -sort        Result presentation order
```

The `esearch` command is used to search different NCBI databases. The `-db` option is used to target a database, and the `-query` is used to design a query string. For example:

```console
~$ esearch -db pubmed -query "Viburnum clemensiae"
<ENTREZ_DIRECT>
  <Db>nucleotide</Db>
  <WebEnv>MCID_5f778aa176179800fc1285f5</WebEnv>
  <QueryKey>1</QueryKey>
  <Count>84</Count>
  <Step>1</Step>
</ENTREZ_DIRECT>
```

The output is an XML object that contains information about the search request against the `nucleotide` database. Although this lab will only use the `nucleotide` database, the full list of databases is printed with the command `einfo -dbs`.

Although we now have the search text, no data has been *fetched* from the `nucleotide` database yet. By piping our `esearch` output into the `efetch` command, we can download the records associated with the query on the target databse. Using `efetch -format fasta` will cause the program to print the fetched sequence data to the screen (stdout) in fasta format.

```console
$ esearch -db nucleotide -query "Viburnum clemensiae" |  efetch -format fasta > sequences.fasta
$ head -n5 sequences.fasta
>KJ796120.1 Viburnum clemensae voucher PW Sweeney et al. 2142 RNA polymerase beta' subunit (rpoC2) gene, partial cds; chloroplast
ATGGAGGTACTTATGGCAGAACGGGCCAATCTGGTCTTTCACAATAAAGTGATAGACGGAACTGCCATGA
AACGACTTATTAGTAGATTAATCGATCACTTCGGAATGGCATATACATCACACATCCTGGATCAAGTAAA
GACTCTGGGTTTCCAACAAGCTACTGCTACATCTATTTCATTAGGAATTGATGATCTTTTAACAATACCT
TCTAAGAGATGGCTAGTTCAAGATGCTGAACAACAAAGTTTGATTTTGGAAAAACACCATCATTATGGGA
```

What command would you use to learn how many sequences were written to `sequences.fasta`? What command would tell you lines it contains?

Another useful format to fetch is the GenBank (`gb`) format, which we saw in the lecture slides. This format contains various metadata relating to the accession. Here, we'll use the `-stop 1` option with `efetch` so we only fetch one record.

```console
$ esearch -db nucleotide -query "Viburnum clemensiae" |  efetch -format gb -stop 1 | head -n10
LOCUS       KJ796120                4152 bp    DNA     linear   PLN 16-DEC-2016
DEFINITION  Viburnum clemensae voucher PW Sweeney et al. 2142 RNA polymerase
            beta' subunit (rpoC2) gene, partial cds; chloroplast.
ACCESSION   KJ796120
VERSION     KJ796120.1
KEYWORDS    .
SOURCE      chloroplast Viburnum clemensae
  ORGANISM  Viburnum clemensae
            Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
            Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae;
```

Each database supports its own set of specialized search terms, which allow users to refine the search terms in their `esearch` query. For example, to only return records on the `nucleotide` database that correspond to both the `rbcl` gene *and* the organism `Viburnum clemensiae`, use the following command 

```console
$ esearch -db nucleotide -query "rbcL [GENE] AND Viburnum clemensiae [ORGN]" | efetch -format fasta | head -n5
>HQ591714.1 Viburnum clemensae isolate B11781 ribulose 1,5-bisphosphate carboxylase (rbcL) gene, partial cds; chloroplast
AAAGATACTGATATCTTGGCAGCATTCCGAGTAACTCCTCAACCTGGAGTTCCACCTGAAGAAGCAGGGG
CCGCGGTAGCTGCCGAATCTTCTACTGGTACATGGACAACTGTGTGGACTGATGGACTTACCAACCTTGA
TCGTTACAAAGGGCGATGCTACCACATTGAGCCCGTTGCTGGAGAAGAAAGTCAATTTATTGCTTATGTA
GCTTACCCATTAGACCTTTTTGAAGAAGGTTCTGTTACTAACATGTTGACTTCCATTGTGGGTAATGTAT
```

Note that search terms are indicated by reserved keywords in all-caps and in square brackets. Combinations of search terms can be constructed using `NOT`, `AND`, and `OR` operators, along with parentheses `()` to assert the order of operations. For example: `"alcohol dehydrogenase [PROT] NOT (bacteria [ORGN] OR fungi [ORGN])"`
Other search terms supported by the `nucleotide` database:
```
  [ACCN]    Accession       [MLWT]    Molecular Weight
  [ALL]     All Fields      [ORGN]    Organism
  [AUTH]    Author          [PACC]    Primary Accession
  [GPRJ]    BioProject      [PROP]    Properties
  [BIOS]    BioSample       [PROT]    Protein Name
  [ECNO]    EC/RN Number    [SQID]    SeqID String
  [FKEY]    Feature key     [SLEN]    Sequence Length
  [FILT]    Filter          [SUBS]    Substance Name
  [GENE]    Gene Name       [WORD]    Text Word
  [JOUR]    Journal         [TITL]    Title
  [KYWD]    Keyword         [UID]     UID
```

To download the five most recently modified matches, you can supply the `-sort "Date Modified"` option to the `esearch` command and `-stop 5` option to `efetch`

```console
$  esearch -db nucleotide -query "Viburnum clemensiae" -sort "Date Modified" |  efetch -format fasta -stop 5
```

Providing the accession in the `esearch` query string will match that lone record.

```console
$ esearch -db nucleotide -query "AY596878" | efetch -format fasta
```

Note that an unmatched search query will identify 0 records. Fetching against a search with 0 matches will return no text.
```console
$ esearch -db nucleotide -query "Tyrannosaurus rex"
<ENTREZ_DIRECT>
  <Db>nucleotide</Db>
  <WebEnv>MCID_5f779558ae9e2c11ab7040b6</WebEnv>
  <QueryKey>1</QueryKey>
  <Count>0</Count>
  <Step>1</Step>
</ENTREZ_DIRECT>
$ esearch -db nucleotide -query "Tyrannosaurus rex" | efetch -format fasta
$
```

Although we've only explored a tiny fraction of what the EDirect utilities can do, this brief overview should provide enough background to complete the lab exercises below.

---

## 3. Scripting with EDirect

In this part of the lab, we will write scripts to download sequences from GenBank that match search criteria for species name, gene name, and sequence length. When completing this lab, you might consider what types of datasets you've needed to compile in your research experiences:
- What criteria or search patterns would be needed to obtain all of the sequences you *did* want, and none of the sequences you *did not* want?
- What features could a computer recognize to distinguish the targetted sequences from the irrelevant sequences?
- How sensitive would any analyses that use the collected sequences be if that dataset was missing some targetted sequences and/or included some off-target sequences?

Solving each problem will involve writing a shell script that makes use of for-loops, if-statements, text-processing, and the newly learned EDirect commands. Solutions may involve reading files line-by-line, which can be done with the following for-loop syntax

```
IFS=$'\n'                 # set the internal file separator as
                          # the newline while running this script
for LINE in `cat $FILE`;  # loop over \n-separated words from cat
do                        # open for-loop
  echo $LINE              # do something with each word
done                      # close for-loop
```

**Problem 1.** Write a shell script called `find_accession.sh` to retrieve a DNA sequence for a provided species name (first argument) and gene name (second argument) from Entrez using EDirect tools. A third optional argument in the format `x:y` may be provided to filter the `esearch` results to only match against accessions with a minimum length of `x` and a maximum length of `y`. This can be done by modifying the `esearch` query string to include the `[SLEN]` search criterion. Retrieve accession number and the sequence length the most recently modified GenBank accession.

The script should return these results when called with these arguments:
```console
$ ./find_accession.sh 'Viburnum rufidulum' 'rbcL'
Viburnum rufidulum,rbcL,KY627132,557
$ ./find_accession.sh 'Viburnum rufidulum' 'rbcL' '1300:1400'
Viburnum rufidulum,rbcL,KJ773975,1323
```

**Problem 2.** Write a second script called `fetch_accessions.sh` that downloads and organizes sequences when provided a file containing species names (argument 1) and a file with gene names (argument 2). The species file simply contains a list of species, one-per-row. 

```console
$ cat my_species.txt
Viburnum clemensiae
Viburnum dentatum
Viburnum rufidulum
```

The gene file is in .csv format, where the first column gives the gene name and the second column gives the expected sequence length (in the format `x:y` to be used with `[SLEN]` as in Problem 1). If the entry in the second column is left empty, that gene will not be filtered by sequence length during the search.

```console
$ cat my_genes.txt
rbcL,1300:1400
matK,
```

By default, the script will store fasta files in the local directory (`./`). Alternatively, the user may provide a directory (argument 3) to identify where the sequence files will be organized. (The command `mkdir -p` will create the target directory, if it does not already exist.)

You can either design this script to use the script from Problem 1 or write a new standalone script. Upon downloading a file, the script should save the output as `<directory_name>/<species>_<gene>_<accession>.fasta`. The script should only download a given accession *if* a file corresponding to that accession does not already exist in the target directory. This feature would be useful to prevent unnecessarily re-downloading large numbers of genomes.

Running the script using the above `my_species.txt` and `my_genes.txt` files as input will download the following fasta files
```console
$ ./fetch_accessions.sh my_species.txt my_genes.txt files
$ ls files
Viburnum_clemensiae_matK_HQ591569.fasta  Viburnum_dentatum_matK_KJ773225.fasta  Viburnum_rufidulum_matK_MH551948.fasta
Viburnum_clemensiae_rbcL_HQ591714.fasta  Viburnum_dentatum_rbcL_KJ773973.fasta  Viburnum_rufidulum_rbcL_KJ773975.fasta
$ wc files/*.fasta
  12   23  841 files/Viburnum_clemensiae_matK_HQ591569.fasta
  21   33 1474 files/Viburnum_clemensiae_rbcL_HQ591714.fasta
  11   20  740 files/Viburnum_dentatum_matK_KJ773225.fasta
  20   31 1468 files/Viburnum_dentatum_rbcL_KJ773973.fasta
  12   24  859 files/Viburnum_rufidulum_matK_MH551948.fasta
  20   31 1473 files/Viburnum_rufidulum_rbcL_KJ773975.fasta
  96  162 6855 total
```

Now run your script against a set of species and genes that you find personally interesting! One way to find new genes is using BLAST (first section).

---

To submit your assignment, please commit and push the following files to your repository:
```
find_accession.sh        # from problem 1
fetch_accessions.sh      # from problem 2
files/*.fasta            # the output from problem 2
history.txt              # redirected from `history` command
```

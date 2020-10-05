# Lab 04A

*Lab 04A GitHub Classroom link:* https://classroom.github.com/a/6f9RSL4X

This lab will focus on retrieving fasta formatted sequences from GenBank, one of NCBI's Entrez databases. These techniques are useful when you need to generate a dataset for a set of organisms and genes. Although these scripts will only download nucleotide sequence information, the scripts could easily be adapted to compile different kinds of datasets (e.g. amino acid sequences, gene annotation features).

The major components of this lab are:
1. Install Entrez Direct on VM
2. Basic uses for EDirect
3. Scripting with EDirect

---


## 1. Install Entrez Direct on VM

To complete this lab, you will need to install Entrez Direct (EDirect) command-line tools to query and access NCBI's Entrez databases, including GenBank. We will use the `curl` command to download an installation script from NCBI, then we'll run that script to install EDirect on to your VM.

First, download the script

```consle
~$  curl ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh -o install-edirect.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   665  100   665    0     0    143      0  0:00:04  0:00:04 --:--:--   149
```

then set the script's permissions to be executable (`+x`) 

```console
~$ chmod +x install-edirect.sh
```

and execute the script

```console
~$ ./install-edirect.sh

Trying to establish local installations of any missing Perl modules
(as logged in /home/mlandis/edirect/setup-deps.log).
Please be patient, as this step may take a little while.
aux/
aux/lib/
aux/lib/perl5/
aux/lib/perl5/Mozilla/
aux/lib/perl5/Mozilla/mk-ca-bundle.pl
aux/lib/perl5/Mozilla/CA/
aux/lib/perl5/Mozilla/CA/cacert.pem
aux/lib/perl5/Mozilla/CA.pm
aux/lib/perl5/JSON/
aux/lib/perl5/JSON/Any.pm

Entrez Direct has been successfully downloaded and installed.

In order to complete the configuration process, please execute the following:

  echo "export PATH=\${PATH}:/home/mlandis/edirect" >> $HOME/.bashrc

or manually edit the PATH variable assignment in your .bash_profile file.

Would you like to do that automatically now? [y/N]
<press y>
OK, done.
```

Your local installation of EDirect should now be correct. Now, you can remove the script.
```console
~$ rm install-edirect.sh
```

A more concise way to download a file and execute its contents as a script is
```console
~$ bash -c "$(curl ftp://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
```

Calling `bash -c` will run its argument as a script. The `$( ... )` notation is another way to create a command substitution, just as we've been doing with back-ticks (\`) in our scripts. Finally, the `curl` command will download the targeted file and print its output to the screen (stdout) by default. So, `bash -c` will receive the contents of the file downloaded by `curl` through the command substitution `$(...)`.


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
$ esearch -db nucleotide -query "Viburnum clemensiae" |  efetch -format fasta > sequences.fasta`
$ head -n5 sequences.fasta
>KJ796120.1 Viburnum clemensae voucher PW Sweeney et al. 2142 RNA polymerase beta' subunit (rpoC2) gene, partial cds; chloroplast
ATGGAGGTACTTATGGCAGAACGGGCCAATCTGGTCTTTCACAATAAAGTGATAGACGGAACTGCCATGA
AACGACTTATTAGTAGATTAATCGATCACTTCGGAATGGCATATACATCACACATCCTGGATCAAGTAAA
GACTCTGGGTTTCCAACAAGCTACTGCTACATCTATTTCATTAGGAATTGATGATCTTTTAACAATACCT
TCTAAGAGATGGCTAGTTCAAGATGCTGAACAACAAAGTTTGATTTTGGAAAAACACCATCATTATGGGA
```

What command would you use to learn how many sequences were written to `sequences.fasta`? to learn how many lines the file contains?

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
$ esearch -db nucleotide -query "Tyrannosaurus Rex"
<ENTREZ_DIRECT>
  <Db>nucleotide</Db>
  <WebEnv>MCID_5f779558ae9e2c11ab7040b6</WebEnv>
  <QueryKey>1</QueryKey>
  <Count>0</Count>
  <Step>1</Step>
</ENTREZ_DIRECT>
$ esearch -db nucleotide -query "Tyrannosaurus Rex" | efetch -format fasta
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

The gene file is a .csv value, where the first column gives the gene name and the second column gives the expected sequence length (in the format `x:y` to be used with `[SLEN]` as in Problem 1), or is left empty for genes that will not be filtered by sequence length during the search.

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

Now run your script against a set of species and genes that you find personally interesting!

---

To submit your assignment, please commit and push the following files to your repository:
```
find_accession.sh        # from problem 1
fetch_accessions.sh      # from problem 2
files/*.fasta            # the output from problem 2
history.txt              # redirected from `history` command
```

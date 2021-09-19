# Lab 07

*Lab 07 GitHub Classroom link:* to be provided

This lab will focus on retrieving fasta formatted sequences from GenBank, one of NCBI's Entrez databases. These techniques are useful when you need to generate a dataset for a set of organisms and genes. Although these scripts will only download nucleotide sequence information, the scripts could easily be adapted to compile different kinds of datasets (e.g. amino acid sequences, gene annotation features).

The major components of this lab are:
1. Exploring BLAST
2. Basic uses for EDirect
3. Scripting with EDirect

---

## 1. Exploring BLAST

This section will demonstrate how to use BLAST (Basic Local Alignment Search Tool). The BLAST is often the first tool researchers use to identify *what* a sequence is and what it does. For example: do any known genes have similar content to this anonymous sequence? what is the expected function of this sequence? and, in what species do we find this gene?  To provide information that can help answer these types of questions, BLAST compares a query sequence to a database of target sequences, computes a BLAST score to assess how well the query and matches to each possible target sequence, and then returns those target sequences with the highest BLAST scores (sometimes called 'hits'). BLAST hits report the identities of matched sequences, the match scores, the significance scores, and so forth.

Most researchers use NCBI's online interface to submit BLAST queries against GenBank records (https://blast.ncbi.nlm.nih.gov/Blast.cgi). The goal of this exercise is to familiarize you with designing BLAST queries and interpreting BLAST output.

BLAST is also available as a [command line tool](https://www.ncbi.nlm.nih.gov/books/NBK279690/), which is useful for scripting. The command line tool, however, requires the local installation of a (large!) GenBank database to be used effectively. Because of that, we'll use the web tool today.

**Problem 1.** Open the NCBI BLAST [website](https://blast.ncbi.nlm.nih.gov/Blast.cgi) and select the Protein BLAST tool. This wil open a new interfact with a tab named `blastp` (i.e. BLAST for proteins) selected.

Copy and paste the following amino acid sequence into the first text field, which reads "
Enter accession number(s), gi(s), or FASTA sequence(s)".

```
> Mysterious_protein_sequence
MSKRKAPQET LNGGITDMLT ELANFEKNVS QAIHKYNAYR KAASVIAKYP HKIKSGAEAK
KLPGVGTKIA EKIDEFLATG KLRKLEKIRQ DDTSSSINFL TRVSGIGPSA ARKFVDEGIK
TLEDLRKNED KLNHHQRIGL KYFGDFEKRI PREEMLQMQD IVLNEVKKVD SEYIATVCGS
FRRGAESSGD MDVLLTHPSF TSESTKQPKL LHQVVEQLQK VHFITDTLSK GETKFMGVCQ
LPSKNDEKEY PHRRIDIRLI PKDQYYCGVL YFTGSDIFNK NMRAHALEKG FTINEYTIRP
LGVTGVAGEP LPVDSEKDIF DYIQWKYREP KDRSE
```

Read through the other options that you can set. A few are particularly interesting.

Setting "Query subrange" allows you to limit the BLAST search to match only part of the query sequence, e.g. if you were interested in only matching a particular domain. This may help you allow you to more precisely predict the function of an anonymous protein.

"Database" option allows you to focus your search for matches against a specific protein database. This is particularly useful if you are e.g. only interested in matching against model organisms, whose protein functions are most likely to have been studied experimentaly. Not only will selecting a specific database speed up your search, it will also decrease your average E-value, since smaller databases contain fewer samples, and therefore are less likely to generate matches that are false positives due to multiple testing. Setting "Organism" can limit your search even further.

Click the "BLAST" button to submit your query. It may take the NCBI servers 30-60 seconds to process your request.

Upon completion, the website will display the query results. Scroll down to find the results table.

Review the top 5 BLAST hits. Create a text file called `part_1_problem_1_answers.txt` that contains answers to these questions:
1. What range of Total Score values do you see?
2. What range of E values do you see?
3. What species does the (input) query sequence probably belong to?
4. What gene does the query sequence belong to?
5. What is the putative function for this gene?
6. Relatively speaking, would you expect that this gene and its function evolves slowly or rapidly compared to other genes?

**Problem 2.** Open the NCBI BLAST [website](https://blast.ncbi.nlm.nih.gov/Blast.cgi) and select the Protein BLAST tool again. Paste the same `Mysertious_protein_sequence` into the text field.

Do not click BLAST yet. Instead, expand the `+ Algorithm parameters` option at the bottom of the screen. Change "Max target sequences" from 100 to 1000 so more (worse) possible matches are returned. Change the "Word size" to 2, which requires fewer characters to initiate a possible match. Change the "Gap costs" to "Existence: 6, Extension: 2" which tells BLAST to allow for more gaps in its alignments. Change "Compositional adjustments" to "No adjustment" to tell BLAST to disregard what we know about the relative frequencies of amino acids. Lastly, uncheck "Low complexity regions" under "Filter" to tell BLAST to ignore segments of the protein that contain little information (e.g. proline-rich segments, acidic/basic regions).

These options should *worsen* our search. Now click BLAST. The query will take longer (60-120 seconds).

Under the "Filter Results" box in the upper right, enter 50 to 60 in the "Percent Identity" option. Click Filter

Review the top 5 BLAST hits in the filtered results. Create a text file called `part_1_problem_2_answers.txt` that contains answers to these questions:
1. What range of Total Score values do you see?
2. What range of E values do you see?
3. What species were matched? Provide some context for how distantly related those species are relative to the species from which the query sequence probably originated.

Click on the name of a sequence to inspect the BLAST alignment. You should see output that resembles this:
```
Query  2    SKRKAP--QETLNGGITDMLTELANFEKNVSQAIHKYNAYRKAASVIAKYPHKIKSGAEA  59
            +KRK P  +  LN  + ++L E+A +E+NV++ +HKYNAYR AAS +AK+P KI SG+EA
Sbjct  3    NKRKNPTSENNLNASVCELLLEIAEYERNVNRNVHKYNAYRNAASTLAKHPKKITSGSEA  62

Query  60   KKLPGVGTKIAEKIDEFLATGKLRKLEKIRQDDTSSSINFLTRVSGIGPSAARKFVDEGI  119
            KKL GVG+KI +KIDE++ TG++ K++KIR DDT+ +IN L RVSGIGP+ AR+ +++GI
Sbjct  63   KKLKGVGSKIGDKIDEYIKTGEMGKVKKIRADDTNVAINLLARVSGIGPAKARELINDGI  122

Query  120  KTLEDLRKNEDKLNHHQRIGLKYFGDFEKRIPREEMLQMQDIVLNEVKKVDSEYIATVCG  179
             T+EDLRKN+DKLNHHQ IGLKYF DFE RIPR+E+  ++  +   + + DS+Y+ T+CG
Sbjct  123  TTIEDLRKNQDKLNHHQIIGLKYFEDFELRIPRDEIKLIEKQLKEHIGEFDSKYLVTICG  182

Query  180  SFRRGAESSGDMDVLLTHPSFTSESTKQPKLLHQVVEQLQKVHFITDTLSKGETKFMGVC  239
            S+RRGA+SSGD+D LLTHPS+TSES+K P LL +V + L+    +TDTLS+G++KFMGVC
Sbjct  183  SYRRGAKSSGDVDALLTHPSYTSESSKCPSLLSKVTQVLKDHGLVTDTLSQGDSKFMGVC  242

Query  240  QLPSKNDEKEYPHRRIDIRLIPKDQYYCGVLYFTGSDIFNKNMRAHALEKGFTINEYTIR  299
             L      +  PHRR+DIRL+P DQYYCG+LYFTGSD+FNK MR HAL+KGFT+NEY IR
Sbjct  243  HL-----MEGLPHRRLDIRLLPHDQYYCGILYFTGSDMFNKAMRQHALDKGFTLNEYCIR  297

Query  300  PLGVTGVAGEPLPVDSEKDIFDYIQWKYREPKDRS  334
            P+G TGV GE LPV  E+DIFDYI + Y+EP +R+
Sbjct  298  PVGSTGVPGEALPVSCERDIFDYIDYDYKEPHERN  332
```

The top line for each row (`Query`) reports the query sequence you initially provided. The bottom line (`Sbjct`) displays the content for the hit your are inspecting. The middle line indicates whether two amino acids at a given position are identical (letter), are functionally equivalent (`+`), or differ (` `; space). Positions that differ must be explained either by an amino acid substitution (letter on top/bottom sequences differ) or a gap (`-` on top/bottom sequence).

**Problem 3.** Return to the BLAST [website](https://blast.ncbi.nlm.nih.gov/Blast.cgi). This time, select the Nucleotide BLAST tool. Copy the text below and paste it into the "Enter Query Sequence" text field.

```
>DinoDNA  "Dinosaur DNA" from Crichton JURASSIC PARK  p. 103 nt 1-1200
GCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAAAATCGACGC
GGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAAGCTCCCTCG
TGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGGAAGCGTGGC
TGCTCACGCTGTACCTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTGGGCTGTGTG
CCGTTCAGCCCGACCGCTGCGCCTTATCCGGTAACTATCGTCTTGAGTCCAACCCGGTAA
AGTAGGACAGGTGCCGGCAGCGCTCTGGGTCATTTTCGGCGAGGACCGCTTTCGCTGGAG
ATCGGCCTGTCGCTTGCGGTATTCGGAATCTTGCACGCCCTCGCTCAAGCCTTCGTCACT
CCAAACGTTTCGGCGAGAAGCAGGCCATTATCGCCGGCATGGCGGCCGACGCGCTGGGCT
GGCGTTCGCGACGCGAGGCTGGATGGCCTTCCCCATTATGATTCTTCTCGCTTCCGGCGG
CCCGCGTTGCAGGCCATGCTGTCCAGGCAGGTAGATGACGACCATCAGGGACAGCTTCAA
CGGCTCTTACCAGCCTAACTTCGATCACTGGACCGCTGATCGTCACGGCGATTTATGCCG
CACATGGACGCGTTGCTGGCGTTTTTCCATAGGCTCCGCCCCCCTGACGAGCATCACAAA
CAAGTCAGAGGTGGCGAAACCCGACAGGACTATAAAGATACCAGGCGTTTCCCCCTGGAA
GCGCTCTCCTGTTCCGACCCTGCCGCTTACCGGATACCTGTCCGCCTTTCTCCCTTCGGG
CTTTCTCAATGCTCACGCTGTAGGTATCTCAGTTCGGTGTAGGTCGTTCGCTCCAAGCTG
ACGAACCCCCCGTTCAGCCCGACCGCTGCGCCTTATCCGGTAACTATCGTCTTGAGTCCA
ACACGACTTAACGGGTTGGCATGGATTGTAGGCGCCGCCCTATACCTTGTCTGCCTCCCC
GCGGTGCATGGAGCCGGGCCACCTCGACCTGAATGGAAGCCGGCGGCACCTCGCTAACGG
CCAAGAATTGGAGCCAATCAATTCTTGCGGAGAACTGTGAATGCGCAAACCAACCCTTGG
CCATCGCGTCCGCCATCTCCAGCAGCCGCACGCGGCGCATCTCGGGCAGCGTTGGGTCCT
```

Review the top 5 BLAST hits in the filtered results. Create a text file called `part_1_problem_3_answers.txt` that contains answers to these questions:
1. What range of Total Score values do you see?
2. What range of E values do you see?
3. What are the sequence descriptions for the best BLAST hits?
4. What are genes like this often used for?
5. This gene sequence appears on page 103 in "Jurassic Park" by Michael Crichton, apparently in reference to the DNA sequences the scientists used to bring extinct non-avian dinosaurs to life. Do you think it is likely that Crichton generated a random DNA sequence or used the DNA from a random gene for his book? Or do you think it is likely that the gene sequence Crichton published could somehow be involved in ressurrecting dinosaurs? Feel free to speculate wildly, but try to give a defensible answer.

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


---

To submit your assignment, please commit and push the following files to your repository:
```
part_1_problem_1.txt     # answers for "good" run of blastp
part_1_problem_2.txt     # answers for "bad" run of blastp
part_1_problem_3.txt     # answers for Jurassic Park run w/ blastn
find_accession.sh        # from problem 2
fetch_accessions.sh      # from problem 3
files/*.fasta            # the output from problem 3
history.txt              # redirected from `history` command
```

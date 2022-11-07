# Lab 18

*Lab 18 GitHub Classroom link:* [https://classroom.github.com/a/rzUHC1m_](https://classroom.github.com/a/rzUHC1m_)

In this lab, we'll learn how to test hypotheses regarding protein evolution using the phylogenetic software package, PAML. [PAML](http://abacus.gene.ucl.ac.uk/software/paml.html) -- which stands for "Phylogenetic Analysis by Maximum Likelihood" -- is open source software written for inferring phylogenies and other phylogenetic patterns.  Specifically, PAML provides a special tool called `codeml` that is used to measure the relative rates of nonsynonmyous vs. synonymous substitutions (called dN/dS).

This lab will cover the following topics

1. Installing PAML
2. Running PAML
3. Scripting with PAML

To begin this lab, clone your GitHub assignment repository to your virtual machine, enter the newly cloned directory, then open the `python` or `ipython` command line interface.

---

## Installing PAML

PAML is written in the programming language C. C programs must be compiled into executable binaries in order to run. Let's install it now.

Log on to your virtual machine, enter the `~/apps` directory, then download the most recent version of PAML using `wget` from the following URL: http://abacus.gene.ucl.ac.uk/software/paml4.9j.tgz. Once downloaded, we can follow the Unix installation instructions for PAML, given [here](http://abacus.gene.ucl.ac.uk/software/paml.html#download). 

```console
$ tar zxvf paml4.9j.tgz      # decompress PAML tarball
... unzips ~100 files ...
$ cd paml4.9j/src            # enter PAML source code dir            
$ make -f Makefile           # this compiles the PAML binaries
cc  -O3 -o baseml baseml.c tools.c -lm
... followed by ~5 minutes of compiler output ...
```

Now, we will clean up the PAML binaries, first by deleting the Windows executables (`.exe`), then moving the newly build binaries, and finally by adding the new `codeml` program to `~/.local/bin`. Recall that `~/.local/bin` is identified in the environment variable, `PATH`, as defined by `~/.bash_profile`.

```console
$ rm ../bin/*.exe
$ mv baseml basemlg codeml pamp evolver yn00 chi2 ../bin
$ cd ~/.local/bin
$ ln -s ~/apps/paml4.9j/bin/codeml .
$ which codeml
/home/mlandis/.local/bin/codeml
```
Now `codeml` can be run from anywhere in the VM's filesystem.

---

## Running PAML

In this section, we will run a `codeml` analysis to gain a better understanding of the program's settings, input, and output.

The `codeml` program may now be run from any directory, but the program requires a file called `codeml.ctl` in the local directory to specify the analysis settings. PAML provides a set of example data and control files to demonstrate how the software works.

Let's begin by running a `codeml` analysis to detect site-specific positive selection in the envelope protein for HIV. We might expect that some sites in env are under positive selection, since the protein is important for HIV infection and for host immune system detection. Navigate into the `examples/HIVNSsites` directory in this lab's repo, then type `codeml` to run an example analysis

```console
$ cd ~/labs/lab-19-mlandis/examples/HIVNSsites
$ codeml

CODONML in paml version 4.9j, February 2020

----------------------------------------------
Phe F TTT | Ser S TCT | Tyr Y TAT | Cys C TGT
      TTC |       TCC |       TAC |       TGC
Leu L TTA |       TCA | *** * TAA | *** * TGA
      TTG |       TCG |       TAG | Trp W TGG
----------------------------------------------
Leu L CTT | Pro P CCT | His H CAT | Arg R CGT
      CTC |       CCC |       CAC |       CGC
      CTA |       CCA | Gln Q CAA |       CGA
      CTG |       CCG |       CAG |       CGG
----------------------------------------------
Ile I ATT | Thr T ACT | Asn N AAT | Ser S AGT
      ATC |       ACC |       AAC |       AGC
      ATA |       ACA | Lys K AAA | Arg R AGA
Met M ATG |       ACG |       AAG |       AGG
----------------------------------------------
Val V GTT | Ala A GCT | Asp D GAT | Gly G GGT
      GTC |       GCC |       GAC |       GGC
      GTA |       GCA | Glu E GAA |       GGA
      GTG |       GCG |       GAG |       GGG
----------------------------------------------
Nice code, uuh?
NSsites batch run (ncatG as in YNGP2000):   0  1  2
ns = 13  	ls = 273
Reading sequences, sequential format..
Reading seq #13: U68508
Sequences read..
Counting site patterns..  0:00
Compressing,     79 patterns at     91 /     91 sites (100.0%),  0:00
Collecting fpatt[] & pose[],     79 patterns at     91 /     91 sites (100.0%),  0:00
Counting codons..

      624 bytes for distance
    77104 bytes for conP
     6952 bytes for fhK
  5000000 bytes for space
 
 ... the analysis will then run for ~2 minutes
     with most standard output relating to
     the program's parameter estimating routine ...
 
 56 h-m-p  0.0005 0.2624   0.5113 +Y     1106.454034  0 0.0017  2076 | 0/28
 57 h-m-p  0.0000 0.0001   0.8554 ++     1106.454018  m 0.0001  2135 | 1/28
 58 h-m-p  0.0006 0.3067   0.7461 +C     1106.453731  0 0.0026  2195 | 1/28
 59 h-m-p  0.0011 0.1311   1.8754 CC     1106.453403  1 0.0013  2255 | 1/28
 
 ... until finally, the program reports that the
     analysis has completed ...
     
BEBing (dim = 4).  This may take several minutes.
Calculating f(x_h|w): 10 categories 21 w sets.
Calculating f(X), the marginal likelihood.
	log(fX) = -1112.401420  S = -1023.138908  -111.908274
Calculating f(w|X), posterior probabilities of site classes.
	did  79 /  79 patterns   2:24
Time used:  2:24
```

When `codeml` is executed, it runs according to the settings specified in the control file, `codeml.ctl`. (Alternatively, `codeml` will run using an alternative control file if when supplied as an argument, e.g. `codeml another_file.ctl`.) Let's study the most salient features of `codeml.ctl` to understand what the `codeml` analysis did:

```console
      seqfile = HIVenvSweden.txt    * sequence data file name
     treefile = HIVenvSweden.trees   * tree structure file name

      outfile = mlc          * main result file name
        noisy = 3   * 0,1,2,3,9: how much rubbish on the screen
      verbose = 0   * 1: detailed output, 0: concise output
      runmode = 0   * 0: user tree;  1: semi-automatic;  2: automatic
                    * 3: StepwiseAddition; (4,5):PerturbationNNI; -2: pairwise

      seqtype = 1   * 1:codons; 2:AAs; 3:codons-->AAs
    CodonFreq = 2   * 0:1/61 each, 1:F1X4, 2:F3X4, 3:codon table
        clock = 0   * 0: no clock, unrooted tree, 1: clock, rooted tree
       aaDist = 0   * 0:equal, +:geometric; -:linear, {1-5:G1974,Miyata,c,p,v}
        model = 0

      NSsites = 0 1 2
                    * 0:one w; 1:NearlyNeutral; 2:PositiveSelection; 3:discrete;
                    * 4:freqs; 5:gamma;6:2gamma;7:beta;8:beta&w;9:beta&gamma;10:3normal
        icode = 0   * 0:standard genetic code; 1:mammalian mt; 2-10:see below
        Mgene = 0   * 0:rates, 1:separate; 2:pi, 3:kappa, 4:all

    fix_kappa = 0   * 1: kappa fixed, 0: kappa to be estimated
        kappa = .3   * initial or fixed kappa
    fix_omega = 0   * 1: omega or omega_1 fixed, 0: estimate
        omega = 1.3  * initial or fixed omega, for codons or codon-based AAs
        ncatG = 10   * # of categories in the dG or AdG models of rates

        getSE = 0   * 0: don't want them, 1: want S.E.s of estimates
 RateAncestor = 0   * (0,1,2): rates (alpha>0) or ancestral states (1 or 2)

   Small_Diff = .45e-6
    cleandata = 1  * remove sites with ambiguity data (1:yes, 0:no)?
  fix_blength = 0  * 0: ignore, -1: random, 1: initial, 2: fixed, 3: proportional
```

The [PAML manual](http://abacus.gene.ucl.ac.uk/software/pamlDOC.pdf) gives detailed descriptions for the `codeml.ctl`. The control file assigns values to critical analysis variables, using the `=` assignment operator. Note also that `*` is used to define a comment. We will focus on only a few `codeml` features, in the order that they appear in the control file.

In the two settings blocks, `codeml` requires a sequence alignment file (`seqfile`) and a tree file (`treefile`). Output is stored to the file `outfile`. The variables `noisy` and `verbose` control how much output is printed. The `runmode` setting allows the user to either provide a pre-estimated tree (as we did) or to estimate the tree from the sequence data itself.

In the third setting block, the control file defines what data type is provided; we provide nucleotide (codon) data. The `CodonFreq`, `clock`, and `aaDist` settings control how we model the equilibrium probabilities for different codons, the relative rate of codon evolution across branches in the phylogeny, or whether we use an "empirical" model of amino acid change. The `model` setting allows us to control whether all branches and sites share the same dN/dS ratio (`model=0`, the *basic model*), whether dN/dS ratios can vary among branches (`model=1` and `model=2`, *branch models*), or whether sites can differ in dN/dS ratios (`model=0` in combination with `NSsites` setting; *sites models*).

By the fourth settings block, we see that our control file used `model = 0` with `NSSites=0 1 2`. This specifies three separate analysis to run: (1) a basic analysis (`NSSites = 0`) where all branches and sites share the same dN/dS ratio; (2) a nearly-neutral analysis (`NSSites = 1`) where all some proportion of sites are allowed to evolve under purifying selection (dN/dS < 1) and all remaining sites evolve under neutrality (dN/dS = 1); and (3) a positive selection analysis (`NSSites = 2`) where some proportion of sites evolve under purifying selection (dN/dS < 1), another proportion of sites evolve under positive selection (dN/dS > 1), and all remaining sites evolve under neutrality (dN/dS = 1).

In the fifth block, we instruct `codeml` to estimate the relative rates of nucleotide transitions vs. transversions (`fix_kappa = 0`) and the dN/dS ratios (`fix_omega = 0`). The `ncatG` parameter tunes how we approximate among site rate variation, and does not need to be changed. The remaining settings (`getSE`, `RateAncestor`, `Small_Diff`, `cleandata`, and `fix_blength`) generally do not need to be modified, either.

Now, let's examine the output, which is named according to the `outfile = mlc` statement in the control file. Output files from `codeml` are generally several hundred lines in length.

```console
$ wc -l mlc
428 mlc
```

Open the file in Nano (`nano mlc`) and we will identify several blocks of output that are especially interesting. The first block of output reports codon usage for each of the Sequences 1-6 in the alignment. Sequences 7-12 appear in the following matrix, and Sequence 13 appears by itself in the matrix following that. In principle, this text could easily be read and parsed to quickly measure codon usage frequencies for a given sequence alignment.

```console
... only shown for Sequences 1-6 ...

Codon usage in sequences
--------------------------------------------------------------------------------------------------------------------------------------
Phe TTT   4   3   2   2   2   3 | Ser TCT   2   2   2   2   2   1 | Tyr TAT   2   2   2   2   1   1 | Cys TGT   2   2   2   2   2   2
    TTC   1   2   1   1   1   1 |     TCC   1   1   1   1   1   1 |     TAC   0   0   0   0   1   0 |     TGC   0   0   0   0   0   0
Leu TTA   2   1   2   2   2   2 |     TCA   0   0   0   0   0   0 | *** TAA   0   0   0   0   0   0 | *** TGA   0   0   0   0   0   0
    TTG   0   0   0   0   0   0 |     TCG   1   1   0   0   0   0 |     TAG   0   0   0   0   0   0 | Trp TGG   1   1   1   1   1   1
--------------------------------------------------------------------------------------------------------------------------------------
Leu CTT   1   1   1   1   0   1 | Pro CCT   0   0   0   0   0   1 | His CAT   1   1   2   2   3   2 | Arg CGT   0   0   0   0   0   0
    CTC   0   0   0   0   0   0 |     CCC   1   1   1   1   1   1 |     CAC   0   0   0   0   0   0 |     CGC   0   0   0   0   0   0
    CTA   1   1   1   1   1   1 |     CCA   1   1   1   1   1   2 | Gln CAA   3   3   3   3   3   3 |     CGA   0   0   0   0   0   0
    CTG   0   0   0   0   0   1 |     CCG   0   0   0   0   0   0 |     CAG   2   2   2   2   1   1 |     CGG   0   0   0   0   0   0
--------------------------------------------------------------------------------------------------------------------------------------
Ile ATT   3   2   2   2   4   2 | Thr ACT   1   2   1   1   1   1 | Asn AAT   7   8   7   5   6   8 | Ser AGT   1   1   2   2   2   1
    ATC   0   1   0   0   0   0 |     ACC   2   1   1   1   1   1 |     AAC   5   5   4   5   5   6 |     AGC   0   0   0   0   0   0
    ATA   7   8   7   8   7   8 |     ACA   4   3   5   4   4   4 | Lys AAA   6   6   5   6   5   6 | Arg AGA   6   6   8   6   7   7
Met ATG   0   0   0   0   1   0 |     ACG   0   0   1   1   2   1 |     AAG   0   0   0   1   0   1 |     AGG   0   0   0   1   0   0
--------------------------------------------------------------------------------------------------------------------------------------
Val GTT   1   0   0   0   0   0 | Ala GCT   2   2   2   2   2   2 | Asp GAT   1   1   1   1   1   0 | Gly GGT   0   0   0   0   0   0
    GTC   0   0   1   1   1   1 |     GCC   0   0   0   0   0   0 |     GAC   0   0   1   0   0   1 |     GGC   0   0   1   0   0   0
    GTA   5   5   7   5   5   5 |     GCA   3   5   2   2   2   3 | Glu GAA   6   5   5   8   8   4 |     GGA   4   4   3   4   3   3
    GTG   0   0   0   0   0   0 |     GCG   0   0   0   0   0   0 |     GAG   0   0   0   0   0   0 |     GGG   1   1   1   1   1   1
--------------------------------------------------------------------------------------------------------------------------------------
```

Next comes a list of base frequencies across codon positions, followed by a sum of codon usage across sequences and amino acids

```console
Sums of codon usage counts
------------------------------------------------------------------------------
Phe F TTT      37 | Ser S TCT      23 | Tyr Y TAT      18 | Cys C TGT      26
      TTC      14 |       TCC      13 |       TAC       1 |       TGC       0
Leu L TTA      26 |       TCA       0 | *** * TAA       0 | *** * TGA       0
      TTG       0 |       TCG       3 |       TAG       0 | Trp W TGG      13
------------------------------------------------------------------------------
Leu L CTT      12 | Pro P CCT       3 | His H CAT      21 | Arg R CGT       0
      CTC       0 |       CCC      13 |       CAC       0 |       CGC       0
      CTA      14 |       CCA      14 | Gln Q CAA      44 |       CGA       2
      CTG       1 |       CCG       0 |       CAG      19 |       CGG       0
------------------------------------------------------------------------------
Ile I ATT      28 | Thr T ACT      18 | Asn N AAT      84 | Ser S AGT      21
      ATC       4 |       ACC      15 |       AAC      66 |       AGC       1
      ATA      97 |       ACA      61 | Lys K AAA      71 | Arg R AGA      94
Met M ATG       1 |       ACG       9 |       AAG       7 |       AGG       2
------------------------------------------------------------------------------
Val V GTT       6 | Ala A GCT      26 | Asp D GAT      11 | Gly G GGT       2
      GTC       6 |       GCC       1 |       GAC      12 |       GGC       1
      GTA      63 |       GCA      36 | Glu E GAA      69 |       GGA      42
      GTG       0 |       GCG       0 |       GAG       0 |       GGG      12
------------------------------------------------------------------------------
```
Notice, for example, how frequently `GTA` is used to encode Valine, or `GGG` is used to encode Glycine.

Next, the outfile file reports blocks of results from each of the three models we analyzed: `Model 0: one-ratio`, `Model 1: NearlyNeutral (2 categories)`, and `Model 2: PositiveSelection (3 categories)`.

Find the line that reads `Model 0: one-ratio`. The lines that follow immediately afterwards simply state what tree was used for the model-fitting, which we can ignore since we know that we supplied this tree through the control file. The remaining output for `Model 0` reports the parameter estimates of interest.

```console
Detailed output identifying parameters

kappa (ts/tv) =  2.47175

omega (dN/dS) =  0.90129

dN & dS for each branch

 branch          t       N       S   dN/dS      dN      dS  N*dN  S*dS

  14..1      0.024   231.1    41.9  0.9013  0.0078  0.0086   1.8   0.4
  14..2      0.079   231.1    41.9  0.9013  0.0260  0.0288   6.0   1.2
  14..15     0.153   231.1    41.9  0.9013  0.0501  0.0556  11.6   2.3
  15..16     0.024   231.1    41.9  0.9013  0.0078  0.0086   1.8   0.4
  16..3      0.050   231.1    41.9  0.9013  0.0165  0.0183   3.8   0.8
  16..17     0.083   231.1    41.9  0.9013  0.0274  0.0304   6.3   1.3
  17..4      0.028   231.1    41.9  0.9013  0.0093  0.0103   2.2   0.4
  17..5      0.100   231.1    41.9  0.9013  0.0327  0.0363   7.6   1.5
  15..18     0.048   231.1    41.9  0.9013  0.0158  0.0175   3.6   0.7
  18..6      0.132   231.1    41.9  0.9013  0.0432  0.0479  10.0   2.0
  18..19     0.034   231.1    41.9  0.9013  0.0110  0.0123   2.6   0.5
  19..7      0.191   231.1    41.9  0.9013  0.0627  0.0695  14.5   2.9
  19..20     0.064   231.1    41.9  0.9013  0.0210  0.0233   4.8   1.0
  20..8      0.193   231.1    41.9  0.9013  0.0634  0.0703  14.6   2.9
  20..21     0.051   231.1    41.9  0.9013  0.0166  0.0184   3.8   0.8
  21..22     0.035   231.1    41.9  0.9013  0.0114  0.0126   2.6   0.5
  22..23     0.037   231.1    41.9  0.9013  0.0120  0.0133   2.8   0.6
  23..24     0.056   231.1    41.9  0.9013  0.0182  0.0202   4.2   0.8
  24..9      0.019   231.1    41.9  0.9013  0.0062  0.0069   1.4   0.3
  24..11     0.070   231.1    41.9  0.9013  0.0231  0.0256   5.3   1.1
  23..10     0.030   231.1    41.9  0.9013  0.0099  0.0110   2.3   0.5
  22..12     0.061   231.1    41.9  0.9013  0.0200  0.0222   4.6   0.9
  21..13     0.198   231.1    41.9  0.9013  0.0650  0.0721  15.0   3.0

tree length for dN:       0.5771
tree length for dS:       0.6403
```

The parameter estimates tell us that transitions occur at a higher rate than transversions (`kappa (ts/tv) =  2.47175`) which is typical. We also learn that for the basic model, the dN/dS ratio is slightly less than 1 (`omega (dN/dS) =  0.90129`). The following lines report the expect proportion of nonsynonymous (column `dN`) versus synonymous (`dS`) substitutions per codon-site along each branch of the tree. The numbers for `N` and `S` are comparable to the numbers of nonsynonymous and synonymous "sites" obtained by the counting method in lecture, and averaged over all sequences in the alignment. The `tree length for dN` value equals the sum of values under the branchwise `dN` value. Dividing the tree length for dN by the tree length for dS gives us the value `0.5771 / 0.6403 = 0.90129`, which is identical to what is reported with the line `omega (dN/dS) =  0.90129`.


Now, let's look at the results for `Model 1: NearlyNeutral (2 categories)`. Ignoring output concerning the tree, we see:

```console
Detailed output identifying parameters

kappa (ts/tv) =  2.59461


MLEs of dN/dS (w) for site classes (K=2)

p:   0.48418  0.51582
w:   0.07885  1.00000
```

The transition/transversion rate ratio is very similar to that for `Model 0`. More interestingly we obtain maximum likelihood estimators (`MLEs`) for our two site-classes. The first row (`p`) reports the proportion of codons expected to fall into the first vs. second site-class. The second row (`w`) presents the dN/dS estimates for codons belonging to site-class 1 or site-class 2. Specifically, `Model 1` found that 48% of codon sites evolved under strong purifying selection (dN/dS = 0.07885 < 1) and the remaining 52% of codon sites evolve neutrally (dN/dS = 1.0). The table with values for `dN & dS for each branch` differ from those obtained under `Model 0`, but are read in the same way.

Finally, let's examine the results for `Model 2: PositiveSelection (3 categories)`.

```console
Detailed output identifying parameters

kappa (ts/tv) =  2.78555


MLEs of dN/dS (w) for site classes (K=3)

p:   0.37712  0.44169  0.18119
w:   0.05998  1.00000  3.62564
```
This output is interpreted in a manner analogous to how the `Model 1` results were read. The `Model 2` analysis estimates that 37% of codons evolve in a manner consistent with strong purifying selection (dN/dS = 0.05998 < 1), 44% of sites evolve in an effectively neutral manner (dN/dS = 1.0), and the remaining 18% of codons evolve in a manner resembling positive selection (dN/dS = 3.62564 > 1).

The `Model 2` analysis also reports which amino acid positions were estimated as evolving under positive selection. We will show only the `Naive Empirical Bayes` analysis, but the `Bayes Empirical Bayes` analysis output is read in a similar manner. The first column reports the amino acid position, the second column gives the amino acid in that position according to the 1st sequence (in this case, U68496), the third column reports the probability that the amino acid was subject to a force consistent with positive selection, and the final column reports the site-specific dN/dS estimate.

```console
Naive Empirical Bayes (NEB) analysis
Positively selected sites (*: P>95%; **: P>99%)
(amino acids refer to 1st sequence: U68496)

            Pr(w>1)     post mean +- SE for w

     9 S      0.720         2.889
    22 S      0.796         3.089
    24 E      0.578         2.517
    26 N      0.905         3.376
    28 T      0.999**       3.624
    31 N      0.566         2.486
    39 H      0.640         2.681
    51 I      0.883         3.319
    66 E      0.998**       3.621
    68 N      0.601         2.578
    69 N      0.830         3.179
    76 E      0.671         2.761
    83 I      0.811         3.128
    87 V      0.985*        3.587
 ```

The final `Model 2` result we'll consider are the relative support for the dN/dS estimates for sites under purifying selection (w0 < 1) and for sites under positive selection (w2 > 1). 

```console
The grid (see ternary graph for p0-p1)

w0:   0.050  0.150  0.250  0.350  0.450  0.550  0.650  0.750  0.850  0.950
w2:   1.500  2.500  3.500  4.500  5.500  6.500  7.500  8.500  9.500 10.500


Posterior on the grid

w0:   0.400  0.339  0.182  0.063  0.013  0.002  0.000  0.000  0.000  0.000
w2:   0.000  0.203  0.503  0.208  0.056  0.018  0.007  0.003  0.002  0.001
```

The first set of numbers defines a grid of possible dN/dS values for purifying (w0) and positive (w2) selection. The second grid of numbers reports the probability that the corresponding dN/dS values estimated from the data are less than the corresponding grid-values.

This output states that the dN/dS estimate for purifying selection (w0; dN/dS < 1) was less than 0.050 with 40% confidence, less than 0.150 with 73% confidence, less than 0.250 with 92% confidence. Positive selection (w2; dN/dS > 1) was between the values 1 and 2.5 with 20% confidence, between 1 and 3.5 with 70% confidence, and between 1 and 4.5 with 91% confidence.


The `rst` file presents much of the same information as `mlc`, with more attention paid to the probability that any codon belongs to a certain dN/dS class and the average estimated dN/dS value estimated for each site
```console
$ cat rst
Supplemental results for CODEML (seqf: HIVenvSweden.txt  treef: HIVenvSweden.trees)


Model 0: one-ratio

Model 1: NearlyNeutral

MLEs of dN/dS (w) for site classes (K=2)

p:   0.48418  0.51582
w:   0.07885  1.00000

Naive Empirical Bayes (NEB) probabilities for 2 classes & postmean_w
(amino acids refer to 1st sequence: U68496)

   1 V   0.00042 0.99958 ( 2)  1.000
   2 V   0.94989 0.05011 ( 1)  0.125
   3 I   0.85352 0.14648 ( 1)  0.214
   4 R   0.97750 0.02250 ( 1)  0.100
   5 S   0.71002 0.28998 ( 1)  0.346
```

The `Model 0` analysis has only one site-class, so no output is reported. The `Model 1` analysis as two site-classes, and we see the same maximum likelihood estimators reported here as they were reported in `mlc`. The table at the bottom of the example output prints each amino acid site, the value of that site in the reference sequence (U68496), the probability that the site is in site-class 1 or site-class 2, the site class with higher probability in parentheses, and the estimated dN/dS value for that site probabilistically averaged over the possible site-class memberships. For example, amino acid in site 3 has a reference identity of I (isoleucine), and was estimated to be in site-class 1 with probability 0.85 vs. site-class 2 with probability 0.15. Site-class 1 is more probable (`( 1)`). The average dN/dS value for this amino acid is approximately `0.85352 * 0.07885 + 0.14648 * 1.0000` or `0.2137801`.

What does all of this mean? This first model assumes all sites evolve under the same dN/dS ratio, and infers that the entire env protein for these HIV sequences evolved under weak purifying selection (dN/dS < 1). The second model finds that roughly 48% of sites evolved under strong purifying selection (dN/dS = 0.079 < 1.0) while 52% sites evolved under neutrality (dN/dS = 1.0). When compared to model 2, the third model infers even stronger purifying selection (dN/dS = 0.060 < 1.0) acts upon a smaller proportion of 37% sites. Fewer sites evolve under neutrality, as well, with 44% of sites falling into the site-class with dN/dS = 1.0. Finally, 18% of all codons in the HIV envelope gene evolve under strong positive selection (dN/dS = 3.63 > 1.0). The table of postively selected amino acid sites can be used to test new hypotheses regarding the evolution of host-virus interactions, and potentially guide therapies for preventing viral infection and/or disease.

---


## Scripting with PAML

As flexible as PAML is for modeling, it is somewhat limited in terms of how it accepts input and how it prints output. We will write a Python script that accepts user arguments as input, runs a PAML analysis under those settings, then generates output datafiles that are easily parsed.

Create a module called `paml.py`. The module will define two functions.

The first function is called `run(control_file, seq_file, tree_file, output_file)`. This function accepts a sequence file and tree file (Newick format) as input. The function then creates a new file called `control_file` in the local directory. The control file will be identical to `codeml.ctl` from the HIV example, except the `seq_file`, `tree_file`, and `output_file` settings are replaced by the user-provided arguments. Once the new control file (`control_file`) is created, run the PAML analysis by calling `codeml control_file`.

The second function is called `format(output_prefix)`. This function will read the `rst` file as input. First, the function will split the output file into different subsections for each model type, then produce two data matrices for Model 1 and Model 2 results. Define the data matrices as lists-of-lists, where each row corresponds to the position of the amino acid.

For Model 1, index columns have the following values (in order): site position, reference sequence amino acid identity, class-1 probability, class-2 probability, most-probable site-class, mean dN/dS value. The first two rows of this matrix would appear as:

```python
[ [ 1, 'V', 0.00042, 0.99958, 2, 1.000 ],
  [ 2, 'V', 0.94989, 0.05011, 1, 0.125 ],
  ...
]
```

The data matrix for Model 2 will also list one amino acid site per row, but with slightly different column entries: site position, reference sequence amino acid identity, class-1 probability, class-2 probability, class-3 probability, most-probable site-class, mean dN/dS value, and probability that the site has dN/dS > 1.

```python
[ [1, 'V', 0.00002, 0.50047, 0.49951, 2, 2.311, 0.500],
  [2, 'V', 0.84770, 0.15185, 0.00045, 1, 0.204, 0.000],
  ...
]
```

The function will then write one output file for each data matrix. If the `output_prefix` argument had the value `HIV`, then the Model 1 output would be named `HIV.model_1.csv` and the Model 2 output would be named `HIV.model_2.csv`. Write the files as comma-separated values, with informative column header names.

Upload your `paml.py` script, your output files for `HIV.model_1.csv` and `HIV.model_2.csv`, and your `history.txt` to your GitHub repository.

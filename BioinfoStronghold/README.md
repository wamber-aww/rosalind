# Introduction
This is the **Bioinformatics Stronghold** problem sets from [Rosalind](http://rosalind.info/problems/list-view/). This part contains questions relating to nucleic acid analysis

# Problems
### Q1: Counting DNA Nucleotides
  - Given: A DNA string s of length at most 1000 nt.
  - Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

### Q2: Transcribing DNA into RNA
  - Given: A DNA string t having length at most 1000 nt.
  - Return: The transcribed RNA string of t.
  
### Q3: Complementing a Strand of DNA
  - Given: A DNA string s of length at most 1000 bp.
  - Return: The reverse complement sc of s.

### Q4: Rabbits and Recurrence Relations
  - Given: Positive integers n≤40 and k≤5.
  - Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

### Q5: Computing GC Content
  - Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
  - Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
  
### Q6: Counting Point Mutations
  - Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
  - Return: The Hamming distance dH(s,t).
  
### Q7: Mendel's First Law
  - Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
  - Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

### Q8: Translating RNA into Protein
  - Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
  - Return: The protein string encoded by s.

### Q9: Finding a Motif in DNA
  - Given: Two DNA strings s and t (each of length at most 1 kbp).
  - Return: All locations of t as a substring of s.

### Q10: Mortal Fibonacci Rabbits
  - Given: Positive integers n≤100 and m≤20.
  - Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

### Q11: Consensus and Profile
  - Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
  - Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

### Q12: Overlap Graphs
  - Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
  - Return: The adjacency list corresponding to O3. You may return edges in any order.

### Q13: Calculating Expected Offspring
  - Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
      1. AA-AA
      2. AA-Aa
      3. AA-aa
      4. Aa-Aa
      5. Aa-aa
      6. aa-aa
  - Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

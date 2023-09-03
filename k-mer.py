#Python 3.10.12 | packaged by Anaconda, Inc. | (main, Jul  5 2023, 19:01:18) [MSC v.1916 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

#function to find the reverse complement.
def reverse_complement(dna_seq):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp_seq = ''.join(complement_dict[base] for base in reversed(dna_seq))
    return reverse_comp_seq

#check how many time given kmer can be found.
def find_overlapping_occurrences(sequence, kmer):
    occurrences = []
    k = len(kmer)
    for i in range(len(sequence) - k + 1):
        if sequence[i:i+k] == kmer:
            occurrences.append(i)
    return occurrences

def find_unique_kmers(sequence, k):
    kmers_to_occurrences = {}
    all_unique = True
    
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmer_reverse = reverse_complement(kmer)
        
        if kmer in kmers_to_occurrences or kmer_reverse in kmers_to_occurrences:
            all_unique = False
            if kmer in kmers_to_occurrences:
                kmers_to_occurrences[kmer].append(i)
            else:
                kmers_to_occurrences[kmer_reverse].append(i)
        else:
            kmers_to_occurrences[kmer] = [i]
            kmers_to_occurrences[kmer_reverse] = [i]
    
    return all_unique, kmers_to_occurrences

# Original DNA sequence is this; direction is 5' to 3'.
seq = "TACGAATTTTTCTTTTGTTTATTTCCTTTCGCTTTGCTTCTCTTCCCTTCGGTTCTGTTC"

# Get the reverse complement of the original DNA sequence.
rev_seq = reverse_complement(seq)

# Check conditions.
k=3;
overlap_seqs = find_overlapping_occurrences(seq, "AGTCT")
result, kmer_occurrences = find_unique_kmers(seq, k)  # can try changing the value of k; default k=5.

# Print results.
if result:
    print(f"The DNA sequence contains all unique {k}-mers.")
else:
    print(f"The DNA sequence does not contain all unique {k}-mers.")
    print("These are the repetitive k-mers found:")
    for kmer, occurrences in kmer_occurrences.items():
        if len(occurrences) > 1:
            print(f"K-mer '{kmer}' found at positions: {occurrences}")








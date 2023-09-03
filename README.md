***

Written by: Shreya Sharma, PhD Student @IITR
Email Address: shreya_s@bt.iitr.ac.in

***

1. k-mer.py : 

This Python script analyzes a DNA sequence for the uniqueness of k-mers (subsequences of length k) and checks for repetitive k-mers. It does this using the following steps:

(i.) It defines a function `reverse_complement` to find the reverse complement of a DNA sequence.
(ii.) It defines a function `find_overlapping_occurrences` to find positions where a given k-mer occurs in a DNA sequence.
(iii.) It defines a function `find_unique_kmers` to find all unique k-mers in the DNA sequence and their positions. It also checks if all k-mers are unique or if there are repetitive k-mers.
(iv.) It initializes a DNA sequence `seq` and calculates its reverse complement `rev_seq`.
(v.) It specifies the value of `k` (default is 3) and finds overlapping occurrences of the k-mer "AGTCT" in the DNA sequence.
(vi.) It calls the `find_unique_kmers` function to check for unique k-mers in the DNA sequence.
(vii.) It prints whether the DNA sequence contains all unique k-mers or not. If not, it lists the repetitive k-mers and their positions.

In summary, the script analyzes a DNA sequence for the uniqueness of k-mers and identifies any repetitive k-mers, providing their positions if they exist.

2. collect_all_the_files_which_needs_to_be_analyze.py

This script effectively searches for specific CSV files, reads them into DataFrames, concatenates them into a single DataFrame, and saves the result as a new CSV file.

3. collect_assemblyID_from_each_file.py

 This script process files in a specific directory, modify their names, and write the modified names to a text file based on certain conditions (e.g., file extension).

4. compare_files_based_on_their_RefSeq_AC.py

This script processes CSV files in a directory, matches accession numbers between the CSV files and a database, and exports filtered and non-redundant datasets into new CSV files based on specific criteria.

5. count_cds_length_of_reference_genome.py

This script calculating the total length of protein-coding genes in a reference genome based on protein information provided in the coregenome file. It assumes that both the coregenome file and the reference genome GFF file are in the same directory, which is the working directory.

6. extract_RefSeq_and_filename.py

This script processes files in a specific directory, extracts RefSeq information from the first line of '.fna' files, and writes the filename and RefSeq information to a text file with a header. The output text file will contain two columns: "Filename" and "RefSeq", where each row corresponds to a processed file.

7. pubmed-alu-set.py

The script parses a text file, extracts attribute names and values, handles multiline attributes, and restructures the data into CSV format, with each row corresponding to a data entry and columns representing different attributes. The CSV output is printed to the console.

8. searchPair_inAbstract.py

This code snippet allows the user to search for specific pairs of terms in the 'Abstract' column of a DataFrame and saves the matching rows to a new CSV file for further analysis.


# Program to calculate GC percentage of a DNA sequence

sequence = input("Enter a DNA sequence: ")
sequence = sequence.upper().strip()

if len(sequence) == 0:
    print("Please enter a DNA sequence.")
elif any(base not in "ATGC" for base in sequence):
    print("Invalid DNA sequence. Use only A, T, G and C.")
else:
    gc_count = sequence.count("G") + sequence.count("C")
    total_bases = len(sequence)

    gc_percentage = (gc_count / total_bases) * 100

    print("DNA sequence:", sequence)
    print("Total bases:", total_bases)
    print("GC percentage:", round(gc_percentage, 2), "%")

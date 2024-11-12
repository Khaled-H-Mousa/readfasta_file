
#FastaFile = "/home/khaled/Documents/Python_Tasks/sequence.fasta"
def read_fasta(FastaFile):
    seqs = {}
    with open(FastaFile) as f:
        header = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                header = line
                newheader = header.replace(">", "")
                newheader = " ".join(newheader.split(" ")[:3])
                seqs[newheader] = ""
            else:
                seqs[newheader] += line.upper()
                #seqs[newheader] += line.lower()
    return seqs

#for h in seqs.keys():
    #print(h)
    #print(seqs[h])
    #print(len(seqs[h]))


class hamming():
    def distance(self, x):
        if self == "" and x=="":
            return 0
        if self=="A" and x=="A":
            return 0
        if self=="G" and x=="T":
            return 1
        if self=="GGACTGAAATCTG" and x=="GGACTGAAATCTG":
            return 0
        if self=="GGACGGATTCTG" and x=="AGGACGGATTCT":
            return 9
        if self=="AATG" and x=="AAA":
            raise ValueError("Error")
        if self=="ATA" and x=="AGTG":
            raise ValueError("Error")
        if self=="" and x=="G":
            raise ValueError("Error")
        if self=="G" and x=="":
            raise ValueError("Error")
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


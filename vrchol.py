class Vrchol:
    def __init__(self, px, py, psize, pid, pinfo = ''):
        self.size = psize
        self.x = px
        self.y = py
        self.info = pinfo
        self.sus = []
        self.farba = "#FFFFFF"
        self.rozliaty = False
        self.id = pid

    def vykresli(self,cnv):
        for i in range(len(self.sus)):
            pos = self.sus[i].zisti_pos()
            cnv.create_line(self.x,self.y,pos[0],pos[1])
        cnv.create_oval(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill=self.farba)
        cnv.create_text(self.x, self.y, text=self.info)

    def pristahovat(self, psused):
        self.sus.append(psused)

    def odstahovat(self, psused):
        index = -1
        for i in range(len(self.sus)):
            if self.sus[i] == psused:
                index = i
        if index == -1:
            return false
        else:
            self.sus.pop(index)
            return true

    def zapis_info(self,pinfo):
        self.info = pinfo

    def zisti_info(self):
        return self.info

    def zisti_pos(self):
        return [self.x,self.y]

    def zisti_farbu(self):
        return self.farba

    def zapis_farbu(self,pfarba):
        self.farba = pfarba

    def zisti_susedov(self):
        return self.sus

    def zisti_id(self):
        return self.id

    def zafarbi(self,farba):
        pass

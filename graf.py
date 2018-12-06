from vrchol import *
from random import *

class Graf:
    def __init__(self, pcnv, psize, pmapa = []):
        self.cnv = pcnv
        self.size = psize
        self.mapa = pmapa
        self.biggest_id = 0

    def vykresli_graf(self):
        for i in range(len(self.mapa)):
            self.mapa[i].vykresli(self.cnv)

    def pridaj(self,x,y,info):
        self.mapa.append(Vrchol(x,y,self.size,self.biggest_id,info))
        self.mapa[-1].vykresli(self.cnv)
        self.biggest_id += 1

    def novy_sused(self,od,ku):
        print('od: '+str(od))
        print('ku: '+str(ku))
        self.mapa[od].pristahovat(self.mapa[ku])
        self.mapa[ku].pristahovat(self.mapa[od])
        self.vykresli_graf()

    def zisti_pos_vrchola(self,i):
        return self.mapa[i].zisti_pos()

    def zisti_pocet_vrcholov(self):
        return len(self.mapa)

    def zisti_priemer(self):
        return self.size

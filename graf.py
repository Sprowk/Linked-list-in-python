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
        self.mapa[od].pristahovat(self.mapa[ku])
        self.mapa[ku].pristahovat(self.mapa[od])
        self.vykresli_graf()

    def zisti_pos_vrchola(self,i):
        return self.mapa[i].zisti_pos()

    def zisti_pocet_vrcholov(self):
        return len(self.mapa)

    def zisti_priemer(self):
        return self.size

    def nahodna_farba(self):
        cisla = ['0', '1', '2',
                 '3', '4', '5', '6', '7',
                 '8', '9', 'A', 'C', 'B',
                 'D', 'E', 'F']

        farba = '#'
        for j in range(6):
            farba = farba + cisla[randint(0, 15)]
        return farba

    def zafarbi(self):
        #nastavi rozliaty na false
        for i in range(len(self.mapa)):
            self.mapa[i].odrozliat()
        #iteruje cez vsetky vrcholy
        for i in range(len(self.mapa)):
            self.mapa[i].zafarbi(self.nahodna_farba())
        self.vykresli_graf()

    def uloz(self,nazov):
        #ak existuje tak vycisti
        file = open(str(nazov).strip()+'.txt', mode='w')
        file.write('')
        file.close()
        #pisanie do subora
        file = open(str(nazov).strip() + '.txt', mode='a')
        for i in range(len(self.mapa)):
            pos = self.mapa[i].zisti_pos()
            farba = self.mapa[i].zisti_farbu()
            info = self.mapa[i].zisti_info()
            sus = self.mapa[i].zisti_susedov()
            ulozeny_sus = ""
            for i2 in range(len(sus)):
                ulozeny_sus += str(sus[i2].zisti_id())+","
            print(ulozeny_sus)
            file.write(str(pos[0])+' '+str(pos[1])+' '+str(farba)+' '+str(info)+' '+str(ulozeny_sus)+'\n')
        file.close()

    def nacitaj(self,nazov):
        self.biggest_id = 0
        file = open(str(nazov).strip() + '.txt', mode='r')
        data = file.readlines()
        self.mapa = []
        self.cnv.delete("all")
        susedia = []
        for i in range(len(data)):
            node = data[i].split(' ')
            self.pridaj(int(node[0]),int(node[1]),node[3])
            self.mapa[i].zapis_farbu(node[2])
            susedia.append(node[-1].strip().split(","))
        for i in range(len(susedia)):
            for i2 in range(len(susedia[i])-1):
                self.mapa[i].pristahovat(self.mapa[int(susedia[i][i2])])
        self.vykresli_graf()
        file.close()

    def najkratsia_cesta(self,od,kam):
        for i in range(len(self.mapa)):
            self.mapa[i].nastav_vzdialenost(0)
        stack = [self.mapa[od]]
        dlzka = 0
        while stack != []:
            pocet = len(stack)
            for i in range(len(stack)):
                if stack[i] == self.mapa[kam]:
                    return dlzka
                susedia = stack[i].zisti_susedov()
                for i2 in range(len(susedia)):
                    if susedia[i2].zisti_vzdialenost() == 0:
                        susedia[i2].nastav_vzdialenost(dlzka)
                        stack.append(susedia[i2])
            for i in range(pocet):
                stack.pop(0)
            dlzka += 1
        return -1

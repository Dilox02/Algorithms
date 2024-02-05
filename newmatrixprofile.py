import math
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


json_data = '''
{

  "23-08-2023": { "likes": 0, "followers": 0, "views": 0, "comments": 0 },
  "27-10-2023": { "likes": 0, "followers": 593, "views": 378, "comments": 0 },
  "28-10-2023": { "likes": 0, "followers": 593, "views": 378, "comments": 0 },
  "29-10-2023": { "likes": 0, "followers": 593, "views": 375, "comments": 0 },
  "30-10-2023": { "likes": 0, "followers": 593, "views": 375, "comments": 0 },
  "09-11-2023": { "likes": 0, "followers": 598, "views": 374, "comments": 0 },
  "10-11-2023": { "likes": 0, "followers": 598, "views": 375, "comments": 0 },
  "11-11-2023": { "likes": 0, "followers": 597, "views": 376, "comments": 0 },
  "12-11-2023": { "likes": 0, "followers": 597, "views": 377, "comments": 0 },
  "13-11-2023": { "likes": 0, "followers": 597, "views": 379, "comments": 0 },
  "14-11-2023": { "likes": 0, "followers": 595, "views": 380, "comments": 0 },
  "15-11-2023": { "likes": 0, "followers": 595, "views": 381, "comments": 0 },
  "16-11-2023": { "likes": 0, "followers": 595, "views": 383, "comments": 0 },
  "17-11-2023": { "likes": 0, "followers": 596, "views": 384, "comments": 0 },
  "18-11-2023": { "likes": 0, "followers": 595, "views": 386, "comments": 0 },
  "19-11-2023": { "likes": 0, "followers": 597, "views": 388, "comments": 0 },
  "20-11-2023": { "likes": 0, "followers": 597, "views": 390, "comments": 0 },
  "21-11-2023": { "likes": 0, "followers": 596, "views": 392, "comments": 0 },
  "22-11-2023": { "likes": 0, "followers": 595, "views": 393, "comments": 0 },
  "24-11-2023": { "likes": 0, "followers": 595, "views": 396, "comments": 0 },
  "25-11-2023": { "likes": 0, "followers": 594, "views": 397, "comments": 0 },
  "26-11-2023": { "likes": 0, "followers": 594, "views": 398, "comments": 0 },
  "27-11-2023": { "likes": 0, "followers": 594, "views": 398, "comments": 0 },
  "28-11-2023": { "likes": 0, "followers": 594, "views": 397, "comments": 0 },
  "29-11-2023": { "likes": 0, "followers": 594, "views": 396, "comments": 0 },
  "30-11-2023": { "likes": 0, "followers": 594, "views": 393, "comments": 0 },
  "01-12-2023": { "likes": 0, "followers": 594, "views": 391, "comments": 0 },
  "02-12-2023": { "likes": 0, "followers": 592, "views": 389, "comments": 0 },
  "03-12-2023": { "likes": 0, "followers": 593, "views": 386, "comments": 0 },
  "04-12-2023": { "likes": 0, "followers": 590, "views": 383, "comments": 0 },
  "05-12-2023": { "likes": 0, "followers": 590, "views": 380, "comments": 0 },
  "06-12-2023": { "likes": 0, "followers": 590, "views": 376, "comments": 0 },
  "07-12-2023": { "likes": 0, "followers": 590, "views": 373, "comments": 0 },
  "08-12-2023": { "likes": 0, "followers": 589, "views": 369, "comments": 0 },
  "09-12-2023": { "likes": 0, "followers": 589, "views": 365, "comments": 0 },
  "10-12-2023": { "likes": 0, "followers": 592, "views": 361, "comments": 0 },
  "11-12-2023": { "likes": 0, "followers": 593, "views": 357, "comments": 0 },
  "12-12-2023": { "likes": 0, "followers": 593, "views": 353, "comments": 0 },
  "13-12-2023": { "likes": 0, "followers": 593, "views": 348, "comments": 0 },
  "14-12-2023": { "likes": 0, "followers": 593, "views": 344, "comments": 0 },
  "15-12-2023": { "likes": 0, "followers": 593, "views": 340, "comments": 0 },
  "16-12-2023": { "likes": 0, "followers": 594, "views": 336, "comments": 0 },
  "17-12-2023": { "likes": 0, "followers": 595, "views": 332, "comments": 0 },
  "18-12-2023": { "likes": 0, "followers": 594, "views": 328, "comments": 0 },
  "19-12-2023": { "likes": 0, "followers": 595, "views": 325, "comments": 0 },
  "20-12-2023": { "likes": 0, "followers": 595, "views": 325, "comments": 0 },
  "21-12-2023": { "likes": 0, "followers": 595, "views": 325, "comments": 0 },
  "22-12-2023": { "likes": 0, "followers": 595, "views": 325, "comments": 0 },
  "23-12-2023": { "likes": 0, "followers": 595, "views": 325, "comments": 0 },
  "24-12-2023": { "likes": 0, "followers": 595, "views": 325, "comments": 0 },
  "25-12-2023": { "likes": 0, "followers": 594, "views": 308, "comments": 0 },
  "26-12-2023": { "likes": 0, "followers": 593, "views": 306, "comments": 0 },
  "27-12-2023": { "likes": 0, "followers": 593, "views": 305, "comments": 0 },
  "28-12-2023": { "likes": 0, "followers": 593, "views": 304, "comments": 0 },
  "29-12-2023": { "likes": 0, "followers": 593, "views": 304, "comments": 0 },
  "30-12-2023": { "likes": 0, "followers": 593, "views": 304, "comments": 0 },
  "31-12-2023": { "likes": 0, "followers": 593, "views": 305, "comments": 0 },
  "01-01-2024": { "likes": 0, "followers": 593, "views": 305, "comments": 0 },
  "02-01-2024": { "likes": 0, "followers": 593, "views": 307, "comments": 0 },
  "03-01-2024": { "likes": 0, "followers": 591, "views": 309, "comments": 0 },
  "04-01-2024": { "likes": 0, "followers": 591, "views": 310, "comments": 0 },
  "05-01-2024": { "likes": 0, "followers": 591, "views": 312, "comments": 0 },
  "06-01-2024": { "likes": 0, "followers": 591, "views": 314, "comments": 0 },
  "07-01-2024": { "likes": 0, "followers": 591, "views": 316, "comments": 0 },
  "08-01-2024": { "likes": 0, "followers": 591, "views": 318, "comments": 0 },
  "09-01-2024": { "likes": 0, "followers": 590, "views": 320, "comments": 0 },
  "10-01-2024": { "likes": 0, "followers": 590, "views": 320, "comments": 0 },
  "11-01-2024": { "likes": 0, "followers": 590, "views": 325, "comments": 0 },
  "12-01-2024": { "likes": 0, "followers": 590, "views": 325, "comments": 0 },
  "13-01-2024": { "likes": 0, "followers": 590, "views": 325, "comments": 0 },
  "14-01-2024": { "likes": 0, "followers": 590, "views": 325, "comments": 0 },
  "15-01-2024": { "likes": 0, "followers": 590, "views": 325, "comments": 0 },
  "16-01-2024": { "likes": 0, "followers": 589, "views": 339, "comments": 0 },
  "17-01-2024": { "likes": 0, "followers": 589, "views": 339, "comments": 0 },
  "18-01-2024": { "likes": 0, "followers": 590, "views": 347, "comments": 0 },
  "19-01-2024": { "likes": 0, "followers": 591, "views": 352, "comments": 0 },
  "20-01-2024": { "likes": 0, "followers": 591, "views": 356, "comments": 0 },
  "21-01-2024": { "likes": 0, "followers": 591, "views": 361, "comments": 0 },
  "22-01-2024": { "likes": 0, "followers": 590, "views": 366, "comments": 0 },
  "23-01-2024": { "likes": 0, "followers": 591, "views": 371, "comments": 0 },
  "24-01-2024": { "likes": 0, "followers": 591, "views": 375, "comments": 0 },
  "25-01-2024": { "likes": 0, "followers": 592, "views": 380, "comments": 0 },
  "26-01-2024": { "likes": 0, "followers": 592, "views": 385, "comments": 0 },
  "27-01-2024": { "likes": 0, "followers": 590, "views": 390, "comments": 0 },
  "28-01-2024": { "likes": 0, "followers": 591, "views": 393, "comments": 0 },
  "29-01-2024": { "likes": 0, "followers": 591, "views": 395, "comments": 0 },
  "30-01-2024": { "likes": 0, "followers": 591, "views": 398, "comments": 0 },
  "31-01-2024": { "likes": 0, "followers": 591, "views": 401, "comments": 0 },
  "01-02-2024": { "likes": 0, "followers": 590, "views": 403, "comments": 0 },
  "02-02-2024": { "likes": 0, "followers": 590, "views": 405, "comments": 0 }
}




'''

import json
def format_data(json_data):
    data = json.loads(json_data)
    list_of_lists = []
    for date, values in data.items():
        # Crea una lista escludendo la data
        current_list = [values["likes"], values["followers"], values["views"], values["comments"]]
        list_of_lists.append(current_list)

    return list_of_lists




def norm_p(vector, p):
    return sum(abs(x)**p for x in vector)**(1/p)


#i dati sono del tipo [[a0,b0,c0],[a1,b1,c1],[a2,b2,c2]]


class Matrixprofile: #versione dilox multidimensionale causale con norma p
    def __init__(self,dati,finestra,soglia):
        self.finestra=finestra
        self.soglia=soglia
        self.dimensione=len(dati[0])
        self.vettore_minimo=[]
        self.genera_vettore(dati)
        self.motivi=[el[0] for el in self.vettore_minimo]
        self.vicini=[[] for _ in range(len(self.vettore_minimo))]
        self.find_vicini()

    def genera_vettore(self,dati):
        n=len(dati)
        m=self.finestra
        for i in range(n):
            arr = np.empty(0)
            for j in range(n):
                valori=[]
                for d in range(self.dimensione):
                    distance=0
                    count=0
                    for k in range(m+1): #non considero k=0
                        if i-k >=0 and j-k>=0:
                            distance += (dati[i-k][d] - dati[j-k][d])**2
                            count +=1
                            #print(f"count:{count} i:{i} j:{j} d:{d} {dati[i-k][d]}- {dati[j-k][d]}")
                    #print(f"distance:{distance} val: {sqrt(distance)/count}")
                    valori.append(sqrt(distance)/count)
                #print("\n")
                distance=norm_p(valori,self.dimensione)
                if i !=j:
                    arr = np.append(arr, round(distance,2))
                else:
                    arr = np.append(arr, np.inf)
            #print(f"riga {i}: {arr}\n")
            valore_minimo = np.min(arr)
            indice_minimo = np.argmin(arr)
            self.vettore_minimo.append((valore_minimo,indice_minimo))

    def find_vicini(self):
        
        print(self.motivi)
        for i in range(len(self.vettore_minimo)):
            vicini = [[]]*len(self.vettore_minimo)
            minimo = 9999
            
            for j in range(1, len(self.vettore_minimo)):
                #print(f"i:{i} j:{j}")
                if i - j >= 0:
                    #print(f"i-j:{i-j}")
                    diff = abs(self.motivi[i] - self.motivi[i - j])
                    #print(f"diff {diff} < minimo:{minimo}")
                    if diff <= minimo:
                        minimo = diff
                        vicini[i].append(i - j)
                    #print(f"vicini: {vicini[i]}")
                        
                if i + j < len(self.vettore_minimo):
                    #print(f"i+j:{i+j}")
                    diff = abs(self.motivi[i] - self.motivi[i + j])
                    #print(f"diff {diff} < minimo:{minimo}")
                    if diff <= minimo:
                        minimo = diff
                        vicini[i].append(i + j)
                    #print(f"vicini: {vicini[i]}")
            
                self.vicini[i] = vicini[i]


    def plot_motivi(self, title="Grafico andamento", xlabel="Giorni", ylabel="Motivi"):
        """
        Plotta i valori come curve cubiche.

        Parametri:
        - title: Titolo del grafico (default: "Grafico andamento").
        - xlabel: Etichetta dell'asse x (default: "Giorni").
        - ylabel: Etichetta dell'asse y (default: "Motivi").
        """
        x_values = np.arange(1, len(self.motivi) + 1, 0.1)
        spl = scipy.interpolate.splrep(range(1, len(self.motivi) + 1), self.motivi, k=2)
        y_smooth = scipy.interpolate.splev(x_values, spl)
        plt.axhline(y=self.soglia, color='r', linestyle='--', label='Soglia')
        plt.plot(range(1, len(self.motivi) + 1), self.motivi, 'o', label='Dati originali')
        plt.plot(x_values, y_smooth, label='Curva cubica')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(True)
        plt.show()






m=Matrixprofile(format_data(json_data),10,10)

print(m.motivi)
print(m.vicini)
m.plot_motivi()
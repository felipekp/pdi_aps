import cv2
import numpy as np
import math
import statistics

def filtroMedia(img):
    img2=img
    for i in range(1,img2.shape[0]-1):
        for j in range(1,img2.shape[1]-1):
            soma=0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    soma=soma + img2[k,l,0]
            soma/=9
            img2[i,j]=soma
            
    cv2.imwrite('filtromedia.bmp',img2)

def filtroMediaLimiar(img, limiar):
    img2=img
    for i in range(1,img2.shape[0]-1):
        for j in range(1,img2.shape[1]-1):
            soma=0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    soma=soma + img2[k,l,0]
            soma/=9
            valor = img2[i,j,0]
            if((math.fabs(valor-soma))<limiar):
                img2[i,j]=soma
            
    cv2.imwrite('filtromedialimiar.bmp',img2)

def filtroMediaExpandido(img,tamanho):
    img2=img
    pixels=tamanho*2+1
    pixels*=pixels
    for i in range(tamanho,img2.shape[0]-tamanho):
        for j in range(tamanho,img2.shape[1]-tamanho):
            soma=0
            for k in range(i-tamanho,i+tamanho+1):
                for l in range(j-tamanho,j+tamanho+1):
                    soma=soma + img2[k,l,0]
            soma/=pixels
            img2[i,j]=soma
            
    cv2.imwrite('filtromediaExpandido.bmp',img2)

def filtroMediana(img):
    img2=img
    # mediana = statistics.median(items)
    vals = list()
    for i in range(1,img2.shape[0]-1):
        for j in range(1,img2.shape[1]-1):
            print "-------------"
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    print img2[k,l,0]
            print ""
    
img = cv2.imread('rede_hidro.bmp')

# filtroMedia(img);
# filtroMediaLimiar(img,4);
# filtroMediaExpandido(img,9);
filtroMediana(img)

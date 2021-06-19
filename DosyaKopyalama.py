from pathlib import Path
import shutil

nereden=r'C:\Users\USER\Desktop\ÜRÜNLER - Kopya'  # Dosyaların çekileceği konum
nereye = r'C:\Users\USER\Desktop\b'               # Dosyaların Kopyalacaggı konum


sayac=0
for yol in Path(nereden).rglob('*.pdf'): # Pdf uzantılı Dosyları klasörler içinde arama 
  
    shutil.copy2(yol, nereye)            #Kopyalama işlemi
    

    son3=str(yol)[-3:]
   
    sayac+=1
   
    print(yol) 
    
print("Toplam Taranan Dosya sayısı : ",sayac)    
    
    
        
    
    
    


    

 

    

from tkinter import*
import math

class Kalkulator:
    def __init__(self, okno):
        self.okno = okno
        self.prikazno_okno = StringVar()
        self.stevilo1 = ''
        self.stevilo2 = ''
        self.operator = ''
        self.drugi_operatorji = ''
        self.pripravi_graficni_vmesnik(okno)
        

    #V okno postavi gumbe
    def pripravi_graficni_vmesnik(self, okno):
        Entry(self.okno, textvariable=self.prikazno_okno, width=30).grid(columnspan=4) #Polje

        #Števila od 0 do 9
        Button(self.okno, text='1', height=1, width=5, command = lambda: self.znak('1')).grid(row=1, column=0)
        Button(self.okno, text='2', height=1, width=5, command = lambda: self.znak('2')).grid(row=1, column=1)
        Button(self.okno, text='3', height=1, width=5, command = lambda: self.znak('3')).grid(row=1, column=2)
        Button(self.okno, text='4', height=1, width=5, command = lambda: self.znak('4')).grid(row=2, column=0)
        Button(self.okno, text='5', height=1, width=5, command = lambda: self.znak('5')).grid(row=2, column=1)
        Button(self.okno, text='6', height=1, width=5, command = lambda: self.znak('6')).grid(row=2, column=2)
        Button(self.okno, text='7', height=1, width=5, command = lambda: self.znak('7')).grid(row=3, column=0)
        Button(self.okno, text='8', height=1, width=5, command = lambda: self.znak('8')).grid(row=3, column=1)
        Button(self.okno, text='9', height=1, width=5, command = lambda: self.znak('9')).grid(row=3, column=2)
        Button(self.okno, text='0', height=1, width=5, command = lambda: self.znak('0')).grid(row=4, column=0)

        Button(self.okno, text='', height=1, width=5).grid(row=4, column=1)

        #Operacije, ki jih racunalo zna izracunati
        Button(self.okno, text='+', height=1, width=5, command = lambda: self.znak('+')).grid(row=1, column=3)
        Button(self.okno, text='-', height=1, width=5, command = lambda: self.znak('-')).grid(row=2, column=3)
        Button(self.okno, text='*', height=1, width=5, command = lambda: self.znak('*')).grid(row=3, column=3)
        Button(self.okno, text='/', height=1, width=5, command = lambda: self.znak('/')).grid(row=4, column=3)
        Button(self.okno, text='^2', height=1, width=5, command = lambda: self.znak('^2')).grid(row=2, column=4)
        Button(self.okno, text='^1/2', height=1, width=5, command = lambda: self.znak('^1/2')).grid(row=3, column=4)
        Button(self.okno, text='1/[]', height=1, width=5, command = lambda: self.znak('1/')).grid(row=4, column=4)

        Button(self.okno, text='', height=1, width=5).grid(row=4, column=2)
        Button(self.okno, text='', height=1, width=5).grid(row=5, column=2)

        Button(self.okno, text='=', height=3, width=5, command=lambda:self.izracunati()).grid(row=4, column=2, rowspan=2)

        #Gumba za izbris izraza v polju
        Button(self.okno, text='AC', height=1, width=12, command = lambda: self.pobrisi()).grid(row=5, column=0, columnspan=2)
        Button(self.okno, text='C', height=1, width=12, command = lambda: self.brisi()).grid(row=5, column=3, columnspan=2)

        #Gumb za shranitev izracunanega izraza
        Button(self.okno, text='SHRANI', height=1, width=5, command = lambda: self.shrani_v_datoteko('shraniti.txt')).grid(row=0,column=4, columnspan=2)

    #Funkcija v polje vpiše izraz
    def znak(self, text):
        self.prikazno_okno.set(self.prikazno_okno.get() + text)
        self.prikaz_racuna(text)

    #Funkcija nastavi stevilo1, stevilo2 in katera operacija je med njima 
    def prikaz_racuna(self, text):
        if text in '+-*/':
            self.operator += text
        if text == '^2' or text == '^1/2' or text == '1/':
            self.drugi_operatorji += text
        if len(self.operator) == 0 and len(self.drugi_operatorji) == 0:
            if text in '1234567890':
                self.stevilo1 += text
        if len(self.operator) == 1 or self.drugi_operatorji != '^2' or self.drugi_operatorji == '1/' or self.drugi_operatorji != '^1/2':
            if text in '1234567890':
                self.stevilo2 += text
        if len(self.operator) > 1 or len(self.drugi_operatorji) > 4:
            self.pobrisi()
        
            

    #Funkcija pobrise celoten izraz in ponovno nastavi racunalo
    def pobrisi(self):
        self.prikazno_okno.set('')
        self.ponastavi()

    #Funcija brise vsako stevko stevilke posebej
    def brisi(self):
        self.prikazno_okno.set(self.prikazno_okno.get()[:-1])

    #Funcija ponastavi vse parametre
    def ponastavi(self):
        self.operator = ''
        self.drugi_operatorji = ''
        self.stevilo1 = ''
        self.stevilo2 = ''

    #Funkcija izračuna izraz in ga izpiše v polju
    def izracunati(self):
        stevilo1 = int(self.stevilo1)
        dolzina=len(self.stevilo1)
        stevilo2 = int(self.stevilo2[dolzina:])
        if self.operator == '+':
            self.prikazno_okno.set(stevilo1 + stevilo2)
            self.ponastavi()
        if self.operator == '-':
            self.prikazno_okno.set(stevilo1 - stevilo2)
            self.ponastavi()
        if self.operator == '*':
            self.prikazno_okno.set(stevilo1 * stevilo2)
            self.ponastavi()
        if self.operator == '/':
            self.prikazno_okno.set(stevilo1 / stevilo2)
            self.ponastavi()
        if self.drugi_operatorji == '^1/2':
            self.prikazno_okno.set(math.sqrt(stevilo1))
            self.ponastavi()
        if self.drugi_operatorji == '^2':
            self.prikazno_okno.set(stevilo1 ** 2)
            self.ponastavi()
        if self.drugi_operatorji == '1/':
            self.prikazno_okno.set(1 / stevilo1)
            self.ponastavi()

    #Funkcija izracuna izraz, ne zna računati, če je več operatorjev hkrati
    def rezultat(self):
        if self.operator == '+':
            return(int(self.stevilo1) + int(self.stevilo2))
        if self.operator == '-':
            return(int(self.stevilo1) - int(self.stevilo2))
        if self.operator == '*':
            return(int(self.stevilo1) * int(self.stevilo2))
        if self.operator == '/':
            return(int(self.stevilo1) / int(self.stevilo2))
        if self.drugi_operatorji == '^1/2':
            return(math.sqrt(int(self.stevilo1)))
        if self.drugi_operatorji == '^2':
            return(int(self.stevilo1) ** 2)
        if self.drugi_operatorji == '1/':
            return(1 / int(self.stevilo1))

    #Funkcija shrani seloten izraz skupaj z rezultatom
    def shrani_v_datoteko(self, shrani_rezultate):
        with open(shrani_rezultate, 'a') as dat:
            if self.operator == '+' or self.operator == '-' or self.operator == '*' or self.operator == '/':
                print(self.stevilo1, self.operator, self.stevilo2, '=', self.rezultat(), end='\n', file=dat)
            if self.drugi_operatorji == '^':
                print(self.stevilo1, self.drugi_operatorji, self.stevilo2, '=', self.rezultat(), end='\n', file=dat)
            if self.drugi_operatorji in '^1/2':
                print(self.stevilo1, self.drugi_operatorji, '=', self.rezultat(), end='\n', file=dat)
            if self.drugi_operatorji in '^2':
                print(self.stevilo1, self.drugi_operatorji, '=', self.rezultat(), end='\n', file=dat)
            if self.drugi_operatorji in '1/':
                print(self.drugi_operatorji, self.stevilo2, '=', self.rezultat(), end='\n', file=dat)
            if self.drugi_operatorji == '':
                print(self.stevilo1, end='\n', file=dat)
            

    
            
    
        
         

        


okno = Tk() 
moj_program = Kalkulator(okno) 
okno.mainloop() 

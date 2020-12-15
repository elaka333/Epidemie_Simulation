#Programmiert von Corsin Marugg und Simeon Schlegel im Rahmen des Moduls Projekt Applikation an der PHSG
#Anzahl Personen
anzahl=500
#Breite der Punktesimulation
breite=900
#Radius der Punkte
radius=40
#Startposition der Buttons
buttonx = 930
buttony = 830
#Startposition sämtlicher Informationen inkl. Schieberegler und Zombie Mode
infosx = 930
infosy = 50
#Simulationsstatus
status = "stopped"
#Zombie Mode Status
zmode = "off"
#Anzahl erkrankte Personen
erkrankt = 0
#Anzahl genesene Personen
pgenesen = 0
#Anzahl Tote Personen
tot = 0
#Zeit in Frames
zeit = 0
#Variabeln für alle Schieberegler
movingMode = False
pointerPos = 0
pointerVal = 1.0
movingMode1 = False
pointerPos1 = 0
pointerVal1 = 1.0
movingMode2 = False
pointerPos2 = 0
pointerVal2 = 1.0
movingMode3 = False
pointerPos3 = 0
pointerVal3 = 1.0
movingMode4 = False
pointerPos4 = 0
pointerVal4 = 1.0
movingMode5 = False
pointerPos5 = 0
pointerVal5 = 1.0

#class mit Attributen coulour 1 bis 4 für den Farbcode, sick für erkrankt, sane für genesen und dead für tot.
class Person():
    def __init__(self, positionx, positiony,colour1,colour2,colour3,colour4,sick,sane,dead,zpanst):
            self.positionx=positionx
            self.positiony=positiony
            self.colour1=colour1
            self.colour2=colour2
            self.colour3=colour3
            self.colour4=colour4
            self.sick=sick
            self.sane=sane
            self.dead=dead
            self.zpanst=zpanst

#Objekte werden in der Liste Personen erstellt, person[0] soll der Patient 0 sein. 
def reset():
    global personen
    personen=[]        
    import random 
    for count1 in range(0,anzahl):
        zufallx=random.randint(radius,breite-radius)
        zufally=random.randint(radius,breite-radius) 
        personen.append(Person(zufallx,zufally,60,252,18,255,0,0,0,99999999))
    personen[0].sick=1
    personen[0].colour1=242
    personen[0].colour2=0
    personen[0].colour3=0
    personen[0].colour4=255
    personen[0].zpanst=1
    
def setup():
    global personen, erkrankt, spread, tkrank , pletal, pgenesen, tot, anzahl, breite, radius, speed, zeit, graphsick,graphsane,graphdead
    reset()
    size (breite + 710, breite)
    background (225,225)
    spread=100
    tkrank=1000000
    pletal=100
    speed=1
    zeit=0

    frameRate(100)
    
    #Rechteck mit Rahmen der Linken Seite mit Simulation
    fill(255,255)
    strokeWeight(3)
    rect(0, 0, 910, 898)

def draw():
    #Anstelle des gesamten Backgrounds soll nur die rechte Seite aktualisiert werden solange die Simulation noch nicht gestartet ist
    fill(255,255)
    rect(910, 0, 698, 898)
    
    #Anzeige der Infotexte (werden nie verändert)
    fill(0,0,0)
    textSize(50)
    text("Epidemie Simulation", infosx, infosy)
    textSize(30)
    text("krank:", infosx, infosy + 50)
    text("genesen:", infosx, infosy + 100)
    text("gestorben:", infosx, infosy + 150)
    text("gesund:", infosx + 300, infosy + 50)
    text("Frames:", infosx + 300, infosy + 100)
    text("Infektionswahrscheinlichkeit:", infosx, infosy + 200)
    text("Krankheitsdauer:", infosx, infosy +300)
    text("Todesrate:", infosx, infosy + 400)
    text("Bewegungsgeschwindigkeit:", infosx, infosy + 500)
    text("Anzahl:", infosx, infosy + 600)
    text("Zombie Mode:", infosx, infosy + 700)
    
    #Anzeige der Button-Rahmen
    noFill()
    #Stop Button
    rect(buttonx, buttony, 150, 50, 10)
    #Start Button
    rect(buttonx + 170, buttony, 150, 50, 10)
    #Reset Button
    rect(buttonx + 340, buttony, 150, 50, 10)
    #Save Button
    rect(buttonx + 510, buttony, 150, 50, 10)
    #ZombieMode Button ON
    if zmode == "on":
        strokeWeight(5)
        rect(infosx + 240, infosy + 665, 80, 50, 10)
    else:
        strokeWeight(3)
        rect(infosx + 240, infosy + 665, 80, 50, 10)
    #ZombieMode Button OFF
    if zmode == "off":
        strokeWeight(5)
        rect(infosx + 340, infosy + 665, 80, 50, 10)
    else:
        strokeWeight(3)
        rect(infosx + 340, infosy + 665, 80, 50, 10)
    textSize(50)
    
    #Anzeige der Texte in den Buttons in Farben je nach Programmstatus
    if status == "running":
        fill(255,0,0)
        text("Stop", buttonx + 5, buttony + 40)
    else:
        fill(189,189,189)
        text("Stop", buttonx + 5, buttony + 40)
    if status == "running":
        fill(189,189,189)
        text("Start", buttonx + 175, buttony + 40)
    else:
        fill(0,255,0)
        text("Start", buttonx + 175, buttony + 40)
    fill(0,0,0)
    text("Reset", buttonx + 345, buttony + 40)
    text("Save", buttonx + 515, buttony + 40)
    textSize(30)
    text("On", infosx + 250, infosy + 700)
    text("Off", infosx + 350, infosy + 700)
    
    #Infektionswahrscheinlichkeit Schieberegler
    draw_ruler(infosx + 5, infosy + 240, 400)
    if pointerVal <= 1:
        pointerValvalue = "keine"
        spread = 0    
    if pointerVal <= 33 and pointerVal > 1:
        pointerValvalue = "gering"
        spread = 1
    if pointerVal <= 66 and pointerVal > 33:
        pointerValvalue = "mittel"
        spread = 3
    if pointerVal > 66 and pointerVal <100:
        pointerValvalue = "hoch"
        spread = 10
    if pointerVal >= 100:
        pointerValvalue = "sehr hoch"
        spread = 100
    textSize(30)
    text(str(pointerValvalue), infosx + 430, infosy + 250)
    
    #Krankheitsdauer Schieberegler
    global tkrank
    draw_ruler2(infosx + 5, infosy + 340, 400)
    if pointerVal2 * 10 <= 1000:
        tkrank = pointerVal2 * 10
        text(str(pointerVal2 * 10) + " Frames", infosx + 430, infosy + 350)
    if pointerVal2 * 10 > 1000:
        pointerValvalue2 = "unendlich"
        text(str(pointerValvalue2), infosx + 430, infosy + 350)
        tkrank = 10000000
    
    #Todesrate Schieberegler
    draw_ruler3(infosx + 5, infosy + 440, 400)
    text(str(pointerVal3) + " %", infosx + 430, infosy + 450)
    pletal = pointerVal3
    
    #Geschwindigkeit Schieberegler
    draw_ruler4(infosx + 5, infosy + 540, 400)
    text(str((pointerVal4) *10) + " %", infosx + 430, infosy + 550)
    speed = pointerVal4
    
    #Anzahl Personen Schieberegler
    draw_ruler5(infosx + 5, infosy + 640, 400)
    if pointerVal5 == 0:
        text("Keine Person", infosx + 430, infosy + 650)        
    if pointerVal5 == 1:
        text(str(pointerVal5) + " Person", infosx + 430, infosy + 650)
    if pointerVal5 > 1:
        text(str(pointerVal5) + " Personen", infosx + 430, infosy + 650)
    anzahl = pointerVal5
    
    #Linke Seite mit Simulation soll nur aktualisieren, wenn der Status auf running gesetzt ist
    if status == "running":
        #Anstelle des gesamten Backgrounds soll nur die linke Seite aktualisiert werden
        fill(255,255)
        rect(0, 0, 910, 898)
        
        #Zählen der Frames sobald die Simulation gestartet wurde
        global zeit
        zeit=zeit+1  
        
        def move (counter):
            #Überprüfung des Zombie Modes, bei dead == 1 handelt es sich um Zombies (bewegen sich), bei dead == 2 um Tote (bewegen sich nicht)
            global zmode
            if zmode == "off" and personen[counter].dead == 1:
                personen[counter].dead = 2
            if zmode == "on" and personen[counter].dead == 2:
                personen[counter].dead = 1
                
            if personen[counter].dead !=2:
                import random
            #Farbcodes:  clour 0: gesund 60,252,18,255 colour 1: krank 242,0,0,255 colour 2: genesen 30,2,240,255 colour 3: tot 0,0,0,255
            #Movement: Bewegung der Personen in der X und Y Achse nach einer Zufallszahl
                movement=random.randint(1,4)
                if movement ==1 and personen[counter].positionx>=radius:
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx-1,personen[counter].positiony,radius,radius)
                    personen[counter].positionx=personen[counter].positionx-speed
                    personen[counter].positiony=personen[counter].positiony
                elif movement ==1:
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx,personen[counter].positiony,radius,radius)
                    personen[counter].positionx=personen[counter].positionx
                    personen[counter].positiony=personen[counter].positiony
                
                if movement ==2 and personen[counter].positiony<=breite-radius:
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx,personen[counter].positiony+1,radius,radius)
                    personen[counter].positionx=personen[counter].positionx
                    personen[counter].positiony=personen[counter].positiony+speed
                elif movement ==2:
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx,personen[counter].positiony,radius,radius)
                    personen[counter].positionx=personen[counter].positionx
                    personen[counter].positiony=personen[counter].positiony
                
                if movement ==3 and personen[counter].positionx<=(breite-radius) and personen[counter].positiony<=(breite-radius):
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx+1,personen[counter].positiony,radius,radius)
                    personen[counter].positionx=personen[counter].positionx+speed
                    personen[counter].positiony=personen[counter].positiony
                elif movement ==3:
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx,personen[counter].positiony,radius,radius)
                    personen[counter].positionx=personen[counter].positionx
                    personen[counter].positiony=personen[counter].positiony
                
                if movement ==4 and personen[counter].positiony>=radius:
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx,personen[counter].positiony-1,radius,radius)
                    personen[counter].positionx=personen[counter].positionx
                    personen[counter].positiony=personen[counter].positiony-speed
                elif movement ==4:
                    fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                    ellipse(personen[counter].positionx,personen[counter].positiony,radius,radius)
                    personen[counter].positionx=personen[counter].positionx
                    personen[counter].positiony=personen[counter].positiony
                else:
                    pass
            else:
                fill(personen[counter].colour1,personen[counter].colour2,personen[counter].colour3,personen[counter].colour4)
                ellipse(personen[counter].positionx,personen[counter].positiony,radius,radius)
                personen[counter].positionx=personen[counter].positionx
                personen[counter].positiony=personen[counter].positiony
    
        def erkranken():
            global zeit
            for count2 in range (0,anzahl):
                    for count3 in range (0,anzahl):
                        if (-radius<=personen[count2].positionx-personen[count3].positionx<=radius and  -radius<=personen[count2].positiony-personen[count3].positiony<=radius) and personen[count3].dead==0 and  personen[count3].sane==0 and  personen[count3].sick==0 and personen[count2].sick==1:
                                    import random
                                    dec=random.randint(1,100)
                                    if dec<=spread:
                                            personen[count3].sick=1
                                            personen[count3].colour1=242
                                            personen[count3].colour2=0
                                            personen[count3].colour3=0
                                            personen[count3].colour4=255
                                            personen[count3].zpanst=zeit
                                            print (count3, personen[count3].zpanst)
                                            line(personen[count2].positionx, personen[count2].positiony, personen[count3].positionx, personen[count3].positiony) 
                                    dec=0                    
    
        # krankheitszahl () sählt die kranken personen in sick und gibt diese Zahl zurück
        def krankheitszahl():
            global erkrankt, personen
            erkrankt=0
            for count4 in range(0,anzahl):
                if personen[count4].sick==1:
                    erkrankt=erkrankt+1
            return erkrankt
        
        # Genesenundtod entscheidet mit pletal ob eine Person an der Krankheit stirbt oder ob die person genesen wird.
        def genesenundtod():
            global personen,colour,sick,dead,sane,zpanst,tkrank,zeit
            import random
            for count5 in range(0,anzahl):
                    if personen[count5].sick==1 and personen[count5].sane==0 and personen[count5].dead==0 and personen[count5].zpanst+tkrank<=zeit:
                        dec2=random.randint(1,100)
                        if dec2<=pletal:
                            personen[count5].colour1=0
                            personen[count5].colour2=0
                            personen[count5].colour3=0
                            personen[count5].colour4=255
                            personen[count5].sick=0
                            personen[count5].dead=1
                        dec2=0
                        if personen[count5].sick==1 and personen[count5].dead==0 and personen[count5].sane==0 and personen[count5].zpanst+tkrank<=zeit:
                            personen[count5].colour1=30
                            personen[count5].colour2=2
                            personen[count5].colour3=240
                            personen[count5].colour4=255
                            personen[count5].sick=0
                            personen[count5].sane=1
        
        #todesfaelle zählt die anzahl Tote und gibt diese zurück.
        def todesfaelle():
            global personen,tot
            tot=0
            for count7 in range(0,anzahl):
                if personen[count7].dead==1 or personen[count7].dead==2:
                    tot=tot+1
            return tot
        
        #genesene zählt die Anzahl genesene und gibt diese zurück.
        def genesene():
            global pgenesen
            pgenesen=0
            for count8 in range(0,anzahl):
                if personen[count8].sane==1:
                    pgenesen=pgenesen+1
            return pgenesen
                
        #Ablauf im draw: Alle personen werden mit move bewegt, dann werden alle personen mit allen bezüglich der position mit erkranken verglichen. Nach einer bestimmten framerate sterben die erkrankten oder genesen.
                        
        global erkrankt, pgenesen, tot 
        
        for count9 in range (0,anzahl):
            move(count9)
        erkranken() 
        genesenundtod()
        krankheitszahl()
        todesfaelle()
        genesene()    
        
        print("krank:")
        print(erkrankt) 
        print("genesen:") 
        print(pgenesen) 
        print("tot:") 
        print(tot)
    
    #Darstellung der Anzahl Personen, welche erkrankt, genesen, tot oder gesund sind sowie die Anzahl Frames
    textSize(30)
    fill(255,0,0)
    text(erkrankt, infosx + 200, infosy + 50)
    fill(0,0,255)
    text(pgenesen, infosx + 200, infosy + 100)
    fill(0,0,0)
    text(tot, infosx + 200, infosy + 150)
    fill(0,255,0)
    text(anzahl - erkrankt - pgenesen - tot, infosx + 450, infosy + 50)
    fill(0,0,0)
    text(zeit, infosx + 450, infosy + 100)
    
#Mausklick auf Buttons    
def mousePressed():
    global status, zmode
    #Stop Button
    if mouseX >= buttonx and mouseX <= buttonx + 150 and mouseY >= buttony and mouseY <= buttony + 50 and mousePressed == True:
        status = "stopped"
        
    #Start Button
    if mouseX >= buttonx + 170 and mouseX <= buttonx + 320 and mouseY >= buttony and mouseY <= buttony + 50 and mousePressed == True:
        status = "running"
        
    #Save Button        
    if mouseX >= buttonx + 510 and mouseX <= buttonx + 660 and mouseY >= buttony and mouseY <= buttony +50 and mousePressed == True:
        save("epidemie_simulation.png")
        
    #Reset Button
    if mouseX >= buttonx + 340 and mouseX <= buttonx + 490 and mouseY >= buttony and mouseY <= buttony + 50 and mousePressed == True:
        setup()
    
    #ZombieMode On Button
    if mouseX >= infosx + 240 and mouseX <= infosx + 320 and mouseY >= infosy + 665 and mouseY <= infosy + 715 and mousePressed == True:
        zmode = "on"
        
    #ZombieMode Off Button
    if mouseX >= infosx + 340 and mouseX <= infosx + 420 and mouseY >= infosy + 665 and mouseY <= infosy + 715 and mousePressed == True:
        zmode = "off"
    else:
        pass    
    
"""
Sämtlicher nachfolgende Code stammt von Simon Hefti (Okt. 2020) und beinhaltet die Schiebereglerfunktionen.
Uns ist bewusst, dass es elegantere Lösungen gibt. In Absprache mit Christian Schlegel haben wir aus Zeitgründen und weil wir mehr in die Funktionalität unseres Programmes und nicht den effizientesten Code investieren wollten,
die Schiebereglerfunktion mehrfach kopiert und die Variablen sowie die Berechnung des Wertes entsprechend angepasst.
"""

#Schieberegler Infektionswahrscheinlichkeit      
def draw_ruler(objX, objY, objLength):
    global movingMode
    global pointerPos
    global pointerVal
    
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos == 0:
        pointerPos = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos - pointerRadius and mouseX < pointerPos + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos = objX
            if mouseX > objX:
                pointerPos = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal = int(100 / float(objLength) * (pointerPos - objX))

#Schieberegler Krankheitsdauer         
def draw_ruler2(objX, objY, objLength):
    global movingMode2
    global pointerPos2
    global pointerVal2
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos2 == 0:
        pointerPos2 = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos2 - pointerRadius and mouseX < pointerPos2 + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode2 = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode2 = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode2 == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos2 = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos2 = objX
            if mouseX > objX:
                pointerPos2 = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos2, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal2 = int(100 / float(objLength) * (pointerPos2 - objX) + 1)

#Schieberegler Todesrate       
def draw_ruler3(objX, objY, objLength):
    global movingMode3
    global pointerPos3
    global pointerVal3
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos3 == 0:
        pointerPos3 = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos3 - pointerRadius and mouseX < pointerPos3 + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode3 = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode3 = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode3 == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos3 = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos3 = objX
            if mouseX > objX:
                pointerPos3 = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos3, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal3 = int(100 / float(objLength) * (pointerPos3 - objX))

#Schieberegler Geschwindigkeit       
def draw_ruler4(objX, objY, objLength):
    global movingMode4
    global pointerPos4
    global pointerVal4
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos4 == 0:
        pointerPos4 = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos4 - pointerRadius and mouseX < pointerPos4 + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode4 = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode4 = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode4 == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos4 = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos4 = objX
            if mouseX > objX:
                pointerPos4 = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos4, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal4 = int(100 / float(objLength) * (pointerPos4 - objX) / 10)

#Schieberegler Geschwindigkeit       
def draw_ruler5(objX, objY, objLength):
    global movingMode5
    global pointerPos5
    global pointerVal5
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos5 == 0:
        pointerPos5 = objX
    
    # Linie zeichnen
    fill(85)
    strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos5 - pointerRadius and mouseX < pointerPos5 + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode5 = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode5 = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode5 == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos5 = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos5 = objX
            if mouseX > objX:
                pointerPos5 = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos5, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointerVal5 = int(100 / float(objLength) * (pointerPos5 - objX) * 5)
#Ende des Codes von Simon Hefti


    
        
   
        

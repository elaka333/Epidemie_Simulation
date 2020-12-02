buttonx = 430
buttony = 330
infosx = 430
infosy = 50
movingMode = False
pointerPos = 0
pointerVal = 1.0
status = "stopped"

def setup ():
    size (945, 400)
    background (255,255)
    global position, colour, erkrankt, sick, spread, tletal, tgenesen, pletal, dead, sane, genesen, tot, draw_ruler, status
    
    position = []
    colour = []
    sick=[]
    dead=[]
    sane=[]
    genesen=0
    tot=0
    
    import random
    for p in range (0,199):
        position.insert(p,random.randint(4,396))
    colour.insert(0,1)
    sick.insert(0,1)
    for h in range (1,99):
        colour.insert(h,0)
    for i in range (1,99):
        sick.insert(i,0)
    for j in range (0,99):
        dead.insert(j,0)
    for l in range (0,99):
        sane.insert(j,0)

#Hier die Verbreitungswahrscheinlichkeit, letale Dauer, Genesungszeit und die letalitätsrate eingeben

    tletal=1000
    tgenesen=10000
    pletal=1
    
    frameRate(60)
    noFill()
    strokeWeight(2)
    rect(0, 0, 410, 399)
            
def draw():
    global status
    #Anstelle des gesamten Backgrounds soll nur die rechte Seite aktualisiert werden
    fill(255,255)
    rect(410, 0, 533, 399)
    # draw_ruler-Funktion von Simon Hefti, Okt. 2020
    draw_ruler(infosx + 5, infosy + 240, 400)
    text(str(pointerVal) + "%", infosx + 430, infosy + 253)
    spread=pointerVal
    
    #Anzeigen des Titels sowie der Buttons
    textSize(50)
    fill(0,0,0)
    text("Epidemie Simulation", infosx, infosy)
    noFill()
    rect(buttonx, buttony, 150, 50, 10)
    textSize(50)
    if status == "running":
        fill(255,0,0)
        text("Stop", buttonx + 10, buttony + 40)
    else:
        fill(189,189,189)
        text("Stop", buttonx + 10, buttony + 40)
    noFill()
    rect(buttonx + 170, buttony, 150, 50, 10)
    if status == "running":
        textSize(50)
        fill(189,189,189)
        text("Start", buttonx + 180, buttony + 40)
    else:
        textSize(50)
        fill(0,255,0)
        text("Start", buttonx + 180, buttony + 40)
    noFill()
    rect(buttonx + 340, buttony, 150, 50, 10)
    textSize(50)
    fill(0,0,0)
    text("Reset", buttonx + 350, buttony + 40)
    
    if status == "running":
        #Anstelle des gesamten Backgrounds soll nur die linke Seite aktualisiert werden
        fill(255,255)
        rect(0, 0, 410, 399)
        def person (x,y,f):
            global storx
            global story
            f1=0
            f2=0
            f3=0
            f4=0
            import random
        #Farbcodes:  gesund 60,252,18,255 krank 242,0,0,255 genesen 30,2,240,255 tot 0,0,0,255
            if f==0:
                f1=60
                f2=252
                f3=18
                f4=255
            if f==1:
                f1=242
                f2=0
                f3=0
                f4=255
            if f==2:
                f1=30
                f2=2
                f3=240
                f4=255
            if f==3:
                f1=0
                f2=0
                f3=0
                f4=255
            move=random.randint(1,8)
            if move ==1 and x>0:
                ellipse(x-1,y,6,6)
                fill(f1,f2,f3,f4)
                storx=x-1
                story=y
                return storx, story
            else: redraw()
            if move ==2 and y<400:
                ellipse(x,y+1,6,6)
                fill(f1,f2,f3,f4)
                story=y+1
                storx=x
                return storx, story
            else: redraw()
            if move ==3 and x<400:
                ellipse(x+1,y,6,6)
                fill(f1,f2,f3,f4)
                storx=x+1
                story=y
                return storx, story
            else: redraw()
            if move ==4 and y>0:
                ellipse(x,y-1,6,6)
                fill(f1,f2,f3,f4)
                story=y-1
                storx=x
                return storx, story
            else: redraw()
            if move ==5 and x>0 and y>0:
                ellipse(x-1,y-1,6,6)
                fill(f1,f2,f3,f4)
                story=y-1
                storx=x-1
                return storx, story
            else: redraw()
            if move ==6 and x<400 and y>0:
                ellipse(x+1,y-1,6,6)
                fill(f1,f2,f3,f4)
                story=y-1
                storx=x+1
                return storx, story
            else: redraw()
            if move ==7 and x<400 and y<400:
                ellipse(x+1,y+1,6,6)
                fill(f1,f2,f3,f4)
                story=y+1
                storx=x+1
                return storx, story
            else: redraw()
            if move ==8 and x>0 and y<400:
                ellipse(x-1,y+1,6,6)
                fill(f1,f2,f3,f4)
                story=y+1
                storx=x-1
                return storx, story
            else: redraw()
        
        def erkranken():
            global erkrankt
            for d in range (0,99):
                contx=d*2
                conty=d+1
                for b in position:
                    if position[contx]==position[contx+2]:
                        if position[conty]==position[conty+2]:
                            if dead[d]!=1 and sane!=1:
                                import random
                                dec=random.randint(1,100)
                                if dec<=spread:
                                    colour[d]=1
                                    sick[d]=1
                                    ellipse(position[contx],position[conty],10,10)
                                    fill(242,0,0,255)
        
    
        def krankheitszahl():
            global erkrankt
            erkrankt=1
            for p in range(0,99):
                if sick[p]==1:
                    erkrankt=erkrankt+1
            return erkrankt
        
    
        def tod():
            global colour,sick,dead
            import random
            for k in range(0,99):
                if sick[k]==1 and sane[k]!=0:
                    dec2=random.randint(1,100)
                    if dec2<=pletal:
                        colour[k]=3
                        sick[k]=0
                        dead[k]=1
                
            
        def genesen():
            global colour,sick,dead
            import random
            for u in range(0,99):
                if sick[u]==1:
                    dec3=random.randint(1,100)
                    if dec3<=tgenesen:
                        colour[u]=2
                        sick[u]=0
                        sane[u]=1
    
        def todesfaelle():
            global tot
            tot=0
            for t in range (0,99):
                if dead[t]==1:
                    tot=tot+1
            return tot
        
        def genesene():
            global genesen
            genesen=0
            for s in range (0,99):
                if sane[s]==1:
                    genesen=genesen+1
            return genesen
                
        global position 
        global erkrankt   
        for n in range (0,98):
            if dead[n]!=1:    
                person(position[n], position[n+1],colour[n])
                position[n]=storx
                position[n+1]=story
            else:
                person(1000,1000,0)
        erkranken()
    
    
        if frameCount // tletal:
            tod()
        if frameCount// tgenesen:
            genesen()
            
        krankheitszahl()
        todesfaelle()
        genesene()
        print("krank:")
        print(erkrankt) 
        print("genesen:") 
        print(genesen) 
        print("tot:") 
        print(tot)
        textSize(30)
        fill(255,0,0)
        text(erkrankt, infosx + 200, infosy + 50)
        fill(0,0,255)
        text(erkrankt, infosx + 200, infosy + 100)
        fill(0,0,0)
        text(tot, infosx + 200, infosy + 150)
    #Anzeige der Informationen
    fill(0,0,0)
    textSize(30)
    text("krank:", infosx, infosy + 50)
    fill(0,0,0)
    text("genesen:", infosx, infosy + 100)
    fill(0,0,0)
    text("gestorben:", infosx, infosy + 150)
    text("Infektionswahrscheinlichkeit:", infosx, infosy + 200)
    
    
#Code von Simon Hefti, Okt. 2020           
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
#Ende des Codes von Simon Hefti
        
#Mausklick auf Buttons    
def mousePressed():
    global status
    if mouseX >= buttonx and mouseX <= buttonx + 150 and mouseY >= buttony and mouseY <= buttony + 50 and mousePressed == True:
        status = "stopped"
    if mouseX >= buttonx + 170 and mouseX <= buttonx + 320 and mouseY >= buttony and mouseY <= buttony + 50 and mousePressed == True:
        status = "running"
    if mouseX >= buttonx + 340 and mouseX <= buttonx + 490 and mouseY >= buttony and mouseY <= buttony + 50 and mousePressed == True:
        setup()
        #Sämtliche Variabeln müssen ebenfalls zurückgesetzt werden!!!
    else:
        pass

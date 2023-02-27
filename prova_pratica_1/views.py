from django.shortcuts import render



def view_a(request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={
      'materie':materie
    }
    return render (request,'materie.html',context)
    
def view_b(request):    
    voti = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    context={
      'materie':materie
    }
    return render (request,'materie.html',context)


'''
students={'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]
           }   

def VotiStudente(request):
    context={
           {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}   
    }
    return render (request,context)

def media(request):
    context={
        dati=students['Giuseppe Gullo']
        print(dati)
        media=0

        for dato in dati:
            media+=dato[1]
        media=media/len(dati)
        print("media="+str(media1))
        
        dati=students['Antonio Barbera']
        print(dati)
        media=0

        for dato in dati:
            media+=dato[1]
        media=media/len(dati)
        print("media="+str(media2))

        dati=students['Nicola Spina']
        print(dati)
        media=0

        for dato in dati:
            media+=dato[1]
        media=media/len(dati)
        print("media="+str(media3))


     
    }
    return render (request,media1,media2,media3,context)
    '''
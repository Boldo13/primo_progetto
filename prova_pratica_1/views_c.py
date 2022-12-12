from django.shortcuts import render

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
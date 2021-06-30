def  importeTotalCarro(request):
    valor=0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            valor=valor+(float(value["precio"]))
    return {"importeTotalCarro":valor}

def productosTotalesCarro(request):
    total=0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total=total+(value["cantidad"])
    return {"productosTotalesCarro":total}
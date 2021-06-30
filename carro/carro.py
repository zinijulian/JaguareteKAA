class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        #else:
        self.carro=carro
    
    def agregarProducto(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            self.sumarProducto(producto)
        self.guardarCarro()

    def guardarCarro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    def eliminarProducto(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardarCarro()

    def restarProducto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id): 
                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])-producto.precio
                    if value["cantidad"]<1:
                        self.eliminarProducto(producto)
                    break
        self.guardarCarro()

    def sumarProducto(self, producto):
        for key, value in self.carro.items():
                if key==str(producto.id): 
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardarCarro()

    def limpiarCarro(self):
        carro=self.session["carro"]={}
        self.session.modified=True
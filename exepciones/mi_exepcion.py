#creando mi propia exepcion personalizada
class MiExepcion(Exception):
    def __init__(self,err):
        print(f"impresionante, cometiste el siguiente error:  {err}")
        

#manejandola
try:
    raise MiExepcion("jajajajajaja, persona poco culta")
except:
    print("Como vas a cometer ese error?")
 
#Lazando mi propia exepcion    
raise MiExepcion("jajajajajaja, persona poco culta")

class MIExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante,cometiste el siguiente error: {err}")
        
try:
    raise MIExcepcion("jajajajajaj,persona poco culta")
except:
    print("como vas a cometer ese error")
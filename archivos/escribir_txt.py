with open('archivos\\texto_de_pipe.txt','w',encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo 
    # archivo.write("jajajaja te la recontra teclee")
    
    #agregando 2 lineas con writelines
    archivo.writelines([" - hola maestro como andas\n", " - misericordia\n"])
    
    #agregando otras dos lineas
    archivo.writelines([" - no se porque dijiste eso\n"," - yo tampoco"])
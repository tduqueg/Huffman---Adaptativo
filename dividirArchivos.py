import pathlib


class dividirArchivos():
    
    def dividirArchivo():
        path_base = "./README.md"

        archivo_Original = open(path_base)


        CHUNK_SIZE = 10024

        archivo_Original = archivo_Original.read(CHUNK_SIZE)

        file_number = 0

        try:
            with open(path_base) as f:
                chunk = archivo_Original
                while chunk:
                    with open('./archivos/texto_parte_' + str(file_number) + '.txt', "x") as chunk_file:
                        chunk_file.write(chunk)
                    file_number += 1
                    chunk = f.read(CHUNK_SIZE)
        except FileExistsError:
            file_number += 1
    
    dividirArchivo()
    archivo_duplicado = pathlib.Path('./archivos/texto_parte_0.txt')
    pathlib.Path.unlink(archivo_duplicado)

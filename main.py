from src.pdf_reader.service.ReaderService import ReaderService
import os
from dotenv import load_dotenv
from src.nlp.service.InferenceService import InferenceService

if __name__ == '__main__':
    # Definimos un nombre para nuestra clase de lectura
    reader = ReaderService
    # Definimos el nombre del archivo pdf en la carpeta resources
    archivo = "src/pdf_reader/resources/ATanembaumSOModernos.pdf"
    # Llamamos a la función que nos dice el número de páginas del pdf
    # print(reader.pageN(archivo))
    # Llamamos a la función que nos dice la metadata de páginas del pdf
    # print(reader.meta(archivo))
    # Llamamos a la función que extrae la informacion del pdf a txt
    # reader.pdf2txt(archivo)
    # Llamamos a la función que imprime la informacion de 1 pagina del pdf
    # print(reader.pdf2txt1page(archivo,5))
    # Cargamos la informacion de nuestro token de openAI
    # load_dotenv("secrets/.env")
    # Imprimimos la API_KEY
    # print(os.getenv('OPENAI_API_KEY'))
    # Imprimimos el resultado de nuestro prompt
    # print(InferenceService().invokeResume(reader.pdf2txt1page(archivo,50)))
    # prompt = input()
    # print(InferenceService().invokeCustom(prompt, reader.pdf2txt1page(archivo,50)))
    # print(reader.pdf2str(archivo))
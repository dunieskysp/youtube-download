from pytube import YouTube
import os
from funciones import output_format as of


def formatos(video_instance, formato):
    if formato != "audio":
        return video_instance.streams.filter(file_extension=formato).order_by('resolution').desc()
    else:
        return video_instance.streams.filter(only_audio=True)


def datos_resolucion(lista_formato):
    resultado = []
    for formato in lista_formato:
        resolucion = str(formato).split(" ")
        resolucion = tuple(dato.split('"')[1].split('"')[
                           0] for dato in resolucion if "itag=" in dato or "res=" in dato or "progressive=" in dato)
        resultado.append(resolucion)
    return resultado


def datos_audio(lista_formato):
    resultado = []
    for formato in lista_formato:
        resolucion = str(formato).split(" ")
        resolucion = tuple(dato.split('"')[1].split('"')[
                           0] for dato in resolucion if "itag=" in dato or "mime_type=" in dato or "abr=" in dato)
        resultado.append(resolucion)
    return resultado


def verificar_formato(video_instance, formato):
    if formato == "mp4" or formato == "mkv" or formato == "webm" or formato == "audio":
        if len(formatos(video_instance, formato)) == 0:
            print(
                f'\nEl video no está disponible en el formato "{formato.upper()}", intente otro.')
            return False
        return formato
    else:
        print(f"{of.error(formato, 'btn')} {of.error('no es un formato válido')}")
        return False


def verificar_video_id(lista_disponibles, video_id):
    for valor in lista_disponibles:
        if video_id in valor:
            return video_id

    print(f"{video_id} no es un ID válido, escoja uno de la lista anterior")
    return False


def descargar_video(video, video_id, directorio, video_instance):
    try:
        video.get_by_itag(video_id).download()
    except:
        print(f'No se pudo descargar el video "{video_instance.title}"')
    else:
        print(
            f'Se descargó correctamente el video "{video_instance.title}" en "{directorio}"')


# url_video = "https://www.youtube.com/watch?v=-OJSZLHTk-8"
url_video = input("Ingrese la URL del video a descargar: ")
video_instance = YouTube(url_video)

formato_descargar = False
while not formato_descargar:
    print(f"\nFormatos admitidos: {of.info('MP4, MKV, WEBM y Audio')}")
    formato_descargar = input(
        "Ingrese el formato en el que desea descargar el video: ")
    formato_descargar = verificar_formato(
        video_instance, formato_descargar.lower())


formatos = formatos(video_instance, formato_descargar)

if formato_descargar != "audio":
    # print(datos_resolucion(formatos))
    print(f'\nDescargas disponibles para el formato "{formato_descargar}"')
    print(" ID | Resol | Progresivo")
    for resolucion in datos_resolucion(formatos):
        if len(resolucion[0]) == 3:
            print(f"{resolucion[0]} | {resolucion[1]} | {resolucion[2]}")
        else:
            print(f"{resolucion[0]}  | {resolucion[1]} | {resolucion[2]}")
else:
    # print(formatos)
    print(f'\nDescargas disponibles en formato de Audio')
    print(" ID | Tipo | Bitrate")
    for audio in datos_audio(formatos):
        # print(audio)
        tipo = audio[1].split("/")[1]
        if len(audio[0]) == 3:
            print(f"{audio[0]} | {tipo} | {audio[2]}")
        else:
            print(f"{audio[0]}  | {tipo} | {audio[2]}")

video_id = False
while not video_id:
    video_id = input("\nIngrese el ID del formato que desea Descargar: ")
    video_id = verificar_video_id(datos_audio(formatos), video_id)

path = os.getcwd()
print(
    f'\nVa a comenzar la decarga del video: "{video_instance.title}" en formato "{formato_descargar}"')
descargar_video(formatos, video_id, path, video_instance)

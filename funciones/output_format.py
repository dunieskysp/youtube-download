# Diccionario con todos los estilos que se le van a aplicar al Texto de Salida
all_styles = {
    # Formato
    'reset': '\033[0m',
    'bold': '\033[01m',
    'disabled': '\033[02m',
    'italic': '\033[03m',
    'underline': '\033[04m',
    'blink': '\033[05m',
    'blink2': '\033[06m',
    'reverse': '\033[07m',
    'invisible': '\033[08m',
    'strike_through': '\033[09m',
    # Color del Texto
    'fg_black': '\033[30m',
    'fg_red': '\033[31m',
    'fg_green': '\033[32m',
    'fg_yellow': '\033[33m',
    'fg_blue': '\033[34m',
    'fg_magenta': '\033[35m',
    'fg_cyan': '\033[36m',
    'fg_white': '\033[37m',
    'fg_black2': '\033[90m',
    'fg_red2': '\033[91m',
    'fg_green2': '\033[92m',
    'fg_yellow2': '\033[93m',
    'fg_blue2': '\033[94m',
    'fg_magenta2': '\033[95m',
    'fg_cyan2': '\033[96m',
    'fg_white2': '\033[97m',
    # Color del Fondo
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
    'bg_black2': '\033[100m',
    'bg_red2': '\033[101m',
    'bg_green2': '\033[102m',
    'bg_yellow2': '\033[103m',
    'bg_blue2': '\033[104m',
    'bg_magenta2': '\033[105m',
    'bg_cyan2': '\033[106m',
    'bg_white2': '\033[107m',
}


# Función que devuelve el Estilo del Texto
def text_styles(text, **styles):
    texto_estilos = ''
    for style in styles:
        try:
            texto_estilos += all_styles[style]
        except KeyError:
            raise KeyError('def TEXT_STYLES: El parametro "{style}" no existe')

    texto_estilos += text
    return f'{all_styles["reset"]}{texto_estilos}{all_styles["reset"]}'


# Función para imprimir un Error ***********************************************************************
def error(text, tipo=""):
    if tipo == "fig":
        return text_styles('\u2718 ' + text, bold=True, fg_red=True)
    elif tipo == "btn":
        return text_styles(text, bold=True, fg_white2=True, bg_red=True)
    elif tipo == "btn_fig":
        return text_styles(' \u2718 ' + text + ' ', bold=True, fg_white2=True, bg_red=True)

    return text_styles(text, bold=True, fg_red=True)


# Función para imprimir una Advertencia *****************************************************************
def warning(text, tipo=""):
    if tipo == "fig":
        return text_styles('\u26A0 ' + text, bold=True, fg_yellow=True)
    elif tipo == "btn":
        return text_styles(text, bold=True, fg_white2=True, bg_yellow=True)
    elif tipo == "btn_fig":
        return text_styles(' \u26A0 ' + text + ' ', bold=True, fg_white2=True, bg_yellow=True)

    return text_styles(text, bold=True, fg_yellow=True)


# Funciones para imprimir que todo salió bien *************************************************************
def succes(text, tipo=""):
    if tipo == "fig":
        return text_styles('\u2714 ' + text, bold=True, fg_green=True)
    elif tipo == "btn":
        return text_styles(text, bold=True, fg_white2=True, bg_green=True)
    elif tipo == "btn_fig":
        return text_styles(' \u2714 ' + text + ' ', bold=True, fg_white2=True, bg_green=True)

    return text_styles(text, bold=True, fg_green=True)


# Funciones para imprimir Información ************************************************************************
def info(text, tipo=""):
    if tipo == "fig":
        return text_styles('\u24D8 ' + text, bold=True, fg_blue=True)
    elif tipo == "btn":
        return text_styles(text, bold=True, fg_white2=True, bg_blue=True)
    elif tipo == "btn_fig":
        return text_styles(' \u24D8 ' + text + ' ', bold=True, fg_white2=True, bg_blue=True)

    return text_styles(text, bold=True, fg_blue=True)


# Funciones para Texto en Negrita
def bold(text):
    return text_styles(text, bold=True)


# print(error("Error!"), error("Error!", "fig"),
#       error("Error!", "btn"), error("Error!", "btn_fig"))

# print(warning("Alerta!"), warning("Alerta!", "fig"),
#       warning("Alerta!", "btn"), warning("Alerta!", "btn_fig"))

# print(succes("Listo!"), succes("Listo!", "fig"),
#       succes("Listo!", "btn"), succes("Listo!", "btn_fig"))

# print(info("Info!"), info("Info!", "fig"),
#       info("Info!", "btn"), info("Info!", "btn_fig"))

# print(bold("Negrita"))

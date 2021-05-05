

def hacerloTodoOtraVez(SioNo):
    """aca me fijo si el usuario quiere usar otra vez el programa, osea tiene otro examen que corregir"""
    if SioNo == "si":
        ejerciciosTotales = int(input("en este examen cuantos ejercicios hay en total: "))
        porcentajeAprobado = int(input("y en este examen cual es el porcentaje de aprobado: "))
        return calcularPorcentaje(ejerciciosTotales, porcentajeAprobado)
    else:
        return

def aprobacion(porcentajeAprobado, porcentajeExamen):

    if porcentajeExamen > porcentajeAprobado:
        return print(f"aprobo con un {porcentajeExamen}%")
        respuesta = bool(input("es necesario hacer otro examen?"))
        hacerloTodoOtraVez(respuesta)
    elif porcentajeExamen == porcentajeAprobado:
        return print("aprobo con la nota minima")
        respuesta = bool(input("es necesario hacer otro examen?"))
        hacerloTodoOtraVez(respuesta)
    else:
        return print(f"el alumno no ha aprobado la materia, se ha sacado un {porcentajeExamen}%")
        respuesta = bool(input("es necesario hacer otro examen?"))
        hacerloTodoOtraVez(respuesta)
        """ aca le pregunto si la personita quiere seguir corrigiendo evaluaciones """
def calcularPorcentaje(ejerciciosTotales, porcentajeAprobado):
    ejercicionBien = int(input("cuantos ejercicios hizo bien: "))
    """ aca me fijo que los ejercicios que hizo bien sean positivos, ademas de contar el porcentaje"""
    if ejercicionBien >= 0:
        # profe porfa no me desapruebes :(
        porcentajeExamen = (100/ejerciciosTotales) * ejercicionBien
        aprobacion(porcentajeAprobado, porcentajeExamen)
    else:
        return print(("los ejercicios bien hechos tienen que ser positivos"))
if 0 == 0:
    porcentajeaprobado = float(input("en este examen cual es el porcentaje de aprobado: "))
    if porcentajeaprobado <= 100:
        ejerciciostotales = int(input("y en este examen cuantos ejercicios hay en total: "))
        if ejerciciostotales > 0:
            calcularPorcentaje(ejerciciostotales, porcentajeaprobado)
        else:
            print("tiene que haber un numero positivo de ejercicios en el examen")
    else:
        print("el porcentaje de aprobacion tiene que ser menor o igual que 100")


def combinaciones(cadena):
    if len(cadena) == 0:
        return ['']
    primer_digito = cadena[0]
    resto_de_cadena = cadena[1:]
    combinaciones_previas = combinaciones(resto_de_cadena)
    nuevas_combinaciones = []
    for combinacion in combinaciones_previas:
        nuevas_combinaciones.append(primer_digito + combinacion)
        if combinacion != '':
            nuevas_combinaciones.append(primer_digito + ' ' + combinacion)
    return nuevas_combinaciones

print(combinaciones('1234'))
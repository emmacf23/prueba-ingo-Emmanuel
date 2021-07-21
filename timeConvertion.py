hours = {"01":"la una","02":"las dos","03":"las tres","04":"las cuatro","05":"las cinco",
        "06":"las seis","07":"las siete","08":"las ocho","09":"las nueve","10":"las diez",
         "11":"las once","12":"las doce"}

tens = { "10": "y diez","1":"y dieci","20":"y veinte","2": "y veinti",
        "3": "y treinta", "4": "y cuarenta","5": "y cincuenta","0":""}

exceptions = {"00":"en punto","11": "y once","12":"y doce","13":"y trece","14":"y catorce",
        "15":"y cuarto","30": "y media","12:00pm": "Es medio día", "12:00am": "Es media noche"}

units = {"1": "uno", "2": "dos", "3": "tres", "4": "cuatro","5": "cinco",
        "6": "seis","7": "siete", "8":"ocho","9":"nueve"}


"""
Entrada: time: Recibe un string con una hora en formato hh:mm am/pm
Salida: Retorna un string con la solución o un mensaje de error
Descripción: Valida la entrada del usuario e inicia el proceso de conversión
"""
def dateToString(time):
    answer = {'text': "",'error':False}
    if(validateTime(time)):
        if(time in exceptions.keys()):
            answer['text']= exceptions[time]            
        else:
            answer['text']=getHour(createTimeDict(time))
        return answer
    else:
        answer['error']=True
        answer['text']="Ocurrio un error.Digite los datos correctamente"
        return answer
        

"""
Entrada: time: Recibe un string con una hora en formato hh:mm am/pm
Salida: Retorna un diccionario con las llaves de las horas, minutos y momento del tiempo
Descripción: Convierte el string en  un diccionario para así facilitar su acceso
"""
def createTimeDict(time):
    return {"hour":time[0]+ time[1],"minutes":time[3]+ time[4],"moment":time[5] + time[6]}


"""
Entrada: time: Recibe un string con una hora en formato hh:mm am/pm
Salida: Retorna un booleano. True en caso de que el texto ingresado sea valido y False en caso contrario.
Descripción: Se encarga de validar si el string ingresado cumple el formato en la hora,minutos y el am/pm
"""
def validateTime(time):
    time = list(time)
    if(len(time) == 7):
        hour = time[0]+ time[1]
        minutes = time[3]+ time[4]
        moment= time[5] + time[6]
        return validateHour(hour) and validateMinutes(minutes) and time[2]==":" and validateMoment(moment)
    return False

"""
Entrada: hour: Recibe un string con una hora en formato hh
Salida: Retorna un booleano. True en caso de que el texto ingresado sea valido y False en caso contrario.
Descripción: Se encarga de validar si el string ingresado es numerico y esta entre 1 y 12
"""
def validateHour(hour):
    if(hour.isnumeric()):
        hour = int(hour)
        return hour > 0 and hour < 13
    return False

"""
Entrada: minutes: Recibe un string con los minutos en formato mm
Salida: Retorna un booleano. True en caso de que el texto ingresado sea valido y False en caso contrario.
Descripción: Se encarga de validar si el string ingresado es numerico y esta entre 0 y 59
"""
def validateMinutes(minutes):
    if(minutes.isnumeric()):
        minutes = int(minutes)
        return minutes > -1 and minutes < 60
    return False

"""
Entrada: moment: Recibe un string con el momento en formato am/pm
Salida: Retorna un booleano. True en caso de que el texto ingresado sea valido y False en caso contrario.
Descripción: "Valida que el momento sea am/pm"
"""
def validateMoment(moment):
    moment.lower()
    return moment == "am" or moment == "pm"
    

"""
Entrada: time: Recibe un string con una hora en formato hh:mm am/pm
Salida: Retorna la hora ya redactada.
Descripción: "Busca en el diccionario el match de la hora y prosigue solicitando los minutos"
"""
def getHour(time):
    response = ''
    hour = time["hour"]
    if(hour in hours.keys()):
        response = 'Son ' + hours[hour] + " "
    return getMinutes(time,response)


"""
Entrada: time: Recibe un string con una hora en formato hh:mm am/pm y la redaccion hasta ahora realizada por las horas
Salida: Retorna los minutos ya redactada.
Descripción: "Busca en el diccionario el match de los minutos y prosigue solicitando el segundo digito de los minutos o el momento del día"
"""
def getMinutes(time,response):
    minutes = time["minutes"]
    if(minutes in exceptions.keys()):  #Valida si esta en el diccionario de excepciones
        response = response + exceptions[minutes]
    elif(minutes in tens.keys()): # Valida si los minutos completos están en el diccionario de minutos
        response = response + tens[minutes]
        #return getUnits(time,response)
    elif(minutes[0] in tens.keys()): #Valida si el primer digito de los minutos esta en el diccionario de los minutos
        response = response + tens[minutes[0]]
        return getUnits(time,response)

    return getMoment(time,response)

"""
Entrada: time: Recibe un string con una hora en formato hh:mm am/pm y la redaccion hasta ahora realizada por los minutos
Salida: Retorna el segundo digito de los minutos ya redactados.
Descripción: "Busca en el diccionario el match del segundo digito de los minutos y prosigue solicitando el momento del día"
"""
def getUnits(time,response):
    minutes =time["minutes"]
    unit = minutes[1]
    if(unit != "0"): # Si la unidad es 0 proceder a el momento. Ejemplo "10" unidad="0"
        if(minutes[0] == "1" or minutes[0] == "2"): # En el caso de que sean estos casos no se debe de separar por una y
            response = response + units[unit]
        else:
            response = response +" y "+units[unit]
    return getMoment(time,response)
        

"""
Entrada: time: Recibe un string con una hora en formato hh:mm am/pm y la redaccion hasta ahora realizada por los minutos
Salida: Retorna el  momento del dia ya redactados.
Descripción: "Verifica si el momento es la mañana, la tarde o la noche"
"""
def getMoment(time,response):
    hour = int(time["hour"])
    moment = time["moment"]
    if(moment == "am"):
        response = response + " de la mañana."
    elif(moment == "pm"):
        if(hour < 6 or hour == 12):
            response = response + " de la tarde."
        else:
            response = response + " de la noche."
    return response

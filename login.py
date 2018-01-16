import easygui as eg
import probaMySQL as pm

def runLogin():
    # ventana de login
    campos = ['Nombre', 'Password']
    salida = eg.multpasswordbox(msg='Bienvenido al CatalagoOA', title='Login'
                                , fields=campos)
    print salida[0]

    # busco en la base de datos
    query = 'select nombre,institucion from usuario where nombre ="' + salida[0] + '" and clave="' + salida[1] + '"'
    resultado = pm.run_query(query)

    try:
        if resultado[0][0] == 'Admin':
            eg.msgbox(msg='Bienvenido Administrador', title='Conectado'
                      , ok_button='continuar')
        else:
            eg.msgbox(msg='Bienvenido Usuario', title='Conectado'
                      , ok_button='continuar')

        return True
    except:
        opcion = ''
        opcion = eg.ccbox(msg='Usuario o contrasena incorrecta', title='Fallo')
        print opcion
        if opcion == True:
            runLogin()
        else:
            return False

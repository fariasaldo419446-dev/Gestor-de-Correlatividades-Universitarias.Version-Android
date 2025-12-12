from kivy.storage.jsonstore import JsonStore
from constantes import ESTADO_FILE
from modelos import Estado


def obtener_todas_materias_carrera(datos, universidad, facultad, carrera):
    materias_oblig = datos[universidad][facultad][carrera]['obligatorias']
    materias_elec = datos[universidad][facultad][carrera]['electivas']
    return materias_oblig + materias_elec


def actualizar_disponibilidad(materias):
    cod_a_materia = {m.codigo: m for m in materias}

    for m in materias:
        if not m.correlativas_regular and not m.correlativas_aprobadas:
            m.disponible = True
        else:
            aprobadas_ok = all(
                c in cod_a_materia and cod_a_materia[c].estado == Estado.APROBADA for c in m.correlativas_aprobadas)
            regular_ok = all(
                c in cod_a_materia and cod_a_materia[c].estado in [Estado.REGULAR, Estado.APROBADA] for c in m.correlativas_regular)
            m.disponible = aprobadas_ok and regular_ok

        if hasattr(m, 'btn') and m.btn:
            m.btn.disabled = not m.disponible
            m.btn.background_color = Estado.colores[m.estado]


def guardar_estados(datos):
    data = {}
    for universidad, facultades in datos.items():
        data_uni = {}
        for facultad, carreras in facultades.items():
            data_facu = {}
            for carrera, tipos in carreras.items():
                data_carrera = {}
                for tipo in tipos:
                    materias = tipos[tipo]
                    for m in materias:
                        data_carrera[str(m.codigo)] = m.estado
                data_facu[carrera] = data_carrera
            data_uni[facultad] = data_facu
        data[universidad] = data_uni

    store = JsonStore(ESTADO_FILE)
    store.put('estados', data=data)


def cargar_estados(datos):
    store = JsonStore(ESTADO_FILE)
    if store.exists('estados'):
        data = store.get('estados')['data']
        for universidad, facultades in datos.items():
            if universidad in data:
                data_uni = data[universidad]
                for facultad, carreras in facultades.items():
                    if facultad in data_uni:
                        data_facu = data_uni[facultad]
                        for carrera, tipos in carreras.items():
                            if carrera in data_facu:
                                estados_carrera = data_facu[carrera]
                                for tipo, materias in tipos.items():
                                    for m in materias:
                                        if str(m.codigo) in estados_carrera:
                                            m.estado = estados_carrera[str(m.codigo)]

class Estado:
    NO_CURSADA = "No cursada"
    REGULAR = "Regular"
    CURSANDO = "Cursando"
    APROBADA = "Aprobada"

    colores = {
        NO_CURSADA: (0.85, 0.85, 0.85, 1),
        REGULAR: (1, 0.85, 0.4, 1),
        CURSANDO: (0.53, 0.81, 0.97, 1),
        APROBADA: (0.64, 0.78, 0.64, 1),
    }


class Materia:
    def __init__(self, codigo, nombre, nivel, corr_reg=None, corr_apr=None):
        self.codigo = codigo
        self.nombre = nombre
        self.nivel = nivel
        self.correlativas_regular = corr_reg or []
        self.correlativas_aprobadas = corr_apr or []
        self.estado = Estado.NO_CURSADA
        self.disponible = False
        self.btn = None

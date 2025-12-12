from modelos import Materia

def crear_materias_sistemas():
    return [
        Materia(1, "Análisis Matemático 1", 1),
        Materia(2, "Álgebra y Geometría Analítica", 1),
        Materia(3, "Física 1", 1),
        Materia(4, "Inglés 1", 1),
        Materia(5, "Lógica y Estructuras Discretas", 1),
        Materia(6, "Algoritmos y Estructuras de Datos", 1),
        Materia(7, "Arquitectura de Computadoras", 1),
        Materia(8, "Sistemas y Procesos de Negocio", 1),
        Materia(11, "Ingeniería y Sociedad", 1),
        Materia(9, "Análisis Matemático 2", 2, [1, 2]),
        Materia(10, "Física 2", 2, [1, 3]),
        Materia(12, "Inglés 2", 2, [4]),
        Materia(13, "Sintaxis y Semántica de los Lenguajes", 2, [5, 6]),
        Materia(14, "Paradigmas de Programación", 2, [5, 6]),
        Materia(15, "Sistemas Operativos", 2, [7]),
        Materia(16, "Análisis de Sistemas de Información", 2, [6, 8]),
        Materia(17, "Probabilidad y Estadísticas", 2, [1, 2]),
        Materia(18, "Economía", 3, [], [1, 2]),
        Materia(19, "Bases de Datos", 3, [13, 16], [5, 6]),
        Materia(20, "Desarrollo de Software", 3, [14, 16], [5, 6]),
        Materia(21, "Comunicación de Datos", 3, [], [3, 7]),
        Materia(22, "Análisis Numérico", 3, [9], [1, 2]),
        Materia(23, "Diseño de Sistemas de Información", 3, [14, 16], [4, 6, 8]),
        Materia(99, "Seminario Integrador (Analista)", 3, [16], [6, 8, 13, 14]),
        Materia(24, "Legislación", 4, [11]),
        Materia(25, "Ingeniería y Calidad de Software", 4, [19, 20, 23], [13, 14]),
        Materia(26, "Redes de Datos", 4, [15, 21]),
        Materia(27, "Investigación Operativa", 4, [17, 22]),
        Materia(28, "Simulación", 4, [17], [9]),
        Materia(29, "Tecnologías para la Automatización", 4, [10, 22], [9]),
        Materia(30, "Administración de Sistemas de Información", 4, [18, 23], [16]),
        Materia(31, "Inteligencia Artificial", 5, [28], [17, 22]),
        Materia(32, "Ciencia de Datos", 5, [28], [17, 19]),
        Materia(33, "Sistemas de Gestión", 5, [18, 27], [23]),
        Materia(34, "Gestión Gerencial", 5, [24, 30], [18]),
        Materia(35, "Seguridad en los Sistemas de Información", 5, [26, 30], [20, 21]),
        Materia(36, "Proyecto Final", 5, [25, 26, 30], [12, 20, 23]),
    ]

def crear_materias_electivas_sistemas():
    return [
        Materia(202, "Backend de Aplicaciones", 3, [14, 13], [6]),
        Materia(203, "Green Software", 4, [20, 19], [13, 14]),
        Materia(204, "Gestión Industrial de la Producción", 4, [19], [8, 16]),
        Materia(205, "Gestión de la Mejora de los Procesos", 4, [19], [8, 16]),
        Materia(206, "Desarrollo y Operaciones DevOps", 4, [19, 20], [14, 13]),
        Materia(207, "Desarrollo de Aplicaciones con Objetos", 4, [13], [6]),
        Materia(208, "Comunicación Multimedial en el Desarrollo de Sistemas", 4, [19], [8, 16]),
        Materia(209, "Arquitectura de Software", 4, [19, 20], [14, 13]),
        Materia(210, "Desarrollo de Tecnologías Blockchain", 5, [26, 19], [20, 14]),
        Materia(211, "Creatividad e Innovación en Ingeniería", 5, [30], [20]),
        Materia(212, "Auditoría de SI/TI", 5, [30], [20]),
        Materia(213, "Gerenciamiento Estratégico", 5, [30], [20]),
        Materia(214, "Consultoría en Negocios Digitales", 5, [30], [20]),
        Materia(215, "Emprendimientos Tecnológicos", 5, [30], [16, 19]),
        Materia(216, "Decisiones en Escenarios Complejos", 5, [27], [19]),
        Materia(217, "Testing de Software", 5, [25], [19, 20]),
        Materia(218, "Seguridad en el Desarrollo de Software", 5, [26, 19], [20, 8]),
        Materia(219, "Integración de Aplicaciones en Entorno Web", 5, [26, 19], [19, 20]),
        Materia(220, "Ingeniería de Software de fuentes abiertas/libres", 5, [20, 19, 26], [13, 14]),
    ]

def crear_materias_psicologia():
    return [Materia(1, "Biología", 1)]

def crear_materias_electivas_psicologia():
    return []

def crear_materias_profesorado_psicologia():
    return [Materia(1, "Biología", 1)]

def crear_materias_electivas_profesorado_psicologia():
    return []

def crear_datos():
    return {
        "UTN": {
            "Facultad Regional Córdoba": {
                "Ingeniería en Sistemas": {
                    "obligatorias": crear_materias_sistemas(),
                    "electivas": crear_materias_electivas_sistemas(),
                },
            },
        },
        "UNC": {
            "Facultad de Psicología": {
                "Licenciatura en Psicologia": {
                    "obligatorias": crear_materias_psicologia(),
                    "electivas": crear_materias_electivas_psicologia(),
                },
                "Profesorado en Psicologia": {
                    "obligatorias": crear_materias_profesorado_psicologia(),
                    "electivas": crear_materias_electivas_profesorado_psicologia(),
                },
            },
        },
    }

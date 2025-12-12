# 🎓 Gestor de Correlatividades Universitarias (Android)

Aplicación móvil desarrollada en Python y Kivy para gestionar el estado de las materias (cursando, regular, aprobada) y visualizar correlatividades en tiempo real.

## Características
* 🚀 **Multi-Universidad:** Soporte inicial para UTN (Sistemas) y UNC (Psicología).
* 🔄 **Control de Correlativas:** Bloquea materias si no tienes las anteriores regularizadas o aprobadas.
* 💾 **Persistencia:** Guarda tu progreso localmente en el dispositivo.
* 📱 **Android:** Compilable a APK usando Buildozer.

## Estructura del Proyecto
* `main.py`: Lógica principal de la interfaz (UI).
* `datos.py`: Carga de planes de estudio y materias.
* `modelos.py`: Definición de clases (Materia, Estado).
* `utils.py`: Lógica de negocio (guardado JSON, verificación de correlativas).
* `buildozer.spec`: Configuración para compilar el APK.

## Cómo ejecutar
1. Instalar dependencias: `pip install kivy`
2. Ejecutar: `python main.py`

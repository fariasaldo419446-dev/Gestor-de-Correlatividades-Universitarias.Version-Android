from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

from modelos import Materia
from modelos import Estado
from datos import crear_datos
from utils import (
    actualizar_disponibilidad,
    guardar_estados,
    cargar_estados,
    obtener_todas_materias_carrera,
)

Window.clearcolor = (1, 1, 1, 1)


class MallaApp(App):

    def build(self):
        self.current_materias = []
        self.materias_por_nivel = {}

        root = BoxLayout(orientation='vertical', spacing=dp(12), padding=dp(12), size_hint=(1, 1))

        header = BoxLayout(size_hint=(1, None), height=dp(70), padding=(dp(20), 0), spacing=dp(10))
        header_label = Label(
            text='Malla Universitaria',
            color=(1, 1, 1, 1),
            size_hint=(1, 1),
            bold=True,
            font_size='24sp',
            halign='center',
            valign='middle',
            text_size=(Window.width - dp(40), dp(70)),
            shorten=True,
            shorten_from='right',
        )
        header.add_widget(header_label)

        with header.canvas.before:
            Color(0.45, 0.25, 0.8, 1)
            self.bg_header = RoundedRectangle(pos=header.pos, size=header.size, radius=[30])
        header.bind(pos=self._update_header_bg, size=self._update_header_bg)
        root.add_widget(header)

        # Cargar datos usando la función importada directamente, sin self.
        self.datos = crear_datos()

        main_layout = BoxLayout(orientation='vertical', size_hint=(1, 1), spacing=dp(16), padding=dp(16))

        self.univ_spinner = self.crear_spinner('Seleccionar Universidad', sorted(list(self.datos.keys())))
        self.univ_spinner.bind(text=self.on_universidad_selected)

        self.facu_spinner = self.crear_spinner('Seleccionar Facultad', [], disabled=True)
        self.facu_spinner.bind(text=self.on_facultad_selected)

        self.carrera_spinner = self.crear_spinner('Seleccionar carrera', [], disabled=True)
        self.carrera_spinner.bind(text=self.on_carrera_selected)

        self.tipo_materia_spinner = self.crear_spinner('Seleccionar tipo de materia', [], disabled=True)
        self.tipo_materia_spinner.bind(text=self.on_tipo_materia_selected)

        self.nivel_spinner = self.crear_spinner('Seleccionar año de cursado', [], disabled=True)
        self.nivel_spinner.bind(text=self.on_nivel_selected)

        self.materias_layout = BoxLayout(orientation='vertical', spacing=dp(8), size_hint_y=None)
        self.materias_layout.bind(minimum_height=self.materias_layout.setter('height'))

        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.materias_layout)

        main_layout.add_widget(self.univ_spinner)
        main_layout.add_widget(self.facu_spinner)
        main_layout.add_widget(self.carrera_spinner)
        main_layout.add_widget(self.tipo_materia_spinner)
        main_layout.add_widget(self.nivel_spinner)
        main_layout.add_widget(scroll)

        root.add_widget(main_layout)

        cargar_estados(self.datos)

        return root

    def _update_header_bg(self, instance, value):
        self.bg_header.pos = instance.pos
        self.bg_header.size = instance.size

    def crear_spinner(self, texto, valores, disabled=False):
        spinner = Spinner(
            text=texto,
            values=valores,
            size_hint=(1, None),
            size=(dp(280), dp(48)),
            background_color=(0.45, 0.25, 0.8, 1),
            color=(1, 1, 1, 1),
            disabled=disabled,
            font_size='18sp',
        )
        return spinner

    def on_universidad_selected(self, spinner, text):
        if text == 'Seleccionar Universidad':
            self.facu_spinner.values = []
            self.facu_spinner.text = 'Seleccionar Facultad'
            self.facu_spinner.disabled = True
            self.carrera_spinner.values = []
            self.carrera_spinner.text = 'Seleccionar carrera'
            self.carrera_spinner.disabled = True
            self.tipo_materia_spinner.values = []
            self.tipo_materia_spinner.text = 'Seleccionar tipo de materia'
            self.tipo_materia_spinner.disabled = True
            self.nivel_spinner.values = []
            self.nivel_spinner.text = 'Seleccionar año de cursado'
            self.nivel_spinner.disabled = True
            self.limpiar_materias()
            return

        facultades = list(self.datos[text].keys())
        self.facu_spinner.values = facultades
        self.facu_spinner.text = 'Seleccionar Facultad'
        self.facu_spinner.disabled = False
        self.carrera_spinner.values = []
        self.carrera_spinner.text = 'Seleccionar carrera'
        self.carrera_spinner.disabled = True
        self.tipo_materia_spinner.values = []
        self.tipo_materia_spinner.text = 'Seleccionar tipo de materia'
        self.tipo_materia_spinner.disabled = True
        self.nivel_spinner.values = []
        self.nivel_spinner.text = 'Seleccionar año de cursado'
        self.nivel_spinner.disabled = True
        self.limpiar_materias()

    def on_facultad_selected(self, spinner, text):
        universidad = self.univ_spinner.text
        if text == 'Seleccionar Facultad' or universidad == 'Seleccionar Universidad':
            self.carrera_spinner.values = []
            self.carrera_spinner.text = 'Seleccionar carrera'
            self.carrera_spinner.disabled = True
            self.tipo_materia_spinner.values = []
            self.tipo_materia_spinner.text = 'Seleccionar tipo de materia'
            self.tipo_materia_spinner.disabled = True
            self.nivel_spinner.values = []
            self.nivel_spinner.text = 'Seleccionar año de cursado'
            self.nivel_spinner.disabled = True
            self.limpiar_materias()
            return

        carreras = list(self.datos[universidad][text].keys())
        self.carrera_spinner.values = carreras
        self.carrera_spinner.text = 'Seleccionar carrera'
        self.carrera_spinner.disabled = False
        self.tipo_materia_spinner.values = []
        self.tipo_materia_spinner.text = 'Seleccionar tipo de materia'
        self.tipo_materia_spinner.disabled = True
        self.nivel_spinner.values = []
        self.nivel_spinner.text = 'Seleccionar año de cursado'
        self.nivel_spinner.disabled = True
        self.limpiar_materias()

    def on_carrera_selected(self, spinner, text):
        universidad = self.univ_spinner.text
        facultad = self.facu_spinner.text
        if (text == 'Seleccionar carrera' or
                universidad == 'Seleccionar Universidad' or
                facultad == 'Seleccionar Facultad'):
            self.tipo_materia_spinner.values = []
            self.tipo_materia_spinner.text = 'Seleccionar tipo de materia'
            self.tipo_materia_spinner.disabled = True
            self.nivel_spinner.values = []
            self.nivel_spinner.text = 'Seleccionar año de cursado'
            self.nivel_spinner.disabled = True
            self.limpiar_materias()
            return

        self.tipo_materia_spinner.values = ['Materias Obligatorias', 'Materias Electivas']
        self.tipo_materia_spinner.text = 'Seleccionar tipo de materia'
        self.tipo_materia_spinner.disabled = False
        self.nivel_spinner.values = []
        self.nivel_spinner.text = 'Seleccionar año de cursado'
        self.nivel_spinner.disabled = True
        self.limpiar_materias()

    def on_tipo_materia_selected(self, spinner, text):
        if text not in ['Materias Obligatorias', 'Materias Electivas']:
            self.nivel_spinner.values = []
            self.nivel_spinner.text = 'Seleccionar año de cursado'
            self.nivel_spinner.disabled = True
            self.limpiar_materias()
            return

        universidad = self.univ_spinner.text
        facultad = self.facu_spinner.text
        carrera = self.carrera_spinner.text

        self.current_materias = self.datos[universidad][facultad][carrera][
            'obligatorias' if text == 'Materias Obligatorias' else 'electivas']

        niveles_unicos = sorted(set(m.nivel for m in self.current_materias))
        self.materias_por_nivel = {nivel: [m for m in self.current_materias if m.nivel == nivel] for nivel in niveles_unicos}

        self.nivel_spinner.values = [str(n) for n in niveles_unicos]
        self.nivel_spinner.text = 'Seleccionar año de cursado'
        self.nivel_spinner.disabled = False

        self.limpiar_materias()

    def on_nivel_selected(self, spinner, text):
        if text == 'Seleccionar año de cursado':
            self.limpiar_materias()
            return
        nivel = int(text)
        materias = self.materias_por_nivel.get(nivel, [])
        self.mostrar_materias(materias)

    def mostrar_materias(self, materias):
        self.limpiar_materias()

        for m in materias:
            if not isinstance(m, Materia):
                continue

        todas_materias = obtener_todas_materias_carrera(
            self.datos,
            self.univ_spinner.text,
            self.facu_spinner.text,
            self.carrera_spinner.text
        )
        actualizar_disponibilidad(todas_materias)

        for m in materias:
            btn = Button(
                text=m.nombre,
                size_hint_y=None,
                height=dp(40),
                background_normal='',
                background_color=Estado.colores[m.estado],
                disabled=not m.disponible,
                color=(0, 0, 0, 1),
                font_size='16sp',
                bold=True,
                padding=(dp(10), 0)
            )
            btn.bind(on_release=lambda btn, mat=m: self.abrir_popup_estado(mat))
            m.btn = btn
            self.materias_layout.add_widget(btn)

    def abrir_popup_estado(self, materia):
        contenido = BoxLayout(orientation='vertical', spacing=15, padding=15)
        label = Label(text=f"Estado actual: {materia.estado}\nSeleccione nuevo estado:")
        contenido.add_widget(label)

        opciones = [Estado.NO_CURSADA, Estado.REGULAR, Estado.CURSANDO, Estado.APROBADA]
        spinner = Spinner(
            text=materia.estado,
            values=opciones,
            size_hint=(1, None),
            height=dp(44)
        )
        contenido.add_widget(spinner)

        btn_confirmar = Button(text="Confirmar", size_hint=(1, None), height=dp(44))
        contenido.add_widget(btn_confirmar)

        popup = Popup(title=f"Cambiar estado - {materia.nombre}", content=contenido,
                      size_hint=(None, None), size=(dp(320), dp(240)), auto_dismiss=True)

        def confirmar_estado(instance):
            materia.estado = spinner.text

            todas = obtener_todas_materias_carrera(
                self.datos,
                self.univ_spinner.text,
                self.facu_spinner.text,
                self.carrera_spinner.text
            )
            actualizar_disponibilidad(todas)
            guardar_estados(self.datos)
            popup.dismiss()

        btn_confirmar.bind(on_release=confirmar_estado)
        popup.open()

    def limpiar_materias(self):
        self.materias_layout.clear_widgets()

    def resetear_desde(self, nivel):
        if nivel in ['universidad', 'facultad']:
            self.facu_spinner.text = 'Seleccionar Facultad'
            self.facu_spinner.disabled = True
        if nivel in ['universidad', 'facultad', 'carrera']:
            self.carrera_spinner.text = 'Seleccionar carrera'
            self.carrera_spinner.disabled = True
        if nivel in ['universidad', 'facultad', 'carrera', 'tipo']:
            self.tipo_materia_spinner.text = 'Seleccionar tipo de materia'
            self.tipo_materia_spinner.disabled = True
        self.nivel_spinner.text = 'Seleccionar año de cursado'
        self.nivel_spinner.disabled = True
        self.limpiar_materias()


if __name__ == '__main__':
    MallaApp().run()

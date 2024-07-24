from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

class ProjectDescriptionApp(App):
    def build(self):
        # Definir fundo escuro
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(
            text="Projeto 1: Aplicativo JavaScript com Electron",
            color=(1, 1, 1, 1),
            font_size='24sp',
            bold=True,
            size_hint_y=None,
            height=40,
            halign='center'
        )
        
        description_text = (
            "Este projeto é um aplicativo desenvolvido com Electron, "
            "que carrega o ChatGPT em uma janela de navegador customizada. "
            "O aplicativo oferece controles de janela (minimizar, maximizar e fechar) "
            "e manipula a navegação para melhorar a segurança."
        )
        
        scrollview = ScrollView(size_hint=(1, 0.3))
        description = Label(
            text=description_text,
            color=(1, 1, 1, 1),
            font_size='18sp',
            text_size=(Window.width - 60, None),
            halign='center',
            valign='middle',
            size_hint_y=None
        )
        description.bind(size=description.setter('text_size'))
        scrollview.add_widget(description)
        
        # Ajustar o caminho da imagem para garantir que seja carregada corretamente
        image_path = os.path.join(os.path.dirname(__file__), 'imagem.jpg')
        image = Image(source=image_path, size_hint=(1, 0.6), allow_stretch=True)
        
        button_layout = BoxLayout(size_hint=(1, 0.2))
        
        close_button = Button(
            text='Fechar',
            size_hint=(0.4, 1),
            background_color=(0, 0.5, 1, 1),
            color=(1, 1, 1, 1),
            font_size='18sp',
            bold=True,
            pos_hint={'center_x': 0.5}
        )
        close_button.bind(on_press=self.close_popup)
        
        back_button = Button(
            text='Voltar',
            size_hint=(0.4, 1),
            background_color=(1, 0.5, 0, 1),
            color=(1, 1, 1, 1),
            font_size='18sp',
            bold=True,
            pos_hint={'center_x': 0.5}
        )
        back_button.bind(on_press=self.close_popup)
        
        button_layout.add_widget(close_button)
        button_layout.add_widget(back_button)
        
        layout.add_widget(title)
        layout.add_widget(scrollview)
        layout.add_widget(image)
        layout.add_widget(button_layout)
        
        return layout
    
    def close_popup(self, instance):
        self.stop()

def run():
    ProjectDescriptionApp().run()

if __name__ == "__main__":
    run()

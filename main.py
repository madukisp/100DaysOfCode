from kivy.config import Config

# Desativar provedores problemáticos
Config.set('input', 'wm_touch', 'disable')
Config.set('input', 'wm_pen', 'disable')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
import subprocess
import os

class ProjectLauncher(App):
    def build(self):
        # Definir fundo escuro
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Fundo escuro (rgba)

        layout = BoxLayout(orientation='vertical')
        
        label = Label(text='Selecione um Projeto para Executar', size_hint=(1, 0.1), color=(1, 1, 1, 1))
        layout.add_widget(label)
        
        scrollview = ScrollView(size_hint=(1, 0.9))
        grid_layout = GridLayout(cols=5, size_hint_y=None, spacing=10, padding=10)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Lista de nomes personalizados para os projetos
        project_names = [
            "Projeto JS", "Projeto Preços", "Projeto Lista de Compras", "Projeto Interface",
            "Projeto 5", "Projeto 6", "Projeto 7", "Projeto 8", "Projeto 9", "Projeto 10",
            # Adicione mais nomes conforme necessário
        ]
        
        for i, project_name in enumerate(project_names, start=1):
            btn = Button(text=project_name, size_hint_y=None, height=40, background_color=(0, 0.5, 1, 1), color=(1, 1, 1, 1))
            btn.bind(on_press=lambda btn, i=i: self.run_project(i))
            grid_layout.add_widget(btn)
        
        scrollview.add_widget(grid_layout)
        layout.add_widget(scrollview)
        
        return layout

    def run_project(self, project_number):
        try:
            # Caminho do arquivo main.py do projeto
            project_path = os.path.join('04-py-interface', f'projeto{project_number}', 'main.py')
            if os.path.exists(project_path):
                # Executar o projeto em um novo processo
                subprocess.Popen(['python', project_path])
                print(f'Executando Projeto {project_number}')
            else:
                self.show_error_popup(f'Arquivo {project_path} não encontrado.')
        except Exception as e:
            self.show_error_popup(f'Erro ao executar o projeto {project_number}: {e}')
    
    def show_error_popup(self, message):
        popup = Popup(title='Erro',
                      content=Label(text=message),
                      size_hint=(0.8, 0.2))
        popup.open()

if __name__ == '__main__':
    ProjectLauncher().run()

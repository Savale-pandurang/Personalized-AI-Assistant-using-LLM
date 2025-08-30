from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

SERVER_BASE = "http://127.0.0.1:8000"  # change to your Mac's LAN IP

class RozClient(App):
    def build(self):
        self.title = "Roz"
        root = BoxLayout(orientation='vertical', padding=12, spacing=8)
        self.log = Label(text='Roz client ready', size_hint_y=0.9)
        row = BoxLayout(size_hint_y=0.1)
        self.inp = TextInput(hint_text='Type message', multiline=False)
        btn = Button(text='Send')
        btn.bind(on_release=self.send)
        row.add_widget(self.inp)
        row.add_widget(btn)
        root.add_widget(self.log)
        root.add_widget(row)
        return root

    def add(self, who, text):
        self.log.text += f"\n{who}: {text}"

    def send(self, *_):
        msg = self.inp.text.strip()
        if not msg:
            return
        self.add('You', msg)
        self.inp.text = ''
        try:
            r = requests.post(f"{SERVER_BASE}/chat", json={"message": msg})
            data = r.json()
            self.add('Roz', data.get('reply', ''))
        except Exception as e:
            self.add('Roz', f"Error: {e}")

if __name__ == '__main__':
    RozClient().run()



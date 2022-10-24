#!/usr/bin/env python
"""
This demo can be ran from the project root directory via:
```sh
python src/main.py
```
It can also be ran via p4a/buildozer.
"""
from kivy.app import App
from kivy.lang import Builder

presentation = Builder.load_file("main.kv")

class DemoApp(App):
    def check_data(self):
        lbltext = self.ids['lbl1'].text
        print(lbltext)

    def build(self):
        return presentation


if __name__ == '__main__':
    DemoApp().run()
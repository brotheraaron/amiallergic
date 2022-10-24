from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy_garden.zbarcam import ZBarCam

class QrScanner(BoxLayout):
    def __init__(self, **kwargs):
        super(QrScanner, self).__init__(**kwargs)
        btn1 = Button(text='Scan Me', font_size="50sp", size_hint=(1.0, 0.3), pos_hint={'x': 0.0,'bottom': 1})
        btn1.bind(on_press=self.callback)
        self.add_widget(btn1)
        btn2 = Button(text='Exit', font_size="50sp", size_hint=(1.0, 0.3), pos_hint={'x': 0.0,'bottom': 1})
        btn2.bind(on_press=quit)
        self.add_widget(btn2)

    def callback(self, instance):
        """On click button, initiate zbarcam and schedule text reader"""
        self.remove_widget(instance) # remove button
        self.zbarcam = ZBarCam()
        self.add_widget(self.zbarcam)
        Clock.schedule_interval(self.read_qr_text, 1)

    def read_qr_text(self, *args):
        """Check if zbarcam.symbols is filled and stop scanning in such case"""
        if(len(self.zbarcam.symbols) > 0): # when something is detected
            self.qr_text = self.zbarcam.symbols[0].data # text from QR
            Clock.unschedule(self.read_qr_text, 1)
            self.zbarcam.stop() # stop zbarcam
            lbl1 = Label(size_hint=(1.0,0.3), pos_hint={'x': 0.0,'top': 0.5}, text=self.qr_text.decode("utf-8"))
            self.add_widget(lbl1)


# https://world.openfoodfacts.org/api/v2/product/3017620429484.json
# ingredients_hierarchy
# ingredients_text

class QrApp(App):
    def build(self):
        return QrScanner()

if __name__ == '__main__':
    QrApp().run()
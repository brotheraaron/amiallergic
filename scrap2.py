def read_qr_text(self, *args):
        """Check if zbarcam.symbols is filled and stop scanning in such case"""
        if(1 > 0): # when something is detected
            self.qr_text = "text from QR"
            print(self.qr_text)
            # self.zbarcam.ids['xcamera']._camera._device.release() # release camera

newVar = read_qr_text()
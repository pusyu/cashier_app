import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.uix.button import Button

from kivy.utils import get_color_from_hex

Window.size = (375, 812)
Window.orientation = 'portrait'

list_makanan = [
    ["1. N.Paket 10K", 10000],
    ["2. N.Campur 13K", 13000],
    ["3. N.Goreng 12K", 12000],
    ["4. N.Sotong 13K", 13000],
    ['5. N.Dagang 6K', 6000],
    ["6. N.Putih + A.Crispy 13K", 13000],
    ["7. Pop Mie 6K", 6000],
    ["8. N.Kuning + A.Crispy 13K", 13000],
    ["9. Mie Lendir 12K", 12000],
    ["10. N.Kuning + Te.Dadar 10K", 10000],
    ["11. Ayam Bakar 15K", 15000],
    ["12. N.Paket + Te.Dadar 10K", 10000],
    ["13. Lakse 6K", 6000],
    ["14. N.Putih + A.Geprek 13K", 13000],
    ["15. Kwetiau 10K", 10000],
    ["16. Bubur Kacang hijau 6K", 6000],
    ["17. Bubur Ketan 6K", 6000],
    ["18. Bubur Ayam 10K", 10000],
    ["19. Indomie G 10K", 10000],
    ["20. Indomie R 10K", 10000],
    ["21. Mie Tarempak 10K", 10000],
    ["22. Gado-gado 10K", 10000],
    ["23. Prata 10K", 10000],
    ["24. Sate Ayam 12K", 12000],
    ["25. Lontong Sayur 10K", 10000],
    ["26. P.Keju Coklat 5K", 5000],
    ["27. Soto 10K", 10000],
    ["28. S.Ayam + Nasi 12K", 12000],
    ["29. Tela-Tela 5K", 5000],
    ["30. Empek-Empek 7K", 7000]

]
list_minuman = [
    ["1. Extrajoss Susu 6K", 6000],
    ["2. Kuku Bima Susu 6K", 6000],
    ["3. Coffee Susu 6K", 6000],
    ["4. Coffemix Es 6K", 6000],
    ["5. Cappucino Es 6K", 6000],
    ["6. Cappucino Panas 6K", 6000],
    ["7. Milo Es 6K", 6000],
    ["8. Milo Panas 6K", 6000],
    ["9. Susu Putih 5K", 5000],
    ["10. Coffemix 5K", 5000],
    ["11. Jeruk Peras 4K", 4000],
    ["12. Kopi O 4K", 4000],
    ["13. Kuku Bima B 4K", 4000],
    ["14. Extrajos B 4K", 4000],
    ["15. Air Asam 4K", 4000],
    ["16. Teh Obeng 4K", 4000],
    ["17. Bestari 4K", 4000],
    ["18. Teh O 4K", 5000],
    ["19. Es Kosong 2K", 2000],
    ["20. Air Putih 1K", 1000]

]


list_makanan_yang_dimasukin = []
total_harga_makanan_yang_dimasukin = 0
list_minuman_yang_dimasukin = []



def callbackMakanan(instance):
    print('The button <%s> is being pressed' % instance.text)
    global list_makanan_yang_dimasukin
    global total_harga_makanan_yang_dimasukin
    global list_minuman_yang_dimasukin

    list_makanan_yang_dimasukin.append(instance.text)

    for i in range(0, len(list_makanan)):
        if (instance.text == list_makanan[i][0]):
            total_harga_makanan_yang_dimasukin += list_makanan[i][1]


def callbackMinuman(instance):
    print('The button <%s> is being pressed' % instance.text)
    global list_makanan_yang_dimasukin
    global total_harga_makanan_yang_dimasukin
    global list_minuman_yang_dimasukin

    list_minuman_yang_dimasukin.append(instance.text)

    for i in range(0, len(list_minuman)):
        if (instance.text == list_minuman[i][0]):
            total_harga_makanan_yang_dimasukin += list_minuman[i][1]


total = 0


def countTotal(instance):
    data = [1]
    data.append(222)
    print("total = ", total_harga_makanan_yang_dimasukin)
    print(list_makanan_yang_dimasukin)
    print(data)


class MenuMakanan(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press=self.show_menu)

    def show_menu(self, instance):
        content = BoxLayout(orientation='vertical')
        content = GridLayout(cols=2)
        close_button = Button(text='Close')
        close_button.background_color = get_color_from_hex("#d9133c")
        close_button.bind(on_press=self.close_menu)
        # ini ui dengan loop biar ga panjang hehe ####
        btnMakanan = []
        for i in range(0, len(list_makanan)):
            temp = Button(text=list_makanan[i][0], font_size='12sp')
            temp.bind(on_press=callbackMakanan)
            btnMakanan.append(temp)
        for i in range(0, len(list_makanan)):
            content.add_widget(btnMakanan[i])
      
        content.add_widget(close_button)
        self.popup = Popup(title='Mau makan apa?', content=content)
        self.popup.open()

    def close_menu(self, instance):
        self.popup.dismiss()


class MenuMinuman(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press=self.show_menu)

    def show_menu(self, instance):
        content = BoxLayout(orientation='vertical')
        content = GridLayout(cols=2)
        close_button = Button(text='Close')
        close_button.background_color = get_color_from_hex("#d9133c")
        close_button.bind(on_press=self.close_menu)

        btnMinuman = []
        for i in range(0, len(list_minuman)):
            temp = Button(text=list_minuman[i][0], font_size='12sp')
            temp.bind(on_press=callbackMinuman)
            btnMinuman.append(temp)
        for i in range(0, len(list_minuman)):
            content.add_widget(btnMinuman[i])
      
        content.add_widget(close_button)
        self.popup = Popup(title='Mau minum apa?', content=content)
        self.popup.open()

    def close_menu(self, instance):
        self.popup.dismiss()


class Pesan(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press=self.show_menu)

    def show_menu(self, instance):
        content = BoxLayout(orientation='vertical')
        content = GridLayout(cols=2)
        close_button = Button(text='Close')
        close_button.bind(on_press=self.close_menu)
        ################################
        content.add_widget(Button(text='Nama pembeli'))
        self.name_input = TextInput(hint_text='Masukkan nama')
        content.add_widget(self.name_input)
        ###############################################
        content.add_widget(Button(text='Menu makanan'))
        stringMakanan = ""
        for i in range(0, len(list_makanan_yang_dimasukin)):
            stringMakanan += list_makanan_yang_dimasukin[i] + ", \n"
        content.add_widget(Label(text=str(stringMakanan)))
        ##############################################
        content.add_widget(Button(text='Menu minuman'))
        stringMinuman = ""
        for i in range(0, len(list_minuman_yang_dimasukin)):
            stringMinuman += list_minuman_yang_dimasukin[i] + ", \n"
        content.add_widget(Label(text=str(stringMinuman)))
        ##########################################################
        content.add_widget(close_button)
        content.add_widget(Label(text="total harga = Rp." +
                                 str(total_harga_makanan_yang_dimasukin)))
        self.popup = Popup(title='Mau makan apa?', content=content)
        self.popup.open()

    def close_menu(self, instance):
        self.popup.dismiss()


class CashierApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(MenuMakanan(text='Food Menu',
                          background_color=get_color_from_hex("##feafca")))
        layout.add_widget(MenuMinuman(text='Drink Menu',
                          background_color=get_color_from_hex("#fe7ba7")))
        layout.add_widget(
            Pesan(text='Pesan', background_color=get_color_from_hex("#984964")))
        return layout


if __name__ == '__main__':
    CashierApp().run()

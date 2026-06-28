import numpy as np
import matplotlib
matplotlib.use('Agg')  # Kivy ilə işləmək üçün vacib backend ayarı
import matplotlib.pyplot as plt
from pydantic import BaseModel, Field

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window

# 1. Pydantic ilə Məlumat Modelinin Strukturunu Qururuq
class HesablamaModeli(BaseModel):
    faza_bucagi: float = Field(..., ge=0, le=360, description="Faza bucağı 0 ilə 360 dərəcə arasında olmalıdır.")
    amplituda: float = Field(..., gt=0, description="Amplituda sıfırdan böyük olmalıdır.")

# 2. Əsas İnterfeys və Məntiq Sinfi
class RiyaziEkran(BoxLayout):
    def __init__(self, **kwargs):
        super(RiyaziEkran, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Başlıq
        self.add_widget(Label(text="Kivy + Matplotlib Grafik Yaratmaq", font_size=24, size_hint_y=None, height=40))

        # Giriş sahəsi: Faza Bucaqı
        self.add_widget(Label(text="Faza Bucaqını Daxil Edin (0 - 360°):", size_hint_y=None, height=30))
        self.faza_input = TextInput(text="0", multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.faza_input)

        # Giriş sahəsi: Amplituda
        self.add_widget(Label(text="Amplitudanı Daxil Edin (> 0):", size_hint_y=None, height=30))
        self.amp_input = TextInput(text="1.0", multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.amp_input)

        # Düymə
        self.Hesabla_btn = Button(text="Qrafiki Yarat", size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.4, 1))
        self.Hesabla_btn.bind(on_press=self.qrafik_ciz)
        self.add_widget(self.Hesabla_btn)

        # Status və ya Xəta Mesajı üçün Label
        self.status_label = Label(text="Məlumat daxil edin və düyməyə basın.", size_hint_y=None, height=30, color=(1, 1, 1, 1))
        self.add_widget(self.status_label)

        # Qrafikin görünəcəyi yer (Image widget)
        self.qrafik_yeri = Image(source='')
        self.add_widget(self.qrafik_yeri)

    def qrafik_ciz(self, instance):
        try:
            # Pydantic ilə istifadəçi girişini yoxlayırıq və doğrulayırıq
            data = HesablamaModeli(
                faza_bucagi=float(self.faza_input.text),
                amplituda=float(self.amp_input.text)
            )
            
            # Əgər bura çatdısa, məlumat doğrudur. Xəta mesajını təmizləyirik.
            self.status_label.text = "Qrafik uğurla yaradıldı!"
            self.status_label.color = (0.2, 1, 0.2, 1)

            # Numpy ilə sinus dalğası hesablanması
            x = np.linspace(0, 4 * np.pi, 1000)
            faza_rad = np.radians(data.faza_bucagi)
            y = data.amplituda * np.sin(x + faza_rad)

            # Matplotlib ilə qrafikin çəkilməsi
            plt.figure(figsize=(6, 4))
            plt.plot(x, y, label=f"Sinus (Faza={data.faza_bucagi}°, Amp={data.amplituda})", color="crimson", linewidth=2)
            plt.title("Numpy və Matplotlib Dalğası")
            plt.xlabel("Zaman / Bucaq")
            plt.ylabel("Dəyər")
            plt.grid(True)
            plt.legend()
            
            # Şəkli yaddaşa yazırıq ki, Kivy-də göstərə bilək
            fayl_adi = "sinus_plot.png"
            plt.savefig(fayl_adi, dpi=150, bbox_inches='tight')
            plt.close()

            # Kivy Image widget-ni yeniləyirik
            self.qrafik_yeri.source = fayl_adi
            self.qrafik_yeri.reload()

        except ValueError:
            self.status_label.text = "Xəta: Zəhmət olmasa düzgün ədədlər daxil edin!"
            self.status_label.color = (1, 0.2, 0.2, 1)
        except Exception as e:
            # Pydantic xətalarını tutmaq üçün
            self.status_label.text = f"Xəta: {str(e)}"
            self.status_label.color = (1, 0.2, 0.2, 1)

# 3. Kivy Tətbiqini Başladan Əsas Sinif
class MatematikApp(App):
    def build(self):
        return RiyaziEkran()

if __name__ == '__main__':
    MatematikApp().run()
    # yenilendi


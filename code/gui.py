from tkinter import *
import customtkinter
from run_track import *
import customtkinter as ctk
import tkinter


class Window(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.translator = Translator()

        self.root_tk = customtkinter.CTk()
        self.root_tk.title("My translator")
        self.root_tk.geometry('700x700')
        self.root_tk.configure(bg='black')

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        customtkinter.set_default_color_theme('blue')

        record_button = customtkinter.CTkButton(self.root_tk, text="Nagrywanie dźwięku", command=self.record_button_logic)
        transcribe_button = customtkinter.CTkButton(self.root_tk, text="Transkrypcja", command=self.transcribe_button_logic)
        translate_button = customtkinter.CTkButton(self.root_tk, text="Tłumaczenie", command=self.translate_button_logic)
        language_detection = customtkinter.CTkButton(self.root_tk, text="Detekcja języka", command=self.detect_button_logic)

        record_button.place(relx=0.5, rely=0.1, anchor=CENTER)
        transcribe_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        translate_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        language_detection.place(relx=0.5, rely=0.7, anchor=CENTER)
        # transcribe_button.pack()
        # translate_button.pack()
        # language_detection.pack()

        self.root_tk['background'] = '#ffbb99'
        # self.root_tk.mainloop()

    def record_button_logic(self):
        # my_label = Label(root_tk, text="Nagranie rozpoczęte")
        # my_label.place(relx=0.5, rely=0.12, anchor = CENTER)
        print_this = customtkinter.CTkLabel(self.root_tk, text='Dźwięk został nagrany poprawnie', bg_color="#ffbb99")
        print_this.place(relx=0.5, rely=0.17, anchor=CENTER)
        self.translator.record_audio()

    def transcribe_button_logic(self):
        label_transcribe = self.translator.transcribe_text('recording2.wav')
        print_this = customtkinter.CTkLabel(self.root_tk, text=label_transcribe, bg_color="#ffbb99")
        print_this.place(relx=0.5, rely=0.37, anchor=CENTER)

    def translate_button_logic(self):
        label_translate = self.translator.translate_text('recording2.wav')
        print_this = customtkinter.CTkLabel(self.root_tk, text=label_translate, bg_color="#ffbb99")
        print_this.place(relx=0.5, rely=0.57, anchor=CENTER)

    def detect_button_logic(self):
        label_detect = self.translator.detect_language('recording2.wav')
        print_this = customtkinter.CTkLabel(self.root_tk, text=label_detect, bg_color="#ffbb99")
        print_this.place(relx=0.5, rely=0.77, anchor=CENTER)

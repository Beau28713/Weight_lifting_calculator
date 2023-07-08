from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

import pandas


class Train_App(FloatLayout):
    def __init__(self, **kwargs):
        super(Train_App, self).__init__(**kwargs)

        Window.size = (800, 300)

        self.weight = TextInput(
            multiline=False,
            text="weight",
            size_hint=(0.2, 0.1),
            pos_hint={"x": 0, "top": 0.99},
        )

        self.reps = TextInput(
            multiline=False,
            text="Reps",
            size_hint=(0.2, 0.1),
            pos_hint={"x": 0, "top": 0.89},
        )

        self.percentage_label = Label(
            text="Percentage of max",
            size_hint=(0.2, 0.1),
            pos_hint={"x": 0.25, "top": 0.20},
        )
        self.percentage_output = TextInput(
            multiline=False, size_hint=(0.33, 0.80), pos_hint={"x": 0.25, "top": 0.99}
        )
        self.max_label = Label(
            text="Calculated Max's",
            size_hint=(0.2, 0.1),
            pos_hint={"x": 0.65, "top": 0.2},
        )
        self.max_output = TextInput(
            readonly=True,
            size_hint=(0.4, 0.7),
            pos_hint={"x": 0.60, "top": 0.99},
        )
        self.enter_buton = Button(
            size_hint=(0.1, 0.1),
            pos_hint={"x": 0.01, "top": 0.70},
            text="Enter",
            on_press=self.rep_max,
        )
        self.size = (300, 300)
        self.add_widget(self.weight)
        self.add_widget(self.reps)
        self.add_widget(self.max_output)
        self.add_widget(self.max_label)
        self.add_widget(self.percentage_label)
        self.add_widget(self.percentage_output)
        self.add_widget(self.enter_buton)

    def rep_max(self, instance):
        weight = int(self.weight.text)
        reps = int(self.reps.text)

        brycki = weight * (36 / (37 - reps))

        epley = weight * (1 + (0.0333 * reps))

        oConner = weight * (1 + (0.025 * reps))

        largest_max = max(brycki, epley, oConner)

        percentage_list = [
            (x / 10 * brycki, y / 10 * oConner) for x, y in enumerate(range(10))
        ]

        data = percentage_list
        headers = ["brycki", "oConner"]
        percentages = pandas.DataFrame(data, columns=headers)

        self.percentage_output.text = percentages.to_string()

        self.max = f"""
Your max using the following equations are:

Brycki  = {brycki:.2f}
Epley   = {epley:.2f}
oConner = {oConner:.2f}
            """
        self.max_output.text = self.max


class MY_App(App):
    def build(self):
        self.title = "Max Lift"
        return Train_App()


if __name__ == "__main__":
    MY_App().run()

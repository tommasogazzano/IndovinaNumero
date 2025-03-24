import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2025 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self._txtOutNMax = ft.TextField(label="NMax", disabled=True, width=200, value = self._controller.getNMax())
        self._txtOutTMax = ft.TextField(label="TMax", disabled=True, width=200, value = self._controller.getTMax())
        self._txtOutT = ft.TextField(label="T Rimanenti" ,disabled=True, width=200)

        self._txtIn = ft.TextField(label="Valore", width=200)
        self._btnReset = ft.ElevatedButton(text="Nuova Partita", width=200, on_click=self._controller.reset)
        self._btnPlay = ft.ElevatedButton(text="Gioca", width=200, on_click=self._controller.play)

        self._lv = ft.ListView(expand= True)

        row1 = ft.Container(self._titolo, alignment = ft.alignment.center)
        row2 = ft.Row([self._txtOutNMax, self._txtOutTMax, self._txtOutT], alignment= ft.MainAxisAlignment.CENTER)
        row3 = ft.Row([self._btnReset, self._txtIn, self._btnPlay], alignment= ft.MainAxisAlignment.CENTER)
        self._page.add(row1, row2, row3, self._lv)


        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()
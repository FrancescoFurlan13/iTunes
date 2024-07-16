import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceAlbum = None


    def handleCreaGrafo(self, e):
        self._model.build_graph(int(self._view._txtInDurata.value))
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Nodi del grafo: {len(self._model._nodes)}"))
        self._view.txt_result.controls.append(ft.Text(f"Archi del grafo: {len(self._model._edges)}"))

        listDD = []
        for e in self._model._edges:
            if e[0] not in listDD:
                listDD.append(e[0])
        listDD.sort(key=lambda x: x.Title, reverse=False)
        for i in listDD:
            self._view._ddAlbum.options.append(ft.dropdown.Option(i.Title))

        self._view.update_page()

    def getSelectedAlbum(self, e):
        pass
        print("getSelectedAlbum called")
        if e.control.data is None:
            self._choiceAlbum = None
        else:
            self._choiceAlbum = e.control.data
        print(self._choiceAlbum)

    def handleAnalisiComp(self, e):
        pass
        if self._choiceAlbum is None:
            warnings.warn("Album field not selected.")
            return
        sizeC, totDurata = self._model.getConnessaDetails(self._choiceAlbum)

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(
            f"La componente connessa che include {self._choiceAlbum} "
            f"ha dimensione {sizeC} e durata totale {totDurata}"))
        self._view.update_page()


    def handleGetSetAlbum(self, e):
        pass


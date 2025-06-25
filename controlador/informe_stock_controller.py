class InformeStockController:
    def __init__(self, vista, logic):
        self.vista = vista
        self.logic = logic
        self.conectar_eventos()
        self.vista.set_column_headers(["Nombre", "Precio", "Descripción", "Stock"])
        self.cargar_datos()

    def conectar_eventos(self):
        self.vista.on_exportar(self.exportar_csv)
        self.vista.on_cerrar(self.vista.close)

    def cargar_datos(self):
        try:
            datos = self.logic.obtener_datos_stock()
            self.vista.mostrar_datos(datos)
        except Exception as e:
            self.vista.mostrar_error(f"No se pudo cargar el informe:\n{e}")

    def exportar_csv(self):
        try:
            path = self.vista.obtener_ruta_guardado()
            if not path:
                return
            datos = self.vista.obtener_datos_tabla()
            self.vista.exportar_a_csv(path, datos)
            self.vista.mostrar_info("Éxito", "Informe exportado correctamente.")
        except Exception as e:
            self.vista.mostrar_error(f"No se pudo exportar el informe:\n{e}")




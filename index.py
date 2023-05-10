import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import datetime


app = Flask(__name__)


@app.route("/uf", methods=["GET"])
def get_uf():
    fecha = request.args.get("fecha")
    year = fecha.split("-")[2]

    # Verificar si la fecha es menor que "2013-01-01"
    if year < "2013":
        return jsonify({"error": "Por favor, ingrese una fecha mayor a 01-01-2013"})

    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"

    # Hacer una solicitud GET a la página
    response = requests.get(url)

    # Analizar el contenido de la página con BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar todas las tablas con clase "table"
    tables = soup.find_all("table", class_="table")

    # Crear una lista para almacenar los datos de las tablas
    data = []

    # Iterar sobre todas las tablas y extraer sus datos
    for table in tables:
        rows = table.find_all("tr")
        mes = ""
        for row in rows:
            th_element = row.find("th")
            if th_element and th_element.find("h2"):
                mes = th_element.find("h2").get_text().strip()
                break

        # Crear un diccionario para almacenar los datos del mes actual
        month_data = {}

        # Iterar sobre las filas y extraer los datos de los elementos th y td
        for i in range(1, len(rows)):
            cols = rows[i].find_all(
                ["th", "td"]
            )  # Buscar tanto los elementos th como td

            # Verificar si la fila tiene suficientes elementos para contener datos válidos
            if len(cols) >= 6:
                dia1 = cols[0].get_text().strip()
                uf1 = cols[1].get_text().strip()
                dia2 = cols[2].get_text().strip()
                uf2 = cols[3].get_text().strip()
                dia3 = cols[4].get_text().strip()
                uf3 = cols[5].get_text().strip()

                # Verificar si alguno de los campos UF está vacío
                if uf1 != "" and uf2 != "" and uf3 != "":
                    # Agregar los datos del día al diccionario del mes actual
                    month_data[dia1] = {"uf": uf1}
                    month_data[dia2] = {"uf": uf2}
                    month_data[dia3] = {"uf": uf3}

        # Verificar si el  mes no está vacío
        if month_data:
            # Agregar el  mes a la lista de datos
            data.append({mes: month_data})

    fecha_desglosada = datetime.datetime.strptime(fecha, "%d-%m-%Y")
    mes_numero = fecha_desglosada.month

    # Diccionario de nombres de mes en español
    nombres_meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    mes_nombre = nombres_meses[mes_numero]

    dia = fecha_desglosada.day

    print("Año:", year)
    print("Mes:", mes_nombre)
    print("Día:", dia)

    # buscando la uf con iterando en data con elmes y fecha solicitada
    for month_data in data:
        if mes_nombre in month_data:
            month_data = month_data[mes_nombre]
            for day, uf_data in month_data.items():
                if int(day) == dia:
                    uf_value = uf_data["uf"]
                    print("uf:", uf_value)
                    return jsonify({"uf": uf_value})

    return jsonify(
        {"error": "No se encontró el valor de la UF para el mes y día especificados"}
    )

    # Devolver los datos en formato JSON


if __name__ == "__main__":
    app.run(debug=True)

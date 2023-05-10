El Servicio de Impuestos Internos (SII) de Chile mantiene una tabla con los valores de la Unidad de Fomento actualizados para cada año. Tu desafío consiste en crear una API en Python que permita a los usuarios consultar el valor de la Unidad de Fomento para una fecha específica utilizando scraping.
necesito crear una API para consultar la Unidad de Fomento en Python, puedes crearme el codigo, los requisitos son:    

La API debe estar desarrollada en Python utilizando la librería "requests" u otra similar.
Para la API puedes usar el Framework que mas te guste.
No se puede utilizar Selenium debido al alto consumo de recursos que estas herramientas implican.
La API debe permitir consultar el valor de la Unidad de Fomento para una fecha específica, la cual debe ser ingresada como parámetro en la solicitud.
La fecha mínima que se puede consultar es el 01-01-2013, y no hay fecha máxima, ya que la tabla se actualiza constantemente.
La API debe devolver el valor de la Unidad de Fomento correspondiente a la fecha consultada.
La respuesta de la API debe estar en formato JSON.
Para ayudarte en el desarrollo de este desafío, puedes utilizar la tabla de valores de la Unidad de Fomento actualizados para cada año que se encuentra en el siguiente enlace: https://www.sii.cl/valores_y_fechas/uf/uf2023.htm       
por ultimo  la tabla de valores de la Unidad de Fomento actualizados para cada año que se encuentra en el siguiente tabla :      


respuesta: para ingresar en tu navegador coloca http://localhost:5000/uf?fecha=11-05-2014 por ejemplo y te devuelve la respuesta
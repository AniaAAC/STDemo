import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import time
from PIL import Image


#set up page configuration for streamlit
icon = 'logo_chameleon.png'
st.set_page_config(page_title='Chameleon',page_icon=icon,initial_sidebar_state='expanded',
                        layout='wide',menu_items={"about":'This streamlit application was developed by Chamaleon'})

title_text = '''<h1 style='font-size: 36px;text-align: center;'>CHAMELEON</h1><h2 style='font-size: 24px;color:#008891;text-align: center;'>“No es el más fuerte ni el más inteligente el que sobrevive, sino el más adaptable” -Charles Darwin</h2>'''
st.markdown(title_text, unsafe_allow_html=True)

#Barra de menu 
selected = option_menu(
                        menu_title=None,
                        options=["HOME","Análisis estadístico","Aprendizaje Automático","Tablero","Líneas de Acción Estratégicas","Nosotros"],
                        icons=["house", "bar-chart", "robot", "table","lightbulb", "envelope"],
                        default_index=1,
                        orientation="horizontal",
                        styles={"container": {"width": "100%","border": "1px ridge  ","background-color": "#002b36","primaryColor": "#FF69B4"},
                                "icon": {"color": "#F8CD47", "font-size": "20px"},
                                "nav-link": {
                                     "color": "#ffffff"  # Cambia el color de las letras a blanco
                                },
                                "nav-link-selected": {
                                    "color": "#F8CD47"  # Puedes personalizar el color del texto seleccionado si lo deseas
                                }})


#sección Home
if selected == "HOME":

     # Título
    st.markdown("""
    <div style="text-align: center; font-size: 36px;color:#e47551; font-weight: bold; margin-bottom: 20px;">
        Mejorando la productividad en el molino caliente 4
    </div>
    """, unsafe_allow_html=True)

    # Mostrar el logo de Ternium y tarjetas en la misma línea
    col1, col2, col3, col4 = st.columns([1, 2, 2, 2])


    # Logo de Ternium desde un archivo local
    with col1:
        try:
            #st.image("Ternium_Logo.svg.png", width=190)
            st.image("Ternium_Logo.jpeg", width= 200)
        except Exception as e:
            st.error(f"Error al cargar la imagen: {e}")


   # Tarjetas
    with col2:
        st.markdown("""
        <div class="card" style="background-color: #f9d19d; padding: 20px; border-radius: 10px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 200px; box-sizing: border-box;">
            <h3 style="color: #e47551;">Misión</h3>
            <p style="color: black;">“Crear valor con nuestros clientes, mejorando la competitividad y productividad conjunta” (Vedoya, 2022).</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card" style="background-color: #f9d19d; padding: 20px; border-radius: 10px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 200px; box-sizing: border-box;">
            <h3 style="color: #e47551;">Visión</h3>
            <p style="color: black;">“Ser la empresa siderúrgica líder de América, comprometida con el desarrollo de sus clientes, a la vanguardia en parámetros industriales y destacada por la excelencia de sus recursos humanos” (Vedoya, 2022).</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card" style="background-color: #f9d19d; padding: 20px; border-radius: 10px; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 200px; box-sizing: border-box;">
            <h3 style="color: #e47551;">Objetivo</h3>
            <p style="color: black;">Ofrecer valor a los stakeholders de la empresa mientras la empresa se posiciona como líder en América Latina y es competitiva en el mercado. Además, de enfocarse en brindar productos y servicios de manera sustentable.</p>
        </div>
        """, unsafe_allow_html=True)

    # Apartado del proceso y problemática
    st.markdown("---")
    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            process_image = Image.open("proceso_MC4.png") 
            st.image(process_image, caption="Fases del proceso", use_column_width=True)
        except Exception as e:
            st.error("Error al cargar la imagen del proceso: {}".format(e))

    with col2:
            st.markdown("""
            <div style="padding: 20px; background-color: #f9d19d; border-radius: 10px; height: 300px; display: flex; justify-content: center; align-items: center; text-align: center;">
                <div>
                    <h3 style="color: #e47551;">Problemática</h3>
                    <p style="color: black;">Los cuellos de botella recurrentes y las interrupciones en distintas fases del proceso limitan el rendimiento esperado, afectando la capacidad de producción y la estabilidad operativa. Nuestro objetivo es identificar y mitigar estos cuellos de botella, para mejorar la eficiencia general y minimizar el impacto de las microdemoras.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
 
  
#seccion Analisis estadístico
if selected == "Análisis estadístico":
       
    st.subheader(':red[Análisis Estadístico]')
    st.markdown('''**En esta sección, se presentará el análisis estadístico realizado, el cual se ha documentado exhaustivamente para proporcionar una comprensión clara de los procesos y resultados obtenidos. Es posible explorar el análisis, apoyado por gráficos y visualizaciones que permiten interpretar los hallazgos de manera efectiva. Además, se ofrecen botones para facilitar la descarga de los códigos utilizados, la presentación resumen del trabajo realizado, y la documentación completa en formato PDF.**''')

    # Agregar botones para descarga directa en una fila
    st.markdown("### Recursos descargables:")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with open("codigo_limpieza.ipynb", "rb") as file:
            st.download_button(
                label="Descargar código de Limpieza",
                data=file,
                file_name="codigo_limpieza.ipynb",
                mime="application/octet-stream",
            )

    with col2:
        with open("codigo_analisis.ipynb", "rb") as file:
            st.download_button(
                label="Descargar código del Análisis",
                data=file,
                file_name="codigo_analisis.ipynb",
                mime="application/octet-stream",
            )

    with col3:
        with open("presentacion.pdf", "rb") as file:
            st.download_button(
                label="Descargar presentación",
                data=file,
                file_name="presentacion.pdf",
                mime="application/pdf",
            )

    with col4:
        with open("documentacion.pdf", "rb") as file:
            st.download_button(
                label="Descargar documentación en PDF",
                data=file,
                file_name="documentacion.pdf",
                mime="application/pdf",
            )
   
    # URL del documento de Google Docs en formato de vista previa
    doc_url = "https://docs.google.com/document/d/1jqLza_eZFU-3WBU41FwVfatLebOSRkJjzkjDeNE1nwY/preview"
    
    # Mostrar el documento usando un iframe
    st.markdown(f"""
        <iframe src="{doc_url}" width="100%" height="600px" style="border:none;"></iframe>
    """, unsafe_allow_html=True)

#SECCIÓN APRENDIZAJE AUTOMÁTICO
if selected == "Aprendizaje Automático":
    st.subheader(":red[Aprendizaje Automático]")
    st.write("""
    En esta sección, se exploran los modelos de **aprendizaje automático** aplicados al proceso del Molino Caliente 4 (MC4). 
    A través de técnicas de aprendizaje supervisado y no supervisado, se busca mejorar la predicción y optimización de diferentes aspectos del proceso productivo.
    
    A continuación, se presentan los modelos utilizados para cada enfoque, así como la opción de descargar el código utilizado para cada uno de ellos. Los modelos supervisados y no supervisados fueron implementados con el objetivo de identificar patrones y predecir comportamientos clave, facilitando la toma de decisiones informadas para la mejora continua en la producción.

    **Modelos Supervisados**: Utilizan datos etiquetados para entrenar el modelo y realizar predicciones precisas sobre futuras observaciones.
    
    **Modelos No Supervisados**: Se emplean para descubrir patrones ocultos en los datos sin la necesidad de etiquetas previas, permitiendo una comprensión más profunda de los comportamientos y características no evidentes en el proceso.
    """)

    select_insight=option_menu('',options=["SUPERVISADO","NO SUPERVISADO"],
                                    icons=["graph-up", "diagram-3"],
                                    orientation='horizontal',
                                    styles={"container":{"border":"2px ridge "},
                                    "icon": {"color": "#F8CD47", "font-size": "20px"}})
            
    if select_insight =="SUPERVISADO":
         st.write("#### Modelos de aprendizaje supervisado")
         #Botón para descargar el código de los modelos
         #st.markdown("#### Recursos descargables:")
         col1, col2 = st.columns(2)

         with col1:
             with open("Supervisados.ipynb", "rb") as file:
                 st.download_button(
                     label="Descargar código de los modelos",
                     data=file,
                     file_name="Supervisados.ipynb",
                     mime="application/octet-stream",
                 )
         st.image("SUPERVISADO.jpg", use_column_width=True)
         st.image("SUPERVISADO2.jpg", use_column_width=True)
         
    if select_insight =="NO SUPERVISADO":
         st.write("#### Modelos de aprendizaje no supervisado")
         #Botón para descargar el código de los modelos
         #st.markdown("#### Recursos descargables:")
         col1, col2 = st.columns(2)

         with col1:
             with open("No_supervisados.ipynb", "rb") as file:
                 st.download_button(
                     label="Descargar código de los modelos",
                     data=file,
                     file_name="No_supervisados.ipynb",
                     mime="application/octet-stream",
                 )
         st.image("NO SUPERVISADO.jpg", use_column_width=True)
       

#SECCIÓN DE LÍNEAS DE ACCIÓN ESTRATÉGICAS
if selected == "Líneas de Acción Estratégicas":
    select_insight=option_menu('',options=["HALLAZGOS","RECOMENDACIONES"],
                                    icons=["search", "clipboard-data"],
                                    orientation='horizontal',
                                    styles={"container":{"border":"2px ridge "},
                                    "icon": {"color": "#F8CD47", "font-size": "20px"}})
            
    if select_insight =="HALLAZGOS":

        #opt=['Top 10 Accommodation with Highest price',
        st.markdown("## Hallazgos principales")

        # Primer hallazgo
        st.markdown("""
         ### Regresión Lineal Múltiple
        El modelo sugiere que algunos tipos de acero podrían estar asociados con tiempos más bajos en FM.
        """)
        
        # Segundo hallazgo
        st.markdown("""
        ### Random Forest
          El análisis de importancia mostró que las características más relevantes para predecir FM Thread Time fueron:
          - FM Thread Speed
          - 1st Accel Time
          - FM Final Speed
        """)
        
        # Tercer hallazgo
        st.markdown("""
        ### K-means Clustering
          Los resultados indican que para la fase de interés (FM), entre los clusters existe una mayor diferencia en el **FM Thread Time (Tiempo de FM)** y en las características del planchón:
          - Slab Width
          - Slab Thickness
          - Slab Length
          - Slab Weight
          
          **Cluster 0**: Plancones con mayor tiempo en FM, asociados a planchones más **anchos, cortos, pesados** y con una menor velocidad final en FM.<br>
          **Cluster 1**: Planchones con menor tiempo en FM, caracterizados por ser **más delgados, largos, menos pesados** y con una mayor velocidad final.<br><br>

          Realizamos una **prueba T para muestras independientes**, concluyendo que:<br>
             Existe una diferencia significativa en los tiempos de demora de cada cluster así como también existe una diferencia significativa en el tiempo en FM.
        """, unsafe_allow_html=True)


    if select_insight =="RECOMENDACIONES":
          
          st.markdown("""
            ## Recomendaciones Estratégicas
            
            ### 1. Establecer KPIs operativos
            Establecer indicadores operativos SMART. Por ejemplo, reducir los cuellos de botella en X fase a X cantidad, o reducir el tiempo promedio en FM en 2s.           

            ### 2. Productividad lograda
            Actualmente, la productividad mensual programada siempre supera a la producción mensual real. Se recomienda realizar una evaluación periódica de los objetivos de producción. Los datos analizados muestran que Ternium ha estado por debajo de la producción programada en los últimos dos años. Es importante ajustar los objetivos con base en la capacidad productiva del Molino Caliente 4 para evitar desmotivación, desviación de prioridades y metas no alcanzadas.

            ### 3. Cuellos de botella en fases de ML4
            Se identificaron cuellos de botella en la fase FM del Molino Caliente 4. Según el socio, se prefiere que los cuellos de botella ocurran en la primera fase del proceso (FCE). A partir del modelo K-means, se obtuvieron dos agrupaciones de datos:

            - **Cluster 0**: Planchones con mayor tiempo en FM, debido a ser más anchos, cortos, pesados y con menor velocidad final en FM.
            - **Cluster 1**: Planchones con menor tiempo en FM, siendo más delgados, largos y menos pesados.

            Se comprobó que cada grupo tiene diferencias significativas en los tiempos de demora y en el tiempo en FM. Se recomienda aplicar la **Teoría de las Restricciones** para identificar y gestionar áreas con menor capacidad, especialmente en términos de maquinaria y recursos humanos.

            **Maquinaria**: Si los planchones más anchos y pesados demoran más, podría ser necesario evaluar la capacidad de la maquinaria para manejar estos casos eficientemente.

            **Recursos Humanos**: Se observa que algunos comentarios sobre demoras e interrupciones están injustificados, lo que puede indicar que el personal operativo no comprende completamente los procesos. Se recomienda proporcionar capacitación continua sobre mejores prácticas operativas.

            ### 4. Mantenimiento predictivo y reactivo
            Actualmente, Ternium tiene una línea de producción automatizada en un 75%, y el mantenimiento es reactivo, respondiendo a incidentes o anomalías. Se recomienda implementar **estrategias de mantenimiento predictivo** para anticipar y mitigar problemas antes de que ocurran, optimizando el tiempo y la eficiencia del proceso.

            ### 5. Planificación de la producción
            Se recomienda generar diversos escenarios de producción basados en la demanda diaria. Cada escenario debería predecir el tiempo en cada fase dentro del molino, ajustando el acomodo de los planchones para optimizar la línea de producción y reducir los cuellos de botella en la fase FM.
            """)
     
#SECCIÓN TABLERO
if selected=="Tablero":
        st.subheader(':red[Visualización del tablero]')
        st.write("En esta sección se encuentra el tablero dinámico de la situación problema. El tablero consta de dos partes esenciales una general y otra más especifica de la fase FM. Además es posible descargar el tablero.")

        with open("Ternium.pbix", "rb") as file:
                 st.download_button(
                     label="Descargar tablero",
                     data=file,
                     file_name="Ternium.pbix",
                     mime="application/octet-stream",
                 )

        st.image("tablero.jpeg", use_column_width=True)
 
#SECCIÓN CONTACTO
if selected == "Nosotros":
     
    st.subheader(':red[Nosotros]')
    st.image("equipo.png", use_column_width=True)
     
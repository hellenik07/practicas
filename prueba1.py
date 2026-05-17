import streamlit as st
import google.generativeai as genai

#Api key y el modelo de gemini que voy a usar
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model= genai.GenerativeModel('gemini-2.5-flash')

#El diseño de la pagina
st.title("Asistente Culinario")
st.write("Escribe que quieres comer y te explicaré datos curiosos de esa comida")

#Entradas del usuario
platillo=st.text_input("Que se te antoja comer?")

#Promp para gemini para que dé los datos curiosos

if st.button("Explicar datos curiosos"):
 
    reglasOcultas="""
 Actúa como chef experto.
 El usuario te dira que quiere comer. Tu objetivo NO es darle la receta.
 debes darle DATOS CURIOSOS sobre la comida,quien lo inventó,en que año surgió,pais de origen,formas de comerlo.
 utiliza un tono amigable.
 La comida de quiere preparar es: """


#aqui se junta lo que ponga el usuario junto con el prompt
    mensajeFinal=reglasOcultas+platillo
 #esta parte manda el mensaje a gemini
    respuestaGemini=model.generate_content(mensajeFinal)
#Esto es lo que se muestra
    st.write(respuestaGemini.text)

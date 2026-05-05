import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Songwriter AI")

# Título y Diseño
st.title("🎼 Songwriter AI Pro")
st.write("Genera letras de canciones al instante.")

# Conexión con la llave
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ Falta configurar la API KEY en Secrets.")

# Entradas
genero = st.text_input("Género Musical", "Cumbia")
tema = st.text_area("¿De qué trata la canción?")

if st.button("Componer Canción ✨"):
    if tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}")
                st.markdown("### 📝 Letra:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Hubo un detalle: {e}")
    else:
        st.warning("Por favor escribe el tema de la canción.")
      

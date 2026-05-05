import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="Songwriter AI", page_icon="🎼")

# Título visual
st.title("🎼 Songwriter AI Pro")
st.write("Genera letras de canciones al instante.")

# Conexión con la llave (Secrets)
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Usamos el modelo más estable
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Error de configuración: {e}")
else:
    st.error("⚠️ Falta la llave en Secrets. Ve a Settings -> Secrets y agrégala.")

# Entradas de texto
genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("¿De qué trata la canción?", placeholder="Ejemplo: Una historia de amor en el campo...")

# Botón principal
if st.button("Componer Canción ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Escribiendo..."):
            try:
                # Petición directa y sencilla
                response = model.generate_content(f"Escribe una canción de {genero} sobre: {tema}. Con estrofas y coro.")
                st.markdown("### 📝 Tu Canción:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"Hubo un detalle: {e}")
                st.info("Si el error persiste, dale a 'Reboot App' en el menú de la derecha.")
    else:
        st.warning("Por favor escribe el tema de la canción.")
        

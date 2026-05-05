import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página
st.set_page_config(page_title="Songwriter AI Pro", page_icon="🎼")

# 2. Conexión con la llave (Secrets)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    # FORZAMOS LA VERSIÓN ESTABLE PARA EVITAR EL ERROR 404
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ Falta la llave en los Secrets de Streamlit.")

# 3. Interfaz de usuario
st.title("🎼 Songwriter AI Pro")
st.write("Crea letras de canciones originales en segundos.")

genero = st.text_input("Género Musical", value="Cumbia")
tema = st.text_area("¿De qué quieres que trate la canción?", placeholder="Ejemplo: El amor entre Alberto y Marissa...")

# 4. Botón de acción
if st.button("Componer Canción ✨", use_container_width=True):
    if tema:
        with st.spinner("🚀 Escribiendo tu éxito..."):
            try:
                # La petición al modelo
                prompt = f"Escribe una canción de {genero} que hable de: {tema}. Que tenga rimas y buen ritmo."
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.markdown("### 📝 Tu Canción:")
                st.write(response.text)
                st.balloons()
            except Exception as e:
                # Si sale el error 404, aquí te dirá cómo arreglarlo
                st.error(f"Hubo un error: {e}")
                st.info("Si el error dice '404', ve a 'Manage app' -> 'Reboot App' para actualizar el servidor.")
    else:
        st.warning("Escribe un tema para poder empezar.")
        

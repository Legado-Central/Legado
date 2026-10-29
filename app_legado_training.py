st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Legado - Control de Asistencia", page_icon="🏋️‍♂️", layout="centered")

# --- BASE DE DATOS INICIAL DE PRUEBA ---
if 'asistencias_gym' not in st.session_state:
    st.session_state.asistencias_gym = pd.DataFrame([
        {"Sede": "Recoleta", "Horario": "07:00 - 08:00 hs", "Alumno": "Sol"},
        {"Sede": "Recoleta", "Horario": "07:00 - 08:00 hs", "Alumno": "Belu"},
        {"Sede": "Recoleta", "Horario": "18:30 - 19:30 hs", "Alumno": "Ruso"},
        {"Sede": "Núñez / Belgrano", "Horario": "08:30 - 09:30 hs", "Alumno": "Carlos Torres"},
        {"Sede": "Núñez / Belgrano", "Horario": "19:30 - 20:30 hs", "Alumno": "Julieta"},
        {"Sede": "Vicente López", "Horario": "08:00 - 09:00 hs", "Alumno": "Lucas Gómez"}
    ])

df = st.session_state.asistencias_gym

# --- INTERFAZ VISUAL ---
st.title("🏋️‍♂️ LEGADO - Panel de Control")
st.subheader("Control de Asistencia por Sedes y Horarios")
st.caption(f"📅 Fecha actual: {datetime.now().strftime('%d/%m/%Y')}")

st.markdown("---")

# 📍 1. Selector de Sede Oficiales de Legado_bsas
st.write("### 📍 1. Seleccione la Sucursal:")
sedes_oficiales = ["Recoleta", "Núñez / Belgrano", "Vicente López"]
sede_sel = st.radio("Elegí una sede para desplegar sus horarios:", sedes_oficiales, horizontal=True)

st.markdown("---")

# ⏱️ 2. Mapeo de Horarios Oficiales
horarios_por_sede = {
    "Recoleta": [
        "07:00 - 08:00 hs", "08:00 - 09:00 hs", 
        "18:30 - 19:30 hs", "19:30 - 20:30 hs", "20:30 - 21:30 hs",
        "09:30 - 11:00 hs (Sáb)"
    ],
    "Núñez / Belgrano": [
        "07:30 - 08:30 hs", "08:30 - 09:30 hs",
        "18:30 - 19:30 hs", "19:30 - 20:30 hs"
    ],
    "Vicente López": [
        "08:00 - 09:00 hs", "09:00 - 10:00 hs",
        "19:00 - 20:00 hs", "20:00 - 21:00 hs"
    ]
}

# Despliegue dinámico de la Sede elegida
st.write(f"### ⏱️ Cronograma y Alumnos: **Sede {sede_sel}**")
horarios_actuales = horarios_por_sede.get(sede_sel, [])

for h in horarios_actuales:
    alumnos_turno = df[(df["Sede"] == sede_sel) & (df["Horario"] == h)]
    total_anotados = len(alumnos_turno)
    
    col1, col2 = st.columns()
    with col1:
        with st.expander(f"⏰ Turno: {h}"):
            if total_anotados > 0:
                st.write("**Lista de atletas anotados para hoy:**")
                for alumno in alumnos_turno["Alumno"]:
                    st.write(f"🏃‍♂️ {alumno}")
            else:
                st.write("No hay alumnos registrados en este horario para el día de hoy.")
    with col2:
        st.metric(label="👥 Total", value=total_anotados    

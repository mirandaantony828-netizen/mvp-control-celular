import streamlit as st

st.set_page_config(
    page_title="Control de Tiempo",
    page_icon="📱"
)

st.title("📱 Control de Tiempo de Estudio")

st.write(
    "Herramienta para ayudar a los estudiantes "
    "a analizar el equilibrio entre el uso del celular "
    "y el tiempo de estudio."
)

st.subheader("Ingresa tus datos")

celular = st.number_input(
    "Horas de celular al día",
    min_value=0.0,
    max_value=24.0,
    value=4.0,
    step=0.5
)

estudio = st.number_input(
    "Horas de estudio al día",
    min_value=0.0,
    max_value=24.0,
    value=2.0,
    step=0.5
)

if st.button("Analizar mi tiempo"):

    if celular > estudio * 2:

        st.warning("⚠️ Uso de celular alto")

        st.write(
            "Tu tiempo de celular es considerablemente "
            "mayor que tu tiempo de estudio."
        )

        st.write(
            "💡 Recomendación: intenta reducir el tiempo "
            "de pantalla y aumentar gradualmente el tiempo de estudio."
        )

    elif estudio >= celular:

        st.success("✅ Buen equilibrio")

        st.write(
            "Tu tiempo de estudio es igual o superior "
            "al tiempo de celular."
        )

        st.write(
            "💡 Recomendación: continúa manteniendo "
            "una buena organización."
        )

    else:

        st.info("💡 Puedes mejorar tu equilibrio")

        st.write(
            "Tu tiempo de celular es mayor que tu tiempo de estudio."
        )

        st.write(
            "Intenta organizar horarios específicos para estudiar "
            "y utilizar el celular."
        )

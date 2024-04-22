import streamlit as st
from  streamlit_option_menu import option_menu
from google_calendar_class import GoogleCalendar
import numpy as np
import datetime as dt
from streamlit_lottie import st_lottie  #Pagina: Lotiefiles.com
import requests
#import '..streamlit/secrets.toml' 
#from send_email import send
#from google_sheets import GoogleSheet

#Funciones
def add_30_minutes(time_str):
    time_format = "%H:%M"
    parsed_time = dt.datetime.strptime(time_str, time_format).time()

    # Convert the time to a datetime object for easier manipulation
    time_datetime = dt.datetime.combine(dt.date.today(), parsed_time)

    # Add 30 minutes to the time
    new_time_datetime = time_datetime + dt.timedelta(minutes=30)
    return new_time_datetime

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#Variables
servicios = ["Inyectables - 15 $","Colocaciones de Suero - 35 $","Curacion de heridas - 25 $", "Control de glucosa - 8 $"]
empleados = ["Rocio","Janeth"]
horas_disponibles = ['10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00']
credentials =  'test-calendar-420116-6df0ced01187.json' #st.secrets["db_credencial"]['credencial_calentar_json']  #'test-calendar-420116-6df0ced01187.json'
calendarid1 = 'diegofiis10@gmail.com'
calendarid2 = '3c286a0e2918ef7053872ef71e0b2892e3c64eaed80255963793e349957f304e@group.calendar.google.com'
timezone = 'America/Lima'
empleado = 'Julian'
document = 'app-citas'
sheet = 'citas'
#html_calendar = """<iframe src="https://calendar.google.com/calendar/embed?src=classtonidev%40gmail.com&ctz=Europe%2FMadrid" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>"""

lottie_url = "https://lottie.host/9142980d-2e79-4348-8048-332aa7083833/8KBBnn9Yc8.json"  #Acceso al formulario de Lottie

#Page config
st.set_page_config(page_title="App Enfermeria", page_icon="👩🏻‍⚕", layout="centered")
#st.image("assets/Portada_2.jpg",use_column_width= True)

lottie = load_lottie(lottie_url)
st_lottie(lottie, height=200)

#prueba 22/04/2024


st.title("Topico de enfermeria a domicilio")
st.text("Jiron intermedio Mz N4 Lt5, SJL")

selected = option_menu(menu_title=None, 
                       options=["Servicios","Reseñas","Portafolio","Detalles"],
                       icons= ["heart-pulse","chat-dots","file-text","pin"], # https://icons.getbootstrap.com/
                       orientation="horizontal",  
                       )

if selected == "Portafolio":
    st.image("assets/Inyectables.png",caption="Inyectables", use_column_width= True)
    st.image("assets/Curacion_heridas.jpeg",caption="Curaciones de heridas",use_column_width= True)
    st.image("assets/Colocacion_sueros.jpg",caption="Colocacion de medicamentos en vía",use_column_width= True)
    st.image("assets/Control_glucosa.jpg",caption="Control de glucosa",use_column_width= True)
    #st.image("assets/corte5.jpg",caption="Corte tupe")

if selected == "Detalles":
    st.image("assets/map.JPG")
    st.markdown(f"Pulsa [aquí](https://www.google.com/maps/search/jiron+mariano+soto+mz+n4+lt5+urbanizacion+mariscal+caceres,+san+juan+de+lurigancho+,+lima+peru/@-11.9497517,-76.9803246,18z/data=!3m1!4b1?entry=ttu) para ver la dirección en Google Maps.")

    st.subheader("Empleados")
    column1, column2 = st.columns(2)
    column1.image("assets/enfermera_1.jpeg",caption="Rocio")
    column2.image("assets/enfermera_1.jpeg",caption="Janeth")

    st.subheader("Horarios de apertura y contacto")
    st.write("---")
    st.text("📞 920 187 327")
    st.write("---")

    c1,c2 = st.columns(2)
    c1.text("Lunes")
    c2.text("10:00 - 19:00")
    c1.text("Martes")
    c2.text("10:00 - 19:00")
    c1.text("Miercoles")
    c2.text("10:00 - 19:00")
    c1.text("Jueves")
    c2.text("10:00 - 19:00")
    c1.text("Viernes")
    c2.text("10:00 - 19:00")
    c1.text("Sabado")
    c2.text("10:00 - 19:00")
    c1.text("Domingo")
    c2.text("Cerrado")

    st.write("---")
    st.markdown("📷  [Instagram](www.instagram.com)")

if selected == "Reseñas":
    st.write("##")
    st.image("assets/atencion_1.jpg")
    #st.image("assets/opinion2.JPG")
    #st.image("assets/opinion3.JPG")
    #st.image("assets/opinion4.JPG")

if selected == "Servicios":

    #st.subheader("Calendario actual")
    #st.markdown(html_calendar,unsafe_allow_html=True)

    st.subheader("Reservar cita")
    a1,a2 = st.columns(2)
    nombre = a1.text_input("Tu nombre*")
    email = a2.text_input("Tu email*")
    fecha = a1.date_input("Fecha")
    if fecha:
        if empleado == 'Julian':
            calendarid = calendarid1
        elif empleado == 'Juan':
            calendarid =  'none' #calendarid2
        calendar = GoogleCalendar(credentials, calendarid) #Se crea el objetio de la clase GoogleCalendar
        hours_blocked = [] #calendar.get_start_times(str(fecha))
        result_hours = np.setdiff1d(horas_disponibles,hours_blocked)
    

    hora = a2.selectbox("Horas disponibles", result_hours)
    servicio = a1.selectbox("Servicio*", servicios)
    empleado = a2.selectbox("Empleado",empleados)
    nota = a1.text_area("💬 Nota (opcional)")

    enviar = st.button("Reservar")

    if enviar:
        if not nombre or not email or not servicio:
            st.warning("Tienes que rellenar todos los campos obligatorios antes de reservar tu cita")
        else:
            with st.spinner('Cargando ...'):
                #create event in google calendar
                precio = servicio.split("-")[1]      
                parsed_time = dt.datetime.strptime(hora, "%H:%M").time()
                hours1 = parsed_time.hour
                minutes1 = parsed_time.minute
                end_hours = add_30_minutes(hora)
                start_time = dt.datetime(fecha.year, fecha.month, fecha.day, hours1+1, minutes1).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
                end_time = dt.datetime(fecha.year, fecha.month, fecha.day, end_hours.hour+1, end_hours.minute).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
                summary = servicio+". "+ nombre
                if empleado == "Julian":
                    calendarid = calendarid1
                elif empleado == "Juan":
                    calendarid = calendarid2

                #crear evento en google calendar
                try:
                    calendar_manager = GoogleCalendar(credentials, calendarid)
                    calendar_manager.create_event(summary,start_time,end_time,timezone)
                except Exception as e:
                    st.warning("Ha habido un error al crear su cita, por favor intentelo más tarde.")

               
    
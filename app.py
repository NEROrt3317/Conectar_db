from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto por una clave segura

# Configuración de la conexión a Neon.tech
DB_HOST = "ep-shiny-bar-a5qygn23.us-east-2.aws.neon.tech"
DB_NAME = "Personas"
DB_USER = "Personas_owner"
DB_PASSWORD = "ebDi1A7glCYo"

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Obtener datos del formulario
    nombre_completo = request.form["nombre_completo"]
    edad = int(request.form["edad"])
    fecha_nacimiento = request.form["fecha_nacimiento"]
    direccion = request.form["direccion"]
    numero_celular = request.form["numero_celular"]
    estado_civil = request.form["estado_civil"]
    nivel_estudio = request.form["nivel_estudio"]
    perfil_laboral = request.form["perfil_laboral"]
    convertido = request.form["convertido"]
    bautizado = request.form["bautizado"]

    # Conexión a la base de datos y ejecución de la consulta
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Personas (
                nombre_completo, edad, fecha_nacimiento, direccion, numero_celular,
                estado_civil, nivel_estudio, perfil_laboral, convertido, bautizado
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre_completo, edad, fecha_nacimiento, direccion, 
                               numero_celular, estado_civil, nivel_estudio, 
                               perfil_laboral, convertido, bautizado))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"Error al guardar en la base de datos: {e}"
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

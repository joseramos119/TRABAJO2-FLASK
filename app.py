# Importar el módulo Flask
from flask import Flask, jsonify,request
from flask_mysqldb import MySQL
from modelo.user import User


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "prueba"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}
mysql = MySQL(app)

# Crear una instancia de la aplicación Flask

# Función de vista para la ruta '/personas'
@app.route('/personas', methods=['GET'])
def get_personas():
    
    # Lista de nombres de personas
    personas = [
        {'nombre': 'Jose'},
        {'nombre': 'Marío'},
        {'nombre': 'ramiro'},
        {'nombre': 'Thiago'},
        {'nombre': 'Luis'},
    ]
    # Convertir la lista en formato JSON
    return jsonify(personas)
@app.route("/usuarios", methods=['GET'])
def mostrar():
 try:    

            cursor = mysql.connection.cursor()
            sql = "SELECT * FROM empleado"
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            return jsonify(data)
 except Exception as error:
        return jsonify({"error": "Ocurrió un error al mostrar los usuarios", "details": str(error)}), 500
@app.route("/insertar_user", methods=['POST'])
def insertar_user():
    try:    
            user_data = request.json
            user = User(**user_data)
            
            cursor = mysql.connection.cursor()

            cursor.execute("INSERT INTO empleado(nombre,apellido,documento,edad,salario) VALUES(%s, %s, %s, %s, %s)",
                       (user.nombre, user.apellido, user.documento, user.edad, user.salario))
            
 
            mysql.connection.commit()
            cursor.close()
            return jsonify({"informacion":"empleado registrado"})
    except Exception as error:
        return jsonify({"error": "Ocurrió un error al registrar el usuario", "details": str(error)}), 500
@app.route("/update/<id>", methods=['PUT'])
def update(id):
    try:    
            user_data = request.json
            user = User(**user_data)
            
            cursor = mysql.connection.cursor()

            cursor.execute("UPDATE empleado SET nombre=%s,apellido=%s,documento=%s,edad=%s,salario=%s WHERE id = %s",
                       (user.nombre, user.apellido, user.documento, user.edad, user.salario,id))
            
 
            mysql.connection.commit()
            cursor.close()
            return jsonify({"informacion":"actualizado correctamente"})
    except Exception as error:
        return jsonify({"error": "Ocurrió un error al update el usuario", "details": str(error)}), 500
@app.route("/delete/<id>", methods=['DELETE'])
def delete(id):
 try:    
       
            cursor = mysql.connection.cursor()
            
            cursor.execute("DELETE FROM empleado WHERE id = %s",(id,))
            cursor.close()
            mysql.connection.commit()
            #print (data)
            return jsonify({"informacion":"eliminado correctamente"})
 except Exception as error:
        return jsonify({"error": "Ocurrió un error al eliminar los usuarios", "details": str(error)}), 500  

if __name__ == '__main__':
    app.run(debug=True)
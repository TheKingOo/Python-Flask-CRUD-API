from flask import Flask , request , jsonify
import json
import pymysql


app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host="your_mysql_host",
    			       	user="your_mysql_username",
                               	password="your_mysql_password",
                               	database="your_database_name",
                               	charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    except pymysql.error as e :
        print(e)
    return conn


@app.route('/Auto' , methods=['GET' , 'POST'])
def all_auto():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM autos")
        allAuto = [
            dict(id_auto =row['id_auto'],id_parking=row['id_parking'] ,
                 matricule = row['matricule'])
                 for row in cursor.fetchall()
        ]
        if allAuto is not None :
            return jsonify(allAuto)

    
    if request.method == 'POST':
        new_id_parking = int(request.form["id_parking"])
        new_matricule = request.form["matricule"]
        sql = """ INSERT INTO autos (id_parking , matricule)
                    VALUES(%s,%s)"""

        cursor = cursor.execute(sql,(new_id_parking, new_matricule))
        conn.commit()
        return "created successfully",201


@app.route('/Auto/<int:id>',methods=['GET','PUT','DELETE'])
def single_auto(id):
    conn = db_connection()
    cursor = conn.cursor()
    auto=None

    if request.method == "GET":
        cursor.execute("SELECT * FROM autos WHERE id_auto=%s",(id,))
        rows = cursor.fetchall()
        for r in rows :
            auto = r
        if auto is not None :
                return jsonify(auto),200
        else:
            return "Something wrong",404
            
    if request.method == 'PUT':
        sql = """UPDATE autos SET id_parking=%s,
                                matricule=%s,
                                WHERE id_auto=%s"""
        
        id_parking=request.form['id_parking']
        matricule = request.form['matricule']

        updated_auto = {
                "id_auto":id,
                "id_parking":id_parking,
                "marticule":matricule,
        }
        cursor = cursor.execute(sql,(id_parking ,matricule,id))
        conn.commit()
        return jsonify(updated_auto)
    

    if request.method =='DELETE':
        sql ="""DELETE FROM autos WHERE id_auto=%s"""
        cursor = cursor.execute(sql,(id,))
        conn.commit()
        return "The auto with id:{} has been deleted.".format(id),200
    



if __name__ == '__main__' :
    app.run(debug=True)

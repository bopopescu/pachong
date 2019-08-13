#coding:utf-8
from flask import Flask,request,render_template
import mysql.connector
import json
import time
import datetime




app = Flask(__name__)

conn = mysql.connector.connect(host='183.66.213.82',port="8803",user= 'tylin',password ='Tylin@123',database ='shenzhen_event',auth_plugin='mysql_native_password') #连接数据库，创建Flask_app数据库
cursor = conn.cursor()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/show")
def show():
    return app.send_static_file('show.html')

@app.route('/event/table')
def table():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,'department': department,"contector":contector}

        list.append(dict)

    return json.dumps(list)

@app.route("/event/table/insert" ,methods=["POST"])
def insert():
    data = request.get_json()

    event_name = data['event_name']
    start_plan = data["start_plan"]
    plan_time = data["plan_time"]
    finish_time = data["finish_time"]
    dpi = data["dpi"]

    if finish_time == "":
        finish_time = 'Null'

    if finish_time == 'Null':

        sql = "INSERT INTO event (event_name,start_plan ,plan_time, finish_time, dpi) VALUES ('%s','%s','%s',%s,%d)"% (event_name,start_plan,plan_time,finish_time,dpi)

    else:

        sql = "INSERT INTO event (event_name, start_plan,plan_time, finish_time, dpi) VALUES ('%s','%s','%s','%s',%d)" % (event_name,start_plan ,plan_time, finish_time, dpi)


    cursor.execute(sql)
    conn.commit()

    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        list.append(dict)

    return json.dumps(list)

@app.route("/event/table/cancel" ,methods=["POST"])
def cancel():
    data = request.get_json()
    id = data["id"]

    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    cancel = "UPDATE event SET finish_time =" + "'"+current_time+"'" + "where id=" + "'" +id+ "'"
    cursor.execute(cancel)
    conn.commit()

    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        list.append(dict)

    return json.dumps(list)


@app.route("/event/table/delete" ,methods=["POST"])
def delete():
    data = request.get_json()
    id = data["id"]

    delete = "DELETE FROM event WHERE id=" + "'" +id+ "'"
    cursor.execute(delete)
    conn.commit()

    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        list.append(dict)

    return json.dumps(list)


@app.route("/event/table/change" ,methods=["POST"])
def change():


    data = request.get_json()
    id = data["id"]
    start_plan = data["start_plan"]
    event_name = data['event_name']
    plan_time = data["plan_time"]
    dpi = data["dpi"]


    change = "UPDATE event SET event_name ='%s',start_plan ='%s',plan_time ='%s',dpi ='%s'where id='%s'"%(event_name,start_plan,plan_time,dpi,id)
    cursor.execute(change)
    conn.commit()




    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        list.append(dict)

    return json.dumps(list)


@app.route('/event/table/late')
def late():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        if state > 0 and state < 999999:
            list.append(dict)

    print(table)
    print(list)
    return json.dumps(list)


@app.route('/event/table/near')
def near():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        if state < 1 and state > -4:
            list.append(dict)


    return json.dumps(list)

@app.route('/event/table/complete')
def complete():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        if state == 999999:
            list.append(dict)

    return json.dumps(list)

@app.route('/event/table/in_plan')
def in_plan():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        if state <-3:
            list.append(dict)

    return json.dumps(list)

@app.route('/event/table/count')
def count():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list_late = []
    list_complete = []
    list_near = []
    list_in_plan = []

    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        dict = {"id": id, 'event_name': event_name, 'start_plan':start_plan ,'plan_time': plan_time, 'finish_time': finish_time, 'state': state,
                'department': department,"contector":contector}

        if state == 999999:
            list_complete.append(dict)

        if state>0 and state <999999:
            list_late.append(dict)

        if state<1 and state>-4:
            list_near.append(dict)

        if state<-3:
            list_in_plan.append((dict))

        count_dict = {"late":len(list_late),"near":len(list_near),"in_plan":len(list_in_plan),"complete":len(list_complete)}

        count_list =[]

        count_list.append(count_dict)

    return json.dumps(count_list)

@app.route('/event/table/date')
def date():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')

    return current_time

@app.route('/table/email_late')
def email_late():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name,email from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list_late = []


    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        email = i[7]

        dict = {"id": id, 'event_name': event_name, 'start_plan': start_plan, 'plan_time': plan_time,
                'finish_time': finish_time, 'state': state,
                'department': department, "contector": contector,"email":email}


        if state > 0 and state < 999999:
            list_late.append(dict)

        a_list = []

        for info in list_late:
            a = [info["event_name"],info["email"],info["department"]]
            a_list.append(a)




    return json.dumps(a_list)


@app.route('/table/email_near')
def email_near():
    table = "SELECT event.id,event_name, start_plan ,plan_time, finish_time, department,name,email from event JOIN person ON event.dpi=person.id"

    cursor.execute(table)

    result = cursor.fetchall()

    list_late = []


    for i in result:

        id = i[0]
        event_name = i[1]
        start_plan = i[2].strftime('%Y-%m-%d')
        plan_time = i[3].strftime('%Y-%m-%d')
        finish_time = i[4]

        localtime = time.strftime("%Y-%m-%d", time.localtime())

        plan_time_trans = time.mktime(time.strptime(plan_time, "%Y-%m-%d"))
        localtime_trans = time.mktime(time.strptime(localtime, "%Y-%m-%d"))

        time_dis = localtime_trans - plan_time_trans

        state = int(time_dis) / 86400

        if finish_time == None:
            finish_time = i[4]

        else:
            finish_time = i[4].strftime('%Y-%m-%d')
            state = 999999

        department = i[5]
        contector = i[6]
        if contector == "":
            contector = "无"

        email = i[7]

        dict = {"id": id, 'event_name': event_name, 'start_plan': start_plan, 'plan_time': plan_time,
                'finish_time': finish_time, 'state': state,
                'department': department, "contector": contector,"email":email}


        if state <1 and state > -4:
            list_late.append(dict)

        a_list = []

        for info in list_late:
            a = [info["event_name"],info["email"],info["department"]]
            a_list.append(a)




    return json.dumps(a_list)



application = app
if __name__ == '__main__':
    app.run(port=5000, debug=True)

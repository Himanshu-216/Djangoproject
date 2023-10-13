from django.shortcuts import render
from django.http import request, HttpResponse
import mysql.connector as sql
# Create your views here.


fname, lname, g, em, pswd = '', '', '', '', ''


# Create your views here.
def signup_action(request):
    global fname, lname, g, em, pswd
    if request.method == 'POST':
        dbase = sql.connect(host="localhost", user="root", passwd="Him@nshu1234", database = "website")
        cursor = dbase.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fname = value
            if key == "last_name":
                lname = value
            if key == "sex":
                g = value
            if key == "email":
                em = value
            if key == "password":
                pswd = value
        c = "insert into users values('{}', '{}', '{}', '{}', '{}')".format(fname, lname, g, em, pswd)
        cursor.execute(c)
        dbase.commit()
    return render(request, 'signup_page.html')
from django.shortcuts import render
from django.http import request, HttpResponse
import mysql.connector as sql
# Create your views here.
emel = ''
pswrd = ''

def login_action(request):
    global emel, pswrd
    if request.method == 'POST':
        dbase = sql.connect(host="localhost", user = "root", passwd = "Him@nshu1234", database= "website")
        cursor = dbase.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                emel = value
            if key == "password":
                pswrd = value
        command = "select * from users where email = '{}' and password = '{}'".format(emel, pswrd)
        cursor.execute(command)
        t = tuple(cursor.fetchall())
        print(t)
        if t == ():
            return render(request, 'error.html')
        else :
            return render(request, 'welcome.html')
    return render(request, 'login_page.html')




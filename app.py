from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET','POST'])
def dropdown():
    error = None
    cars = ['vehicle.dodge.charger_police', 'vehicle.chevrolet.impala', 'vehicle.mini.cooper_s', 'vehicle.toyota.prius']
    if request.method == 'GET':
        return render_template('test.html', cars=cars)
    car = request.form.get('cars')
    print(car)
#os.system("start cmd /K python PythonAPI/examples/automatic_control.py --car " + '"' + car + '"')
    return redirect("https://account.mongodb.com/account/login", code=302)





if __name__ == "__main__":
    app.run()

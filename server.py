from flask import Flask,render_template, request,url_for,redirect
import csv 

app = Flask(__name__)



@app.route('/')
def my_home(): 
    
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name): 
    
    return render_template(page_name)



def write_to_file(data):
    with open("database.txt",mode="a") as database:
        name = data["Name"]

        email = data["Email"]
        message = data["Message"]
        file = database.write(f"\n{name},{email},{message}")


def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        name = data["Name"]

        email = data["Email"]
        message = data["Message"]
        csv_writer =  csv.writer(database2,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data = data)
        return redirect("about.html")
    else:
        return "somethin went wrong again "
    



# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/elements.html")
# def elem():
#     return render_template("elements.html")


# @app.route("/generic.html")
# def gene():
#     return render_template("generic.html")



# # @app.route("/favicon.ico")
# # def blog():
# #     return "there are ny thoughts on blogs"

# @app.route("/blog")
# def blog():
#     return "these are a blog site for test"

# @app.route("/blog1")
# def blog1():
#     return "these 2020 dogs test"
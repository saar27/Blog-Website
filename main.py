from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

my_email = "saar79656@gmail.com" 
my_password = "onri mwlv oytm zvrw"

response = requests.get("https://api.npoint.io/410e0761dcb0c918a394")
posts = response.json()

@app.route('/')
def home():
    return render_template("index.html",all_posts= posts)

@app.route('/index.html')
def home2():
    return render_template("index.html", all_posts= posts)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html',methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        is_on = True
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= my_email, password= my_password)
            connection.sendmail(from_addr= my_email, to_addrs= "saar1324@hotmail.com", msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template("contact.html",name= is_on)
    return render_template("contact.html")
    

@app.route('/post.html/<int:index>')
def post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post    
    return render_template("post.html", post= requested_post)








if __name__ == "__main__":
    app.run(debug= True)
    
    
    


    
#<li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="post.html">Sample Post</a></li>


# </div>
#                     <!-- Divider-->
#                     <hr class="my-4" />
#                     <!-- Post preview-->
#                     <div class="post-preview">
#                         <a href="post.html">
#                             <h2 class="post-title">Failure is not an option</h2>
#                             <h3 class="post-subtitle">Many say exploration is part of our destiny, but it’s actually our duty to future generations.</h3>
#                         </a>
#                         <p class="post-meta">
#                             Posted by
#                             <a href="#!">Start Bootstrap</a>
#                             on July 8, 2023
#                         </p>
#                     </div>    
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def pet_main() :
   result=0
   resp = request.form
   a="dog1"
   b="dog2"
   c="dog3"
   x=resp.get("enter dog")

   if a==x:
       result="husky price:15k"
       return render_template("output1.html",resp=result)
   elif b==x:
       result="german shepherd price:20k"
       return render_template("output2.html",resp=result)
   elif c==x:
       result="pamorelin price:25k"

       return render_template("output3.html",resp=result)
   else:
       return render_template("input.html")


if __name__ == '__main__':
    app.run(debug=True)
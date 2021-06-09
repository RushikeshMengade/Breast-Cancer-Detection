from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)
model=pickle.load(open("Breastcancer.pkl","rb"))

@app.route("/")

def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET","POST"])
def predict():
    
    if request.method == "POST":
        mean_radius=request.form["Mean_Radius"]
        mean_texture =request.form['Mean_Texture']
        mean_perimeter =request.form['Mean_Perimeter']
        mean_area=request.form['Mean_Area']
        mean_smoothness=request.form['Mean_Smoothness']
        mean_compactness=request.form['Mean_Compactness']
        mean_concavity=request.form['Mean_Concavity']
        mean_concave_points=request.form['Mean_Concave_Points']
        mean_symmetry=request.form['Mean_Symmetry']
        mean_fractal_dimension=request.form['Mean_Fractal_Dimension']
        radius_error=request.form['Radius_Error']
        texture_error=request.form['Texture_Error']
        perimeter_error=request.form['Perimeter_Error']
        area_error=request.form['Area_Error']
        smoothness_error=request.form['Smoothness_Error']
        compactness_error=request.form['Compactness_Error']
        concavity_error=request.form['Concavity_Error']
        concave_points_error=request.form['Concave_Points_Error']
        symmetry_error=request.form['Symmetry_Error']
        fractal_dimension_error=request.form['Fractal_Dimension_Error']
        worst_radius=request.form['Worst_Radius']
        worst_texture=request.form['Worst_Texture']
        worst_perimeter=request.form['Worst_Perimeter']
        worst_area=request.form['Worst_Area']
        worst_smoothness=request.form['Worst_Smoothness']
        worst_compactness=request.form['Worst_Compactness']
        worst_concavity=request.form['Worst_Concavity']
        worst_concave_points=request.form['Worst_Concave_Points']
        worst_symmetry=request.form['Worst_Symmetry']
        worst_fractal_dimenssion=request.form['Worst_Fractal_Dimension']
        
        prediction=model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
                          mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,
                          radius_error,texture_error,perimeter_error,area_error,smoothness_error,
                          compactness_error,concavity_error,concave_points_error,symmetry_error,
                          fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,
                          worst_area,worst_smoothness,worst_compactness,worst_concavity,
                          worst_concave_points,worst_symmetry,worst_fractal_dimenssion]])
        
        
        
            
        
        output=round(prediction[0])
        
        if output==0:
            return render_template('index.html',prediction_text="patient has cancer(malignat tumer){}".format(output))
        else:
            return render_template('index.html',prediction_text="patient has no cancer(malignat benigh){}".format(output))
            


    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)

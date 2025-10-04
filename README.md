# Ex.05 Design a Website for Server Side Processing
# Date:04-10-2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">  
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>Power of Lamp Bulb</title>  
<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">
body {
    background-color: rgb(234, 255, 0);
    font-family: Arial, sans-serif;
}

.edge {
    width: 1440px;
    margin-left: auto;
    margin-right: auto;
    padding-top: 250px;
    padding-left: 300px;
}

.box {
    display: block;
    border: thick dashed rgb(0, 170, 255);
    width: 500px;
    min-height: 300px;
    font-size: 20px;
    background-color: rgb(128, 128, 128);
    padding: 20px;
    box-sizing: border-box;
}

.formelt {
    color: rgb(0, 0, 0);
    text-align: center;
    margin-top: 7px;
    margin-bottom: 6px;
}

h1 {
    color: rgb(255, 0, 17);
    text-align: center;
    padding-top: 20px;
}
</style>
</head>
<body>
<div class="edge">
    <div class="box">
        <h1>Power of Lamp Bulb</h1>
        <form method="POST">
            {% csrf_token %}
            <div class="formelt">
                <label>Intensity: <input type="text" name="Intensity" value="{{I}}"></label> <br/>
            </div>
            <div class="formelt">
                <label>Resistance: <input type="text" name="Resistance" value="{{R}}"></label> (in Ω)<br/>
            </div>
            <div class="formelt">
                <input type="submit" value="Calculate"><br/>
            </div>
 <div class="formelt">
                <label>Power: <input type="text" name="power" value="{{power}}" readonly></label> watts<br/>
            </div>
        </form>
    </div>
</div>
</body>
</html>

views.py

from django.shortcuts import render

def power(request):
    context = {'power': "0", 'i': "0", 'r': "0"}  # default values

    if request.method == 'POST':
        try:
            # Must match input names from your HTML form (Intensity, Resistance)
            i = float(request.POST.get('Intensity', '0'))
            r = float(request.POST.get('Resistance', '0'))

            # Formula: P = I² * R
            p = (i ** 2) * r

            # Store in context for template
            context['power'] = p
            context['i'] = i
            context['r'] = r

            print("POST method is used")
            print("Intensity =", i)
            print("Resistance =", r)
            print("Power =", p)

        except ValueError:
            context['power'] = "Invalid input"

    return render(request, 'mathapp/math.html', context)

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns =[
    path('admin/',admin.site.urls),
    path('power/',views.power,name="power"),
    path('',views.power,name="home")
]
```
# SERVER SIDE PROCESSING:
# HOMEPAGE:
![alt text](<Screenshot 2025-10-04 211145.png>)
# RESULT:
![alt text](<Screenshot 2025-10-04 211236.png>)
![alt text](<Screenshot 2025-10-04 211256.png>)

The program for performing server side processing is completed successfully.

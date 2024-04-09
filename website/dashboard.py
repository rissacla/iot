from flask import Blueprint, render_template, request, redirect, url_for, session

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def dashboard():
    plants = [
        {
            "title": "Anthie",
            "image": "plant1.jpg",
            "species": "Anthurium Magnificum", 
            "health": "Good", 
            "soil": "Aroid Soil Mix", 
            "moisture": "Good", 
            "humidity": "Good", 
            "temperature": "20°C",
            "immediate": "NA",
            "light": "Indirect Bright Exposure",
            "lastWater": "2",
            "lastFertilized": "50",
            "feedback": [
                "Consider repotting in spring.",
                "Looks healthy!"
            ]
        },

        {
            "title": "To-ma-to", 
            "image": "plant2.jpg", 
            "species": "Tomato", 
            "health": "Fair", 
            "soil": "50% Sphagnum, 50% Perlite", 
            "moisture": "Low", 
            "humidity": "Good", 
            "temperature": "23°C",
            "immediate": "Water plant as soon as possible",
            "light": "Direct Exposure",
            "lastWater": "10",
            "lastFertilized": "47",
            "feedback": [
                "Water plant once a week.",
                "Fertilize plant once every 40-60 days.",
                "Try using eggshells once every 12 days for optimal growth rate."
            ]
        },

        {
            "title": "Tom", 
            "image": "plant2.jpg", 
            "species": "Tomato", 
            "health": "Good", 
            "soil": "Aroid Soil Mix", 
            "moisture": "Good", 
            "humidity": "Good", 
            "temperature": "20°C", 
            "immediate": "NA",
            "light": "Direct Exposure",
            "lastWater": "7",
            "lastFertilized": "20",
            "feedback": [
                "Try using eggshells once every 12 days for optimal growth rate."
            ]
        },
    ]


    if "header" in session:
        session.pop("header", None)

    return render_template("dashboard/dashboard.html", plants=plants)

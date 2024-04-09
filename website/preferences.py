from flask import Blueprint, render_template, request, redirect, url_for, session

preferences_bp = Blueprint("preferences", __name__, url_prefix="/preferences")

@preferences_bp.route("/")
def preferences():

    if "header" in session:
        session.pop("header", None)

    return render_template("preferences/preferences.html")

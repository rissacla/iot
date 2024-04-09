from flask import Blueprint, render_template, request, redirect, url_for, session

settings_bp = Blueprint("preferences", __name__, url_prefix="/preferences")

@settings_bp.route("/")
def settings():

    if "header" in session:
        session.pop("header", None)

    return render_template("preferences/preferences.html")

from flask import Blueprint, render_template, request, redirect, url_for, session

settings_bp = Blueprint("settings", __name__, url_prefix="/settings")

@settings_bp.route("/")
def settings():

    if "header" in session:
        session.pop("header", None)

    return render_template("settings/settings.html")

from flask import Blueprint, render_template, session, request

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def dashboard():
    if "header" in session:
        session.pop("header", None)
    return render_template("dashboard/dashboard.html")

@dashboard_bp.route("/update_item", methods=['POST'])
def update_item():
    item = request.form['item']
    session['selected_item'] = item  # Update selected item in session
    return item

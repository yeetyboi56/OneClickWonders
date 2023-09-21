from urllib.parse import quote

import requests
import os

from flask import Blueprint, render_template

from app.forms import PlannerForm
from app.login_required import login_required

planner_route = Blueprint("planner", __name__)


def render_planner_page(form, route=None, error=None) -> str:
    return render_template(
        "planner.html",
        title="Route Planner",
        form=form,
        form_name="planner",
        form_title="Route Planner",
        form_fields=[form.start, form.end],
        field_submit=form.submit,
        route=route,
        error=error
    )


@planner_route.route("/planner/", methods=["GET", "POST"])
@login_required
def planner():
    form = PlannerForm()

    if form.validate_on_submit():
        start = quote(form.start.data, safe="")
        end = quote(form.end.data, safe="")

        response = requests.get(f"https://www.mapquestapi.com/directions/v2/route?key={os.environ['MAPQUEST_API_KEY']}&from={start}&to={end}")

        data = response.json()

        if data.get("info") and data.get("info").get("statuscode") == 0:
            route: dict = data.get("route")

            legs = sorted(route.get("legs"), key=lambda d: d.get("index"))

            maneuvers = sorted(legs[0].get("maneuvers"), key=lambda d: d.get("index"))

            narratives = [maneuver.get("narrative") for maneuver in maneuvers]

            return render_planner_page(form, route=narratives)
        else:
            return render_planner_page(form, error="Unable to find route")

    return render_planner_page(form)

from flask import render_template, Blueprint
from sqlalchemy import func
from map_package.models import Zone, Trip, Commodity

map_bp = Blueprint('map', __name__)

@map_bp.route("/", methods=['GET','POST'])
def index():
    key="62ErzPFwmXOe1DFW2P1y"

    
    selected_zone = Zone.query.filter_by(FAF_Zone=363).first()

    
    imports = Trip.query.join(Commodity).with_entities(Commodity.Description, func.count(func.distinct(Trip.dms_orig))).filter(Trip.dms_dest==363).group_by(Commodity.Description)

    

    return render_template('index.html',key=key, selected_zone=selected_zone,imports=imports)
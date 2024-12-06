from geoalchemy2.types import Geometry
from map_package import db


class Zone(db.Model):
    __tablename__ = 'zones_points'

    FAF_Zone = db.Column(db.Integer, primary_key=True)
    FAF_Zone_D = db.Column(db.String)
    centroids = db.Column(Geometry(geometry_type='POINT', srid=5070))
    imports = db.relationship('Trip', foreign_keys="Trip.dms_dest",lazy=True)
    exports = db.relationship('Trip', foreign_keys="Trip.dms_orig",lazy=True)
    

    def __repr__(self):
        return f"{self.FAF_Zone_D}"
    
class Commodity(db.Model):
    __tablename__ = 'comms'
    
    id = db.Column(db.Integer, primary_key=True)
    Description = db.Column(db.String)
    trips = db.relationship('Trip', foreign_keys="Trip.sctg2", lazy=True)

    def __repr__(self):
        return f"{self.Description}"



class Trip(db.Model):
    __tablename__ = 'trips'

    index = db.Column(db.Integer, primary_key=True)
    fr_orig = db.Column(db.Float)
    dms_orig = db.mapped_column(db.Integer, db.ForeignKey('zones_points.FAF_Zone'))
    dms_dest = db.mapped_column(db.Integer, db.ForeignKey('zones_points.FAF_Zone'))
    fr_dest = db.Column(db.Float)
    fr_inmode = db.Column(db.Float)
    dms_mode= db.Column(db.Integer)
    fr_outmode= db.Column(db.Float)
    sctg2 = db.mapped_column(db.Integer, db.ForeignKey('comms.id'))
    trade_type= db.Column(db.Integer)
    dist_band = db.Column(db.Integer)
    tons_2018= db.Column(db.Float)
    tons_2019 = db.Column(db.Float)
    tons_2020 = db.Column(db.Float)
    tons_2021 = db.Column(db.Float)
    tons_2022= db.Column(db.Float)
    tons_2023= db.Column(db.Float)
    value_2018= db.Column(db.Float)
    value_2019 = db.Column(db.Float)
    value_2020 = db.Column(db.Float)
    value_2021 = db.Column(db.Float)
    value_2022= db.Column(db.Float)
    value_2023 = db.Column(db.Float)
    current_value_2018 = db.Column(db.Float)
    current_value_2019= db.Column(db.Float)
    current_value_2020= db.Column(db.Float)
    current_value_2021= db.Column(db.Float)
    current_value_2022= db.Column(db.Float)
    current_value_2023 = db.Column(db.Float)
    tmiles_2018= db.Column(db.Float)
    tmiles_2019 = db.Column(db.Float)
    tmiles_2020= db.Column(db.Float)
    tmiles_2021 = db.Column(db.Float)
    tmiles_2022 = db.Column(db.Float)
    tmiles_2023= db.Column(db.Float)

    def __repr__(self):
        return f"Transporting {self.sctg2} from {self.dms_orig} to {self.dms_dest} by {self.dms_mode}"
from application import application, db
from flask import render_template
from util.utils import *

@application.errorhandler(404)
def not_found_error(error):
    return render_template('errors/page_404.html'), 404

@application.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/page_500.html'), 500

@application.errorhandler(504)
def internal_error(error):
    # db.session.rollback()
    return render_template('errors/page_504.html'), 500

from flask import Flask, jsonify
from flask_restful import Api

from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from app.db import db
from app.loans.api.resources import loans_v1_0_blueprint, api
from .ext import marsh, migrate


def create_app(settings_module):
    app = Flask(__name__)
    app.app_context().push()
    app.config.from_object(settings_module)
    db.init_app(app)
    marsh.init_app(app)
    migrate.init_app(app, db)

    api.init_app(app)
    # Api(app, catch_all_404s=True)
    app.url_map.strict_slashes = False

    app.register_blueprint(loans_v1_0_blueprint)

    register_error_handlers(app)

    return app

def register_error_handlers(app: Flask):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'})

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden Error'}), 403

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': 'Object not found'}), 404

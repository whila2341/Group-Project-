from fastapi import FastAPI
from . import orders, order_items, payment, order_tracking, data_analysis, system_documentation


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_items.router)
    app.include_router(order_tracking.router)
    app.include_router(payment.router)
    app.include_router(data_analysis.router)
    app.include_router(system_documentation.router)

from . import orders, order_items, order_tracking


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_items.router)
    app.include_router(order_tracking.router)

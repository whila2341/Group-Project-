from . import orders, order_details, recipes, sandwiches, resources, promo_codes, payment, data_analysis, System_doc

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    promo_codes.Base.metadata.create_all(engine)
    data_analysis.Base.metadata.create_all(engine)
    System_doc.Base.metadata.create_all(engine)

import pandas as pd
from config import Config

input_file = Config.INPUT_BASE_DIR + \
             "order_items" + \
             Config.INPUT_FILE_NAME

order_items = pd.\
    read_csv(input_file,
             names=["order_item_id", "order_item_order_id",
                    "order_item_product_id", "order_item_quantity",
                    "order_item_subtotal", "order_item_product_price"
                    ])
order_revenue = order_items. \
    groupby("order_item_order_id")["order_item_subtotal"]. \
    agg(revenue=sum).round(2)

output_file = Config.OUTPUT_BASE_DIR + \
    "/order_revenue"

order_revenue.to_csv(output_file, header=None)


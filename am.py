
# import required libs
import pandas as pd
import datatime as dt

# Defined Functions
def next_action(brand):
    """
    The purpose of this function is to assign a next action
    based on the brand that the customer purchased.
    """

    if brand == 'ABC':
        return 'Call Customer'
    elif brand == 'Brand2':
        return 'Ship Directly with Purolator'
    elif brand =='DT':
        return 'Ship Directly with FedEx'
    

def delivery_date(x):
    """
    The purpose of this function is to fill in
    the delivery date.    
    """

    x = pd.to_datetime(x)
    if x.day_name() in ['Saturday','Sunday']:
        return x + pd.offsets.BDay(1)
    else:
        return x + pd.offsets.BDay(2)

# Maintainable mapping
route_map = {'Call Customer':'Personalized Delivery', 'Ship Directly with Purolator':'Purolator_123','Ship Directly with FedEx':'FedEx_Express'}

# import source data from files
am = pd.read_csv ('account_managers.csv')
co = pd.read_csv ('customer_orders.csv')

# clean up date column
co['order_date'] = pd.to_datetime(co['order_date'])

# Aligning each account manager to the correct product group
co.drop('account_manager', axis=1, inplace=True)
co = pd.merge(left = am, right=co, left_on='brand', right_on='brand',  how='inner')

# Determine the next action, using next_action() function
co['next_action'] = co['brand'].apply(next_action)

# Determine delivery date
co['delivery_date'] = co['order_date'].apply(delivery_date)

# Determine delivery route
co['delivery_route'] = co['next_action'].map(route_map)

# output file
co.to_csv('/Users/delinaivanova/Downloads/final_order_routing.csv')







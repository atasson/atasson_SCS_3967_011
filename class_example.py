import pandas as pd

class DeliveryProcessor:

    """
    The purpose of this class is to consistently process delivery data
    across all Canadian stores receiving orders

    The business logic it covers is:
    - delivery dates
    - delivery routes
    - next action
    """

    # defining attributes that exist
    def __init__(self, account_managers_path, orders_path):
        self.am = pd.read_csv(account_managers_path)
        self.co = pd.read_csv(orders_path)

    # define the methods / functions
    def next_action(self, brand):
    
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

    def delivery_date(self, x):
        
        """
        The purpose of the function is to calculate the shipping date
        If the order is placed Sat/Sun, ships next business day, otherwise
        within 2 business days
        """

        x = pd.to_datetime(x)
        if x.day_name() in ['Saturday','Sunday']:
            return x + pd.offsets.BDay(1)
        else:
            return x + pd.offsets.BDay(2)
        
    def route_map(self, x):
        if x == 'Call Customer':
            return 'Personalized Delivery'
        elif x == 'Ship Directly with Purolator':
            return 'Purolator_123' 
        elif x == 'Ship Directly with FedEx':
            return 'FedEx_Express'

    # define the process
    def process(self):
        # Cleanup
        self.co['order_date'] = pd.to_datetime(self.co['order_date'])
        self.co.drop('account_manager', axis=1, inplace=True)
        self.co = pd.merge(left = self.am, right=self.co, left_on='brand', right_on='brand', how='inner')

        # Business logic
        self.co['next_action'] = self.co['brand'].apply(self.next_action)
        self.co['delivery_date'] = self.co['order_date'].apply(self.delivery_date)
        self.co['delivery_route'] = self.co['next_action'].apply(self.route_map)

        return self.co

    # define an export function

    def export(self, output_path):
        self.co.to_csv(output_path, index=False)

processor = DeliveryProcessor('account_managers.csv',
                              'customer_orders.csv')

final_df = processor.process()

processor.export('final_order_routing_v2.csv')
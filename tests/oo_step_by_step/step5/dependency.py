class DeliveryService:
    def delivery(self, product):
        pass


class DeliveryBoy(DeliveryService):
    def delivery(self, product):
        pass


class DeliveryCompany:

    def __init__(self, service):
        self.delivery_service = service

    def delivery(self, product):
        self.delivery_service.delivery(product)

from kivy.uix.screenmanager import Screen

class PaymentScreen(Screen):
    def make_payment(self):
        from_user = self.ids.from_user_field.text
        to_user = self.ids.to_user_field.text
        amount = float(self.ids.amount_field.text)
        # Aqui você deve implementar a lógica de pagamento entre usuários
        self.ids.message.text = f"Payment of {amount} made from {from_user} to {to_user}"

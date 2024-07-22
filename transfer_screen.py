from kivy.uix.screenmanager import Screen

class TransferScreen(Screen):
    def transfer_funds(self):
        from_user = self.ids.from_user_field.text
        to_user = self.ids.to_user_field.text
        amount = float(self.ids.amount_field.text)
        # Aqui você deve implementar a lógica de transferência de fundos entre usuários
        self.ids.message.text = f"Transferred {amount} from {from_user} to {to_user}"
v
from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    name =  self.name.text
    email = self.email.text
    alert('submitted')

    anvil.server.call('add_register', name, email)

    self.clear_all()
  def clear_all(self):
   self.name.text=''
   self.email.text=''

  def name_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass

  def student_name_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

  def student_email_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass



   
   


  
    


from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Get_Recipes_click(self, **event_args):
    self.output.content,val = anvil.server.call('fetch_recipes',
                                     self.Required_Ingredients.text,
                                     self.Prohibited_Ingredients.text)
    if val:
      self.output.visible = True
    else:
      self.output.content = "No results"
      
    


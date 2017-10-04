Gender-AI
---------

Uses a neural network based method to predict the gender of a person from the first name. The network weights are included in the module. No external dependencies, except numpy. Weights are stored inline to make this a single file module.

Usage::
  >>> import gender_ai as g
  >>> g.predict ('Sheldon')

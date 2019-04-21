## All machine learning models

### Create a new model

In order to create a new model, create a new file in src/models.  
Your new model should derive from the AbstractModel from the answers.py file, 
and implement the two methods : 
- get_model(self)
- evaluate_model(self, data_test)

```python
from src.answers import AbstractModel

class NewModel(AbstractModel):

    def get_model(self):
        pass

    def evaluate_model(self, data_test):
        pass
```

Once the model is created, the user should add this model in the **tests/test_model_validity.py** test 
class for it to be tracked by travis. 
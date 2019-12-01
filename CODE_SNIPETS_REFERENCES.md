## PyModM and Marshamallow
```python
import warnings
from pymodm import MongoModel, fields as mongofields
from marshmallow import Schema, fields


class A(MongoModel):
    name = mongofields.CharField()


class ASchema(Schema):
    name = fields.Str()


if __name__ == "__main__":
    warnings.simplefilter("always")
    a = A(name="asd")
    print(ASchema().dumps(a))
```
https://pypi.org/project/pymodm
https://pymodm.readthedocs.io/en/stable/


## Phone Validation and Parsing
https://pypi.org/project/phonenumbers/

from app import app

print("\n\n")

#app.run(debug=True)


from dataClasses.products import NutritionalValueObj, CerealObj, DataFactory

a = NutritionalValueObj(5,5,5,5,5,5,5,5,5)
b = CerealObj("abc","abc",a,1,2,3,4)


_dict = b.to_dict()
_list = DataFactory.create_from_dict(**_dict)
for _item in _list:
    print(_item.nutritions.to_dict())
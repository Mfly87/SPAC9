from app import app

#app.run(debug=True)


from database import NutritionalValueObj, CerealObj

a = NutritionalValueObj(5,-5,5,5,5,5,5,5,5)
b = CerealObj("abc","abc",a,1,2,3,4)

print("\n\n")
print(a.to_dict())
print(a.is_valid())
print("\n\n")
print(b.to_dict())
print(b.is_valid())

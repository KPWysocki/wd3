produkty={"sok": "litry", "chleb": "sztuki", "piwo": "butelki"}
sztuki={value: key for key, value in produkty.items()}
print(sztuki)

lista=[(i,j) for i in sztuki.keys for j in sztuki.items if sztuki.keys()=="sztuki"]
print(lista)

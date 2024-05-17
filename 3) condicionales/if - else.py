
# condicional if-else

print("condicional if-else (sino)");

llueve=True;
es_feriado=False;

if llueve or es_feriado:
    print("me quedo en casa");
else:
    print("voy al snpp");

x=28;
if x<0:
    print(x, "es manor que cero");
else:
    print(f"{x} es mayor que cero");


e=int(input("ingrese su edad: "));
if e>18:
    print("es mayor de edad");
elif e<18:
    print("es meor de edad");
else:
    print("tiene 18 años");
'''
a=int(input("inicio: "));
b=int(input("final: "));

for i in range(a,b,2):
    print(i);
    '''
x=int(input("ingrese un numero para la tabla de multiplicar: "));
print("tabla de multiplicar con el ciclo while...");
i=0;
while i<=10:
    res=x*i;
    print(f"{x}x{i}={res}");
    i=i+1;

print("tabla de multiplicar con el ciclo for...");

m=int(input("ingrese otro numero: "));
for c in range(10):
    p=m*c;
    print(f"{m}x{c}={p}")

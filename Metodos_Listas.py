class Metodos:
    def ingreso_elementos(self,List,tam):
        for i in range(tam):
            print("ingrese un numero en la List[",i,"]: ")
            num=(int(input("numero ")))
            List.append(num)
    def imprimir_elementos(self,List,tam):
        for i in range(tam):
            print(List[i])

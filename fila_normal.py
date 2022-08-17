class fila_normal:
    codigo:int= 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ''

    def gera_senha_atual(self)->None:
        self.senha_atual = f'NM{self.codigo}'



    def resata_fila(self)->None:
        if self.codigo >=100:
            self.codigo = 0
        else:
            self.codigo+=1

    def atualiza_fila(self)->None:
        self.resata_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa:str)->str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'cliente atual:{cliente_atual}, dirija-se ao caixa {caixa}')


class FilaPrioritaria:

    codigo:int=0
    fila_prioritaria= []
    clientes_atendidos = []
    senha_atual = ''

    def gera_senha_atual(self)->None:
        self.senha_atual = f'NM{self.codigo}'

    def reseta_fila(self)->None:
        if self.codigo >=100:
            self.codigo = 0
        else:
            self.codigo +=1

    def atualiza_fila(self)->None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila_prioritaria.append(self.senha_atual)

    def chama_cliente(self, caixa:int)->str:
        cliente_atual = self.fila_prioritaria.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'cliente atual:{cliente_atual}, dirija-se ao caixa {caixa}')

    def estatistica(self, dia: str, agencia: int, flag: str)->dict:
        if flag!= 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.clientes_atendidos
            estatistica['quantidade de clientes atendidos'] = len(self.clientes_atendidos)
        return estatistica

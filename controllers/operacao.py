# -*- coding: utf-8 -*-
def index(): 
    data_atual=request.now
    mes=request.now
    ano=request.now
    mes=request.args(0, cast=int)
    ano=request.args(1, cast=int)
    primeira_data=datetime.date(ano, mes, 1)
    ultima_data=datetime.date(ano, mes, 1)

    if (mes==12):
        ultima_data=datetime.date(ano+1, 1, 1)
    else:
        ultima_data=datetime.date(ano, mes+1, 1)
    rows = db((db.operacao.data_operacao>=primeira_data)&(db.operacao.data_operacao<ultima_data)).select(orderby=db.operacao.data_operacao)
    return locals()

def alt_operacao():
    response.view = 'generic.html' # use a generic view
    operacao = db.operacao(request.args(0, cast=int))
    cliente = db.cliente(operacao.cliente)
    usuario=auth.user
    deletar=False
    if usuario.id==1:
        deletar=True
    db.operacao.id.readable = False
    db.operacao.id.writable = False
    db.operacao.tipo_operacao.readable = False
    db.operacao.tipo_operacao.writable = False
    db.operacao.operadora.readable = False
    db.operacao.operadora.writable = False
    db.operacao.cliente.readable = False
    db.operacao.cliente.writable = False
    db.operacao.tipo_conta.readable = False
    db.operacao.tipo_conta.writable = False
    db.operacao.nome_conta.readable = False
    db.operacao.nome_conta.writable = False
    db.operacao.cpf_conta.readable = False
    db.operacao.cpf_conta.writable = False
    db.operacao.nome.readable = False
    db.operacao.nome.writable = False
    db.operacao.cpf.readable = False
    db.operacao.cpf.writable = False
    db.operacao.telefone.readable = False
    db.operacao.telefone.writable = False
    db.operacao.nome.readable = False
    db.operacao.nome.writable = False
    db.operacao.nome.readable = False
    db.operacao.nome.writable = False
    db.operacao.tipo_operacao.readable = False
    db.operacao.tipo_operacao.writable = False
    db.operacao.cliente.readable = False
    db.operacao.cliente.writable = False
    db.operacao.valor_operacao.readable = True
    db.operacao.valor_operacao.writable = False
    db.operacao.valor_repassado.readable = False
    db.operacao.valor_repassado.writable = False
    db.operacao.quant_parcelas.readable = False
    db.operacao.quant_parcelas.writable = False
    db.operacao.bonus.readable = False
    db.operacao.bonus.writable = False
    db.operacao.data_operacao.readable = True
    db.operacao.data_operacao.writable = True
    db.operacao.banco.readable = False
    db.operacao.banco.writable = False
    db.operacao.agencia.readable = False
    db.operacao.agencia.writable = False
    db.operacao.conta.readable = False
    db.operacao.conta.writable = False
    db.operacao.tipo_conta.readable = False
    db.operacao.tipo_conta.writable = False
    db.operacao.valor_comissao.readable = True
    db.operacao.valor_comissao.writable = True
    db.operacao.produtor_pago.readable = True
    db.operacao.produtor_pago.writable = True
    db.operacao.taxa_operadora.readable = False
    db.operacao.taxa_operadora.writable = False
    db.operacao.confirmado.readable = True
    db.operacao.confirmado.writable = True

    form = SQLFORM(db.operacao, request.args(0, cast=int), deletable=deletar)
    if form.process().accepted:
        session.flash = 'Projeto atualizado'
        redirect(URL('operacao','visualizar_operacao', args=operacao.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)


def visualizar_operacao():
    operacao = db.operacao(request.args(0, cast=int))
    return locals()

def confirmar_operacao():
    operacao = db.operacao(request.args(0, cast=int))
    if operacao.confirmado:
        operacao.confirmado=False
    else:
        operacao.confirmado=True
    operacao.update_record()
    redirect(URL('index', args=[operacao.data_operacao.month,operacao.data_operacao.year]))
    return locals()

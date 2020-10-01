# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

def index():
    form = db((db.cliente)).select()
    return locals()

@auth.requires_login()
def lista_cliente():

    # Se não for unformado o número da página, deduzimos que é a primeira
    paginacao = 10
    if len(request.args) == 0:
        pagina = 1
    else:
        # Tenta converter o número da página
        try:
            pagina = int(request.args[0])
        except ValueError:
            # Redireciona para a página de erro
            redirect(URL('erro', vars={
                    'msg':'Numero da página inválido'
                    }))

    # Se a página informada é 0, redireciona para a página 1
    if pagina <= 0:
        redirect(URL(args=1))

    # Total de clientes
    total = db(db.cliente).count()

    # Calcula o total de páginas
    paginas = total/paginacao
    if total%paginacao:
        paginas+=1

    # Se o número de página extrapolou o possível, redirecione para a
    # última página
    if pagina > paginas:
        redirect(URL(args=[paginas]))

    # Calcula os limites da consulta
    limites = (paginacao*(pagina-1), (paginacao*pagina))
    registros = db(db.cliente).select(
        limitby=limites,
        )
    consul=(request.args(1))
    if (consul):
        registros = db((db.cliente.cpf.contains(consul))|(db.cliente.nome.contains(consul))).select(limitby=(0,20))
    return dict(rows=registros, pagina=pagina, paginas=paginas)
    return locals()

def lista_cliente_amostra():

    # Se não for unformado o número da página, deduzimos que é a primeira
    paginacao = 10
    if len(request.args) == 0:
        pagina = 1
    else:
        # Tenta converter o número da página
        try:
            pagina = int(request.args[0])
        except ValueError:
            # Redireciona para a página de erro
            redirect(URL('erro', vars={
                    'msg':'Numero da página inválido'
                    }))

    # Se a página informada é 0, redireciona para a página 1
    if pagina <= 0:
        redirect(URL(args=1))

    # Total de clientes
    total = db(db.cliente).count()

    # Calcula o total de páginas
    paginas = total/paginacao
    if total%paginacao:
        paginas+=1

    # Se o número de página extrapolou o possível, redirecione para a
    # última página
    if pagina > paginas:
        redirect(URL(args=[paginas]))

    # Calcula os limites da consulta
    limites = (paginacao*(pagina-1), (paginacao*pagina))
    registros = db(db.cliente).select(
        limitby=limites,
        )
    consul=(request.args(1))
    if (consul):
        registros = db(db.cliente.nome.contains(consul)).select(limitby=(0,20))
    return dict(rows=registros, pagina=pagina, paginas=paginas)
    return locals()

@auth.requires_login()
def acesso_cliente():
    cliente = db.cliente(request.args(0, cast=int))
    rows = db(db.operacao.cliente==cliente.id).select()
    return locals()

@auth.requires_login()
def cad_cliente():
    response.view = 'generic.html' # use a generic view
    form = SQLFORM(db.cliente).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('lista_cliente'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)

@auth.requires_login()
def alt_cliente():
    response.view = 'generic.html' # use a generic view
    cliente = db.cliente(request.args(0, cast=int))
    form = SQLFORM(db.cliente, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Projeto atualizado'
        redirect(URL('acesso_cliente', args=cliente.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    return dict(form=form)

@auth.requires_login()
def alt_operacao():
    response.view = 'generic.html' # use a generic view
    operacao = db.operacao(request.args(0, cast=int))
    cliente = db.cliente(operacao.cliente)

    db.operacao.id.readable = False
    db.operacao.id.writable = False

    db.operacao.cliente.readable = False
    db.operacao.cliente.writable = False

    form = SQLFORM(db.operacao, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Projeto atualizado'
        redirect(URL('acesso_cliente', args=cliente.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)

@auth.requires_login()
def alt_operacao_admin():
    response.view = 'generic.html' # use a generic view
    operacao = db.operacao(request.args(0, cast=int))
    cliente = db.cliente(operacao.cliente)

    db.operacao.id.readable = False
    db.operacao.id.writable = False

    db.operacao.tipo_operacao.readable = False
    db.operacao.tipo_operacao.writable = False

    db.operacao.cliente.readable = False
    db.operacao.cliente.writable = False

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

    db.operacao.data_operacao.readable = False
    db.operacao.data_operacao.writable = False

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

    db.operacao.taxa_operadora.readable = True
    db.operacao.taxa_operadora.writable = True

    db.operacao.confirmado.readable = True
    db.operacao.confirmado.writable = True

    form = SQLFORM(db.operacao, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Projeto atualizado'
        redirect(URL('acesso_cliente', args=cliente.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'

    return dict(form=form)
@auth.requires_login()
def cad_operacao():
    response.view = 'generic.html' # use a generic view
    cliente = db.cliente(request.args(0, cast=int))
    db.operacao.id.readable = False
    db.operacao.id.writable = False
    db.operacao.nome.default = cliente.nome
    db.operacao.telefone.default = cliente.telefone
    db.operacao.cpf.default = cliente.cpf

    db.operacao.nome_conta.default = cliente.nome
    db.operacao.cpf_conta.default = cliente.cpf
    db.operacao.data_operacao.readable = True
    db.operacao.data_operacao.writable = False

    db.operacao.cliente.default = cliente.id
    db.operacao.cliente.writable = False

    form = SQLFORM(db.operacao).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('acesso_cliente', args=cliente.id))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)


@auth.requires_login()
def acesso_operacao():
    operacao = db.operacao(request.args(0, cast=int))
    return locals()

@auth.requires_login()
def visualizar_operacao():
    operacao = db.operacao(request.args(0, cast=int))
    return locals()
# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

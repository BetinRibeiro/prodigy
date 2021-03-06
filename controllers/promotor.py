# -*- coding: utf-8 -*-
@auth.requires_login()
def lista_promotor():
    rows = db(db.produtor.id!=1).select(orderby=db.produtor.nome)
    return locals()
@auth.requires_login()
def cad_produtor():
    response.view = 'generic.html' # use a generic view
    form = SQLFORM(db.produtor).process()
    if form.accepted:
        response.flash = 'Formulario aceito'
        redirect(URL('lista_promotor'))
    elif form.errors:
        response.flash = 'Formulario não aceito'
    else:
        response.flash = 'Preencha o formulario'
    return  dict(form=form)
@auth.requires_login()
def alt_produtor():    
    response.view = 'generic.html' # use a generic view
    produtor = db.produtor(request.args(0, cast=int))
    form = SQLFORM(db.produtor, request.args(0, cast=int), deletable=False)
    if form.process().accepted:
        session.flash = 'Projeto atualizado'
        redirect(URL('lista_promotor', args=produtor.id))
    elif form.errors:
        response.flash = 'Erros no formulário!'
        
    return dict(form=form)

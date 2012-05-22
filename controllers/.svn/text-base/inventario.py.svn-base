def index(): return dict()

@auth.requires_login()
def criar():
    inventarioform = SQLFORM(db.inventario,submit_button="Inserir")
    if inventarioform.accepts(request.vars, session):
        session.flash = "Inserido!"
        redirect(URL(r=request, f="visualizar", args=inventarioform.vars.id))
    return dict(inventarioform=inventarioform)

@auth.requires_login()
def visualizar():
    inventarioid = request.args(0)
    inventario = db(db.inventario.id == inventarioid).select()[0]
    return dict(inventario = inventario)

@auth.requires_login()
def gerenciar():
    form = SQLFORM.smartgrid(db.inventario,ui='jquery-ui',paginate=20,searchable=True,showbuttontext=False,sortable=True, details=True,user_signature = False,maxtextlength=50,csv=True, search_widget='default',create=True,linked_tables=['child'],\
                             formname='web2py_grid', fields=[db.inventario.nome,db.inventario.descricao],
                             formstyle = 'divs',
                             upload = '<default>',
                             )
    return dict(form=form)

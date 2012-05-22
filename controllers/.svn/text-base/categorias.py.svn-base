def index(): return dict()

#Criar Categorias dos Inventarios
@auth.requires_login()
def criar_inventario():
    form = SQLFORM(db.inventario_categorias)
    return dict(form=form)

def teste():
      form = SQLFORM.smartgrid(db.arquivos_categorias,ui='jquery-ui',paginate=20,searchable=True,showbuttontext=False,sortable=True, details=True,user_signature = False,maxtextlength=50,csv=True, search_widget='default',create=True,linked_tables=['child'],\
                             formname='web2py_grid',
                             formstyle = 'divs',
                             )
      return dict(form=form)

#Criar categorias dos Arquivos
@auth.requires_login()
def criar_arquivos():
    form = SQLFORM(db.arquivos_categorias)
    if form.accepts(request.vars,session):
        session.flash = "Inserido!"
        redirect(URL(r=request,f="visualizar_arquivo",args=form.vars.id))
    return dict(form=form)
@auth.requires_login()
def gerenciar_inventario():
    form = SQLFORM.smartgrid(db.inventario_categorias,ui='jquery-ui',paginate=20,searchable=True,showbuttontext=False,sortable=True, details=True,user_signature = False,maxtextlength=50,csv=True, search_widget='default',create=True,linked_tables=['child'],\
                             formname='web2py_grid',fields=[db.inventario_categorias.nome,db.inventario_categorias.descricao],
                             formstyle = 'divs',
                             upload = '<default>',
                             )
    return dict(form=form)
@auth.requires_login()
def gerenciar_arquivos():
    form = SQLFORM.smartgrid(db.arquivos_categorias,ui='jquery-ui',paginate=20,searchable=True,showbuttontext=False,sortable=True, details=True,user_signature = False,maxtextlength=50,csv=True, search_widget='default',create=True,linked_tables=['child'],\
                             formname='web2py_grid',fields=[db.arquivos_categorias.nome,db.arquivos_categorias.descricao],
                             formstyle = 'divs',
                             upload = '<default>',
                             )
    return dict(form=form)

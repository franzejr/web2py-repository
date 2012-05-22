def index():
    return

@auth.requires_login()
def criar():
    arquivoform = SQLFORM(db.arquivos_upload,fields=['nome','descricao','arquivo','categoria'],submit_button="Inserir Arquivo")
    categorias = db(db.arquivos_categorias).select()
    if arquivoform.accepts(request.vars, session):
        session.flash = "Inserido!" 
        redirect(URL(r=request, f="visualizar", args=arquivoform.vars.id))
    return dict(arquivoform=arquivoform,categorias=categorias)
@auth.requires_login()
def visualizar():
    arquivoid = request.args(0)
    arquivo = db(db.arquivos_upload.id == arquivoid).select()[0]
    return dict(arquivo = arquivo)

@auth.requires_login()
def buscar():
    form, rows=crud.search(db.arquivos_upload,queries = ['equals','contains'],query_labels={'equals':'Igual','contains':'Contem'})
    return dict(form=form, rows=rows)
@auth.requires_login()
def buscarCategoria():
    categorias = db(db.arquivos_categorias).select()
    form = SQLFORM.factory(db.arquivos_upload,fields=['nome','categoria'],submit_button="Pesquisar",record=False)
    result = ""                
    if form.accepts(request.vars,session):
        try:
            result = db((db.arquivos_upload.nome.contains(request.vars.nome))  \
                          & (db.arquivos_upload.categoria.contains(request.vars.categoria) ) \
                          ).select()
        except:
            result = db((db.arquivos_upload.categoria.contains(request.vars.categoria) ) \
                          ).select()
    return dict(categorias=categorias,form=form,result=result)

@auth.requires_login()
def listar():
    records = db(db.arquivos_upload).select(db.arquivos_upload.ALL)
    return dict(records=records)

@auth.requires_login()
def gerenciar():
    form = SQLFORM.smartgrid(db.arquivos_upload,ui='jquery-ui',paginate=20,searchable=True,showbuttontext=False,sortable=True, details=True,user_signature = False,maxtextlength=50,csv=True, search_widget='default',create=True,linked_tables=['child'],\
                             formname='web2py_grid',fields=[db.arquivos_upload.nome,db.arquivos_upload.descricao,db.arquivos_upload.arquivo,db.arquivos_upload.categoria],
                             formstyle = 'divs',
                             upload = '<default>',
                             )
    return dict(form=form)
    
    
########################
##Funcoes que trabalham com json
########################
def getIdArquivo():
    cat = request.vars['cat[]']
    nome = request.vars.nome

    try:
        result = db((db.arquivos_upload.nome.contains(nome)) & (db.arquivos_upload.id == db.categorias_arq.arquivo)  \
                      & (db.categorias_arq.categoria.contains(cat) ) \
                      ).select(db.arquivos_upload.id)
    except:
        return response.json(cat)
    return response.json(result)




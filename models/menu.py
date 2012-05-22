response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
    (T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
    
    (T('Arquivos'),False,URL('arquivos','gerenciar'),[
        (T('Inserir'),False,URL('arquivos','criar'),[]),
        (T('Busca em Geral'),False,URL('arquivos','buscar'),[]),
        (T('Buscar por Categoria'),False,URL('arquivos','buscarCategoria'),[]),
    ]),
                 
    (T('Inventario'),False,URL('inventario','gerenciar'),[
        (T('Criar'),False,URL('inventario','criar'),[]),
        (T('Gerenciar'),False,URL('inventario','gerenciar'),[]),
    ]),
                 
    (T('Categorias'),False,URL('categorias','#'),[
        (T('Arquivos'),False,URL('categorias','gerenciar_arquivos'),[
        ]), 
        (T('Inventário'),False,URL('categorias','gerenciar_inventario'),[
        ])],
     )]
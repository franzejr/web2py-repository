# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

def arquivos_upload_manage():
    form = SQLFORM.smartgrid(db.t_arquivos_upload,onupdate=auth.archive)
    return locals()

def arquivos_categorias_manage():
    form = SQLFORM.smartgrid(db.t_arquivos_categorias,onupdate=auth.archive)
    return locals()




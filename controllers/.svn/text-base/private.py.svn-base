# -*- coding: utf-8 -*-

@auth.requires_login()
def users():
    form = SQLFORM.smartgrid(db.auth_user,ui='jquery-ui',paginate=20,searchable=True,showbuttontext=False,sortable=True, details=True,user_signature = False,maxtextlength=50,csv=True, search_widget='default',create=True,linked_tables=['child'],\
                             formname='web2py_grid', fields=[db.auth_user.username,db.auth_user.registration_key,db.auth_user.first_name],
                             formstyle = 'divs',
                             upload = '<default>',
                             )
    return dict(form=form)

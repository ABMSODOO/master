# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2018 abmsodoo All Rights Reserved
#
##############################################################################
{
    'name': 'HR Contract Dynamic Fields',
    'version': '1.0',
    'category': 'HR',
    'price': 35.00,
    'currency': 'EUR',
    'license': 'OPL-1',
    'author':'ABMSODOO',
    'images': ['images/main_1.png', 'images/main_2.png', 'static/description/main_screenshot.PNG'],
    'description': """
    Key Features
    ------------
    You can add the fields in employee contracts for salary rules""",
    'depends': ['base','hr','hr_contract'],
    'data':['views/view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

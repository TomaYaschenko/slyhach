my_dict={'Nechita Bogdan':{'Python}','Java'},
         'Marhalov Volodymir':{'FrontEnd}','FullStack'},
         'Bylat Sofiya':{'Python}','FrontEnd'},
         'Kycher Roman':{'FrontEnd'} }
backend={'Python','Java'}
for name,groups in my_dict.items():
    if len(groups)>1:
        print('2 or more groups: ',name, groups)

    if 'FontEnd' not in groups:
        print('No FrontEnd: ', name, groups)

    if backend & groups:
        print('no FrontEnd: ',name,groups)



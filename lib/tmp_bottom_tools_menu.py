gh={'b1_name':'b_up1',
    'b2_name':'b_up2',
    'b3_name':'b_up3',
    'b4_name':'b_up4',
    'b5_name':'b_up5',}

def vv(**k_var):
    gh={}
    for x in k_var:
        gh[x]=k_var[x]
    return gh

bb=vv(b1_name='b_up1',b2_name='b_up2')
for x in bb:
    print(x)
    print(bb[x])
import xmlrpc.client
from xmlrpc_lib import XmlrpcLib 
from migration_lib import MigrationLib
from pprint import pprint

odoo11 = XmlrpcLib('http://192.168.1.5:8069', '11_test', 'test@test.com', 'test')
odoo13 = XmlrpcLib('http://192.168.1.5:8070', '13_test', 'test1@test.com', 'test')

print(odoo11.get_version())
print(odoo13.get_version())

migrate = MigrationLib(odoo11, odoo13)
print('Odoo 11: {}'.format(odoo11.search_read('res.users', fields=['name'])))
print('Odoo 13: {}'.format(odoo13.search_read('res.users', fields=['name'])))
pprint(migrate.inspect_differences('res.users'))
migrate.copy_table('res.users', 'res.users')
#print(odoo11.search_read('res.partner', fields=['name', 'create_uid']))
# url_1 = 'http://192.168.1.5:8069'
# url_2 = 'http://192.168.1.5:8070'
# db_1 = '11_test'
# db_2 = '13_test'
# username_1 = 'test@test.com'
# password_1 = 'test'
# username_2 = 'test@test.com'
# password_2 = 'test'

# common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_1))
# print(common.version())
# uid_1 = common.authenticate(db_1, username_1, password_1, {})

# common2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_2))
# print(common2.version())
# uid_2 = common2.authenticate(db_2, username_2, password_2, {})

# models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_1))
# record = models.execute_kw(db_1, uid_1, password_1,
#     'res.partner', 'search_read',
#     [[]])

# pprint(record)
# print(uid_2)

# models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_2))
# record = models_2.execute_kw(db_2, uid_2, password_2,
#         'res.partner', 'search',
#         [[]])

# pprint(record)
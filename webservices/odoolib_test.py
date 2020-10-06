import odoorpc

# Prepare the connection to the server
odoo = odoorpc.ODOO("localhost", port=8069)

# Check available databases
# print(odoo.db.list())

# Login
odoo.login("odoodb", "admin", "admin")

# Current user
user = odoo.env.user
# print(user.name)  # name of the user connected
# print(user.company_id.name)  # the name of its company

# Simple 'raw' query


odoo.execute("openacademy.course", "create", {"name": "Course created from odoolib"})

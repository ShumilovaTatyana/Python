import operations as oper
import export as expr
import user_interface

def run():
    oper = user_interface.get_operation()
    match oper:
        case '1':
            db_csv_name = user_interface.get_db_name()
            db_json_name = user_interface.get_db_name()
            expr.export_db(db_csv_name + '.csv', db_json_name + '.ison')
            



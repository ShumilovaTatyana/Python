import model as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_c = view.get_value()
    numm = view.get_oper()
    model.init(value_a, value_b, value_c)
    result = model.do_it()
    view.view_data(result, "result")
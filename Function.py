
def on_radio_select(r_var, tempa, timer):
    if r_var.get() == 0:
        for i in tempa:
            i.config(state="normal")
        for i in timer:
            i.config(state="normal")
    else:
        for i in tempa:
            i.config(state="disabled")
        for i in timer:
            i.config(state="disabled")

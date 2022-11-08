import dearpygui.dearpygui as dpg

def save_callback():
    print('Save Clicked')


dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=1000)
dpg.setup_dearpygui()

#testing
print('test')

with dpg.window(label="Example Window"):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
import dearpygui.dearpygui as dpg

def save_callback():
    print('Save Clicked')


dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=1000)
dpg.setup_dearpygui()


with dpg.window(label="C^2"):
    dpg.add_text("Examinee Form")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string", default_value='First Name')
    #dpg.add_slider_float(label="float")

dpg.show_viewport()

#can replace start_dearpygui()
while dpg.is_dearpygui_running():
    #print('running')
    dpg.render_dearpygui_frame()

print('end')
print('ivan was here')

dpg.destroy_context()
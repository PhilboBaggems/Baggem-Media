def swith_frame(driver, frame_index):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame_index)

def switch_window(driver, window_index):
    driver.switch_to.default_content()
    driver.swith_to.window(driver.window_handles[window_index])

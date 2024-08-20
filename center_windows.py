def center_window(window, min_width, min_height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - min_width) // 2
    y = (screen_height - min_height) // 2

    window.geometry(f"{min_width}x{min_height}+{x}+{y}")

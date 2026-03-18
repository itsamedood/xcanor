from gui import GUI
from tkinter import Menu
from util import Util


def setup_menu(gui: GUI) -> Menu:
  menu = Menu(gui)

  # Create menus.
  task_menu = Menu(gui)
  misc_menu = Menu(gui)

  # Create buttons (cascades) at the task bar (top left).
  menu.add_cascade(label="Task", menu=task_menu)
  menu.add_cascade(label="Misc", menu=misc_menu)

  # Add selections to cascades.
  task_menu.add_checkbutton(label="Run forever", command=lambda: Util.toggle_forever(), state="active")

  misc_menu.add_checkbutton(label="Japanese title", command=lambda: gui.toggle_title())
  misc_menu.add_separator()
  misc_menu.add_command(label="Exit", command=gui.quit)

  return menu


if __name__ == "__main__":
  menu = setup_menu(gui:=GUI())
  gui.config(menu=menu)

  gui.mainloop()  # Run!

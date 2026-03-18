from tkinter import Frame


class MainFrame(Frame):
  """ Initial frame when launched. """

  # `controller` is `GUI` but can't be imported as it causes a circular import.
  def __init__(self, parent: Frame, controller) -> None:
    Frame.__init__(self, parent)
    self.controller = controller

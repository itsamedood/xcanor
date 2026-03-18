from frames.mainFrame import MainFrame
from PIL import Image, ImageTk
from tkinter import Frame, Tk
from util import Util


class GUI(Tk):
  """ Heart of the program as it's the master for the GUI, as the name suggests. """

  frame_stack: list[str] = []  # Contains a stack-like trace of the frames, so we can go back and forth between screens (frames).

  def __init__(self, *args, **kwargs):
    Tk.__init__(self, *args, **kwargs)

    # Set keybind for escape key.
    self.bind("<Key>", lambda event: print("escape!") if event.keysym == "Escape" else ...)

    # Init main window.
    self.title("Xcanor - Lion's Sin of Automation")
    self.geometry("640x480")
    self.attributes("-alpha", 0.8)  # Slight transparency.
    self.resizable(False, False)

    icon = ImageTk.PhotoImage(Image.open("assets/xcanor_msp.png"))
    self.iconphoto(True, icon)  # Ignore error, this does actually work.

    # Making the container (same size as the window) where frames will go.
    # This creates the illusion of switching between menus.
    self.container = Frame(self)
    self.container.pack(side="top", fill="both", expand=True)
    self.container.grid_rowconfigure(0, weight=1)
    self.container.grid_columnconfigure(0, weight=1)

    self.frames: dict[str, Frame] = {}

    # Manually add the frames here.
    for F in (
      MainFrame,
    ):
      name = F.__name__
      frame = F(self.container, self)
      frame.grid(row=0, column=0, sticky="nsew")
      self.frames[name] = frame

    self.show_frame("MainFrame")

  def show_frame(self, frame: str) -> ...: ...

  def toggle_title(self) -> None:
    Util.toggle_japanese_title()
    self.title("エクスカノール - 自動化の獅子の罪" if Util.japanese_title else "Xcanor - Lion's Sin of Automation")

  # def on_esc(self, event: Event):
  #     if event.keysym == "Escape": ...

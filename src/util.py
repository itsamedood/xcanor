class Util:
  run_forever = False
  japanese_title = False

  @staticmethod
  def toggle_forever() -> None:
    Util.run_forever = not Util.run_forever

  @staticmethod
  def toggle_japanese_title() -> None:
    Util.japanese_title = not Util.japanese_title

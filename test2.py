from QTileLayout import QTileLayout

layout = QTileLayout(
    rowNumber=8,
    columnNumber=5,
    verticalSpawn=100,
    horizontalSpan=150,
    verticalSpacing=0.125,
    horizontalSpacing=0.125,
)

layout.addWidget(
    widget=QtWidgets.QLabel('Hello world'),
    fromRow=3,
    fromColumn=2,
    rowSpan=1,python
)


#URL: https://pypi.org/project/pyqt5-tile-layout/
# https://libraries.io/pypi/pyqt5-tile-layout
# https://github.com/arnaudframmery/qt-tile-layout

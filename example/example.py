#!python
# -*- coding: utf-8 -*-

"""Example of qdarkstyle use for Python and Qt applications.

This module provides a main window with every item that could be created with
Qt Design (common ones) in the basic states (enabled/disabled), and
(checked/unchecked/tristate) for those who has this attribute.

Requirements:

    - Python 2 or Python 3
    - PyQt4 or PyQt5 or PySide or PySide2
    - QtPy
    - PyQtGraph (if choosen)

To run this example using PyQt5, simple do

.. code-block:: python

    python example.py

or

.. code-block:: python

    python example.py  --qt_api=pyqt5

To use PySide instead, do

.. code-block:: python

    python example.py  --qt_api=pyside

You also can run the example without dark theme (no_dark), to check for
problems.

.. code-block:: python

    python example.py  --qt_api=pyqt5 --no_dark

To get help

.. code-block:: python

    python example.py  --help

.. note.. :: qdarkstyle does not have to be installed to run the example.

"""

import argparse
import os
import sys
import warnings
from os.path import abspath, dirname

# show all warnings
warnings.simplefilter('always')

# make the example runnable without the need to install
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))


def main():
    """Execute QDarkStyle example."""
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--qt_api', default='pyqt5',
                        choices=['pyqt', 'pyqt5', 'pyside', 'pyside2'],
                        help="Choose which binding is to be used to run the example.", type=str)
    parser.add_argument('--no_dark', action='store_true',
                        help="Exihibts the original  window (without qdarkstyle).")
    parser.add_argument('--test', action='store_true',
                        help="Auto close window after 2s.")
    parser.add_argument('--reset', action='store_true',
                        help="Reset stored application settings.")

    # parsing arguments from command line
    args = parser.parse_args()

    # set up QT_API before importing QtPy
    os.environ['QT_API'] = args.qt_api

    # using QtPy API
    from qtpy import QtGui, QtWidgets, QtCore, API_NAME

    # import examples UI
    from ui.mw_menus_ui import Ui_MainWindow as ui_main
    from ui.dw_buttons_ui import Ui_DockWidget as ui_buttons
    from ui.dw_displays_ui import Ui_DockWidget as ui_displays
    from ui.dw_inputs_fields_ui import Ui_DockWidget as ui_inputs_fields
    from ui.dw_inputs_no_fields_ui import Ui_DockWidget as ui_inputs_no_fields
    from ui.dw_widgets_ui import Ui_DockWidget as ui_widgets
    from ui.dw_views_ui import Ui_DockWidget as ui_views
    from ui.dw_containers_tabs_ui import Ui_DockWidget as ui_containers_tabs
    from ui.dw_containers_no_tabs_ui import Ui_DockWidget as ui_containers_no_tabs

    # must be in this place, after setting path, to not need to install
    import qdarkstyle

    # getting stylesheet
    style = qdarkstyle.load_stylesheet()

    if args.no_dark:
        style = ""

    # functions to restore window state after closing
    def write_settings(window):
        """Get window settings and write it into a file."""
        settings = QtCore.QSettings('QDarkStyle', 'QDarkStyle Example')
        settings.setValue('pos', window.pos())
        settings.setValue('size', window.size())
        settings.setValue('state', window.saveState())

    def read_settings(window, reset=False):
        """Read and set window settings from a file."""
        settings = QtCore.QSettings('QDarkStyle', 'QDarkStyle Example')

        if reset:
            settings.clear()

        pos = settings.value('pos', window.pos())
        size = settings.value('size', window.size())
        state = settings.value('state', window.saveState())

        window.restoreState(state)
        window.resize(size)
        window.move(pos)

    # create the application
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName('QDarkStyle')
    app.setApplicationName('QDarkStyle Example')

    # setup stylesheet
    app.setStyleSheet(style)

    # create main window
    window = QtWidgets.QMainWindow()
    window.setObjectName('mainwindow')
    ui = ui_main()
    ui.setupUi(window)
    window.setWindowTitle("QDarkStyle v." + qdarkstyle.__version__ +
                          " - Example - Using QtPy with " + API_NAME)

    # create docks for buttons
    dw_buttons = QtWidgets.QDockWidget()
    dw_buttons.setObjectName('buttons')
    ui_buttons = ui_buttons()
    ui_buttons.setupUi(dw_buttons)
    window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dw_buttons)

    # create docks for buttons
    dw_displays = QtWidgets.QDockWidget()
    dw_displays.setObjectName('displays')
    ui_displays = ui_displays()
    ui_displays.setupUi(dw_displays)
    window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dw_displays)

    # create docks for inputs - fields
    dw_inputs_fields = QtWidgets.QDockWidget()
    dw_inputs_fields.setObjectName('fields')
    ui_inputs_fields = ui_inputs_fields()
    ui_inputs_fields.setupUi(dw_inputs_fields)
    window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dw_inputs_fields)

    # create docks for inputs - no fields
    dw_inputs_no_fields = QtWidgets.QDockWidget()
    dw_inputs_no_fields.setObjectName('inputs_no_fields')
    ui_inputs_no_fields = ui_inputs_no_fields()
    ui_inputs_no_fields.setupUi(dw_inputs_no_fields)
    window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dw_inputs_no_fields)

    # create docks for widgets - QListWidget
    dw_widgets = QtWidgets.QDockWidget()
    dw_widgets.setObjectName('widgets')
    ui_widgets = ui_widgets()
    ui_widgets.setupUi(dw_widgets)
    window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dw_widgets)

    # create docks for views
    dw_views = QtWidgets.QDockWidget()
    dw_views.setObjectName('views')
    ui_views = ui_views()
    ui_views.setupUi(dw_views)
    window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dw_views)

    # create docks for containters - tabs
    dw_containers_tabs = QtWidgets.QDockWidget()
    dw_containers_tabs.setObjectName('containers')
    ui_containers_tabs = ui_containers_tabs()
    ui_containers_tabs.setupUi(dw_containers_tabs)
    window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dw_containers_tabs)

    # create docks for containers - no tabs
    dw_containers_no_tabs = QtWidgets.QDockWidget()
    dw_containers_no_tabs.setObjectName('containers_no_tabs')
    ui_containers_no_tabs = ui_containers_no_tabs()
    ui_containers_no_tabs.setupUi(dw_containers_no_tabs)
    window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dw_containers_no_tabs)

    # tabify right docks
    window.tabifyDockWidget(dw_buttons, dw_displays)
    window.tabifyDockWidget(dw_displays, dw_inputs_fields)
    window.tabifyDockWidget(dw_inputs_fields, dw_inputs_no_fields)

    # tabify left docks
    window.tabifyDockWidget(dw_widgets, dw_views)
    window.tabifyDockWidget(dw_views, dw_containers_tabs)
    window.tabifyDockWidget(dw_containers_tabs, dw_containers_no_tabs)

    # auto quit after 2s when testing on travis-ci
    if "--test" in sys.argv:
        QtCore.QTimer.singleShot(2000, app.exit)

    # run
    read_settings(window, args.reset)
    window.showMaximized()
    window.setWindowFlags(window.windowFlags() |
                          QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowMaximizeButtonHint |
                          QtCore.Qt.WindowCloseButtonHint)
    app.exec_()
    write_settings(window)


if __name__ == "__main__":
    sys.exit(main())

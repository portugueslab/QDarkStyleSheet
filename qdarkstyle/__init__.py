#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""QDarkStyle is a dark stylesheet for Python and Qt applications.

This module provides a function to transparently load the stylesheet.

First, you can get stylesheet provided by QDarkStyle for various Qt bindings
as shown bellow. To correctly use this feature, set the environment variable
berofe any import or call. This will set the environment variable QT_API for
QtPy:

.. code-block:: python

    import os
    os.environ['QT_API'] = 'pyqt5'

Then, import our module

.. code-block:: python

    import qdarkstyle

If you already set up the QT_API environment variable, just use what as set

.. code-block:: python

    dark_stylesheet = qdarkstyle.load_stylesheet()

Finally, set your QApplication with it

.. code-block:: python

    app.setStyleSheet(dark_stylesheet)

Enjoy!

"""

import logging
import os
import platform
import warnings

__version__ = "3.0"

QT_API_VALUES = ['pyqt', 'pyqt5', 'pyside', 'pyside2']


def _logger():
    return logging.getLogger('qdarkstyle')


def load_stylesheet(qt_api=''):
    """
    Load the stylesheet based on QtPy abstraction layer environment variable.

    Note: if you are using other abstraction layer, i.e PyQtGraph to do imports
    on Qt things you must set both to use the same Qt binding (PyQt, Pyside).

    :return the stylesheet string (css)
    """

    if qt_api:
        os.environ['QT_API'] = qt_api


    from qtpy.QtCore import QFile, QTextStream
    import qdarkstyle.style_rc

    f = QFile(":qdarkstyle/style.qss")

    if not f.exists():
        _logger().error("Unable to load stylesheet, file not found in "
                        "resources")
        return ""
    else:
        f.open(QFile.ReadOnly | QFile.Text)
        ts = QTextStream(f)
        stylesheet = ts.readAll()
        if platform.system().lower() == 'darwin':  # see issue #12 on github
            mac_fix = '''
            QDockWidget::title
            {
                background-color: #31363b;
                text-align: center;
                height: 12px;
            }
            '''
            stylesheet += mac_fix
        return stylesheet

##############################################################################
# Deprecated functions to be removed on version 4.0
##############################################################################


def load_stylesheet_from_environment(is_pyqtgraph=False):
    """
    Load the stylesheet from QT_API (or PYQTGRAPH_QT_LIB) environment variable.

    :param is_pyqtgraph: True if it is to be set using PYQTGRAPH_QT_LIB

    :raise KeyError: if QT_API/PYQTGRAPH_QT_LIB does not exist

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_from_environment() is deprecated in version 3,"
        "use load_stylesheet(), no more need for is_pyqtgraph parameter.",
        DeprecationWarning
    )
    return load_stylesheet()


def load_stylesheet_pyside():
    """
    Load the stylesheet for use in a pyside application.

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyside() is deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and/or "
        "use load_stylesheet(qt_api='pyside')",
        DeprecationWarning
    )
    return load_stylesheet(qt_api='pyside')


def load_stylesheet_pyside2():
    """
    Load the stylesheet for use in a pyside2 application.

    :raise NotImplementedError: Because it is not supported yet
    """
    warnings.warn(
        "load_stylesheet_pyside2() is deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and/or "
        "use load_stylesheet(qt_api='pyside2')",
        DeprecationWarning
    )
    return load_stylesheet(qt_api='pyside2')


def load_stylesheet_pyqt():
    """
    Load the stylesheet for use in a pyqt4 application.

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyqt() is deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and/or "
        "use load_stylesheet(qt_api='pyqt')",
        DeprecationWarning
    )
    return load_stylesheet(qt_api='pyqt')


def load_stylesheet_pyqt5():
    """
    Load the stylesheet for use in a pyqt5 application.

    :param pyside: True to load the pyside rc file, False to load the PyQt rc file

    :return the stylesheet string
    """
    warnings.warn(
        "load_stylesheet_pyqt5() is deprecated in version 3,"
        "set QtPy environment variable to specify the Qt binding and/or "
        "use load_stylesheet(qt_api='pyqt5')",
        DeprecationWarning
    )
    return load_stylesheet(qt_api='pyqt5')

def _qt_wrapper_import(qt_api):
    """
    Check if Qt API defined can be imported.
    :param qt_api: Qt API string to test import
    :return load function fot given qt_api, otherwise empty string
    """
    warnings.warn(
        "_qt_wrapper_import() is deprecated in version 3,"
        "no need for this function anymore",
        DeprecationWarning
    )
    
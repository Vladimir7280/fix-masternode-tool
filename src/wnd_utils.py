#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Bertrand256
# Created on: 2017-03
import logging
import os
import threading
import traceback
import sys
import thread_utils
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QObject, QLocale
from PyQt5.QtGui import QPalette, QPainter, QBrush, QColor, QPen, QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QWidget, QFileDialog, QInputDialog
import math
import message_dlg
from thread_fun_dlg import ThreadFunDlg, WorkerThread
import app_cache as app_cache


class WndUtils:

    def __init__(self, app_config=None):
        self.app_config = app_config

    def messageDlg(self, message):
        ui = message_dlg.MessageDlg(self, message)
        ui.exec_()

    def set_app_config(self, app_config):
        self.app_config = app_config

    @staticmethod
    def displayMessage(type, message):
        msg = QMessageBox()
        msg.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.LinksAccessibleByMouse)
        msg.setIcon(type)

        # because of the bug: https://bugreports.qt.io/browse/QTBUG-48964
        # we'll convert a message to HTML format to avoid bolded font on Mac platform
        if message.find('<html') < 0:
            message = '<html style="font-weight:normal">' + message.replace('\n', '<br>') + '</html>'

        msg.setText(message)
        return msg.exec_()

    @staticmethod
    def errorMsg(message):
        if threading.current_thread() != threading.main_thread():
            return WndUtils.callFunInTheMainThread(WndUtils.displayMessage, QMessageBox.Critical, message)
        else:
            return WndUtils.displayMessage(QMessageBox.Critical, message)

    @staticmethod
    def warnMsg(message):
        if threading.current_thread() != threading.main_thread():
            return WndUtils.callFunInTheMainThread(WndUtils.displayMessage, QMessageBox.Warning, message)
        else:
            return WndUtils.displayMessage(QMessageBox.Warning, message)

    @staticmethod
    def infoMsg(message):
        if threading.current_thread() != threading.main_thread():
            return WndUtils.callFunInTheMainThread(WndUtils.displayMessage, QMessageBox.Information, message)
        else:
            return WndUtils.displayMessage(QMessageBox.Information, message)

    @staticmethod
    def queryDlg(message, buttons=QMessageBox.Ok | QMessageBox.Cancel, default_button=QMessageBox.Ok,
            icon=QMessageBox.Information):

        def dlg(message, buttons, default_button, icon):
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setTextInteractionFlags(
                Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.LinksAccessibleByMouse)

            # because of the bug: https://bugreports.qt.io/browse/QTBUG-48964
            # we'll convert a message to HTML format to avoid bolded font on Mac platform
            if message.find('<html') < 0:
                message = '<html style="font-weight:normal">' + message.replace('\n', '<br>') + '</html>'

            msg.setText(message)
            msg.setStandardButtons(buttons)
            msg.setDefaultButton(default_button)
            return msg.exec_()

        if threading.current_thread() != threading.main_thread():
            return WndUtils.callFunInTheMainThread(dlg, message, buttons, default_button, icon)
        else:
            return dlg(message, buttons, default_button, icon)

    def centerByWindow(self, parent):
        """
        Centers this window by window given by attribute 'center_by_window'
        :param center_by_window: Reference to (parent) window by wich this window will be centered.
        :return: None
        """
        self.move(parent.frameGeometry().topLeft() + parent.rect().center() - self.rect().center())

    @staticmethod
    def threadFunctionDialog(worker_fun, worker_fun_args, close_after_finish=True, buttons=None, title='',
                             text=None, center_by_window=None):
        """
        Executes worker_fun function inside a thread. Function provides a dialog for UI feedback (messages 
        and/or progressbar).
        :param worker_fun: user's method/function to be executed inside a thread 
        :param worker_fun_args:  argumets passed to worker_fun
        :param close_after_finish: True, if a dialog is to be closed after finishing worker_fun
        :param buttons: list of dialog button definitions; look at doc od whd_thread_fun.Ui_ThreadFunDialog class
        :return: value returned from worker_fun
        """
        ui = ThreadFunDlg(worker_fun, worker_fun_args, close_after_finish,
                          buttons=buttons, title=title, text=text, center_by_window=center_by_window)
        ui.exec_()
        ret = ui.getResult()
        ret_exception = ui.worker_exception
        del ui
        if ret_exception:
            # if there was an exception in the worker function, pass it to the caller
            raise ret_exception
        return ret

    @staticmethod
    def runInThread(worker_fun, worker_fun_args, on_thread_finish=None, on_thread_exception=None,
                    skip_raise_exception=False):
        """
        Run a function inside a thread.
        :param worker_fun: reference to function to be executed inside a thread
        :param worker_fun_args: arguments passed to a thread function
        :param on_thread_finish: function to be called after thread finishes its execution
        :param skip_raise_exception: Exception raised inside the 'worker_fun' will be passed to the calling thread if:
            - on_thread_exception is a valid function (it's exception handler)
            - skip_raise_exception is False
        :return: reference to a thread object
        """
        thread = None

        def on_thread_finished_int():
            logging.debug('Finished WorkerThread for: ' + str(worker_fun))
            if thread.worker_exception:
                if on_thread_exception:
                    on_thread_exception(thread.worker_exception)
                else:
                    if not skip_raise_exception:
                        raise thread.worker_exception
            else:
                if on_thread_finish:
                    on_thread_finish()

        if threading.current_thread() != threading.main_thread():
            # starting thread from another thread causes an issue of not passing arguments'
            # values to on_thread_finished_int function, so on_thread_finish is not called
            st = traceback.format_stack()
            logging.error('Running thread from inside another thread. Stack: \n' + ''.join(st))

        thread = WorkerThread(worker_fun=worker_fun, worker_fun_args=worker_fun_args)
        thread.finished.connect(on_thread_finished_int)
        thread.start()
        logging.debug('Started WorkerThread for: ' + str(worker_fun))
        return thread

    @staticmethod
    def callFunInTheMainThread(fun_to_call, *args):
        return thread_wnd_utils.callFunInTheMainThread(fun_to_call, *args)

    def setIcon(self, widget, ico):
        if isinstance(ico, str):
            icon = QIcon()
            icon.addPixmap(QPixmap(os.path.join(self.app_config.app_path if self.app_config else '', "img/" + ico)))
        else:
            icon = self.style().standardIcon(ico)
        widget.setIcon(icon)

    def set_cache_value(self, name, value):
        app_cache.set_value(self.__class__.__name__ + '_' + name, value)

    def get_cache_value(self, name, default_value, type):
        return app_cache.get_value(self.__class__.__name__ + '_' + name, default_value, type)

    def open_file_query(self, message, directory='', filter='', initial_filter=''):
        """
        Creates an open file dialog for selecting a file or if the user configures not to use graphical dialogs
          (on some linuxes there are problems with graphic libs and app crashes) - normal input dialog for entering
          the full path to the file opens instead.
        :param message:
        :param directory:
        :param filter: example: "All Files (*);;Conf files (*.conf)"
        :param initial_filter: example: "Conf files (*.conf)"
        :return:
        """
        sip_dialog = self.app_config.dont_use_file_dialogs if self.app_config else False
        file_name = ''

        if sip_dialog:
            file_name, ok = QInputDialog.getText(self, 'File name query', message)
            if not ok:
                file_name = ''
        else:
            file = QFileDialog.getOpenFileName(self,
                                                   caption=message,
                                                   directory=directory,
                                                   filter=filter,
                                                   initialFilter=initial_filter)
            if len(file) >= 2:
                file_name = file[0]
        return file_name

    def save_file_query(self, message, directory='', filter='', initial_filter=''):
        """
        Creates an open file dialog for selecting a file or if the user configures not to use graphical dialogs
          (on some linuxes there are problems with graphic libs and app crashes) - normal input dialog for entering
          the full path to the file opens instead.
        :param message:
        :param directory:
        :param filter: example: "All Files (*);;Conf files (*.conf)"
        :param initial_filter: example: "Conf files (*.conf)"
        :return:
        """
        sip_dialog = self.app_config.dont_use_file_dialogs if self.app_config else False
        file_name = ''

        if sip_dialog:
            file_name, ok = QInputDialog.getText(self, 'File name query', message)
            if not ok:
                file_name = ''
        else:
            file = QFileDialog.getSaveFileName(self,
                                                   caption=message,
                                                   directory=directory,
                                                   filter=filter,
                                                   initialFilter=initial_filter)
            if len(file) >= 2:
                file_name = file[0]
        return file_name

    def write_csv_row(self, file_ptr, elems):
        """ Writes list of values as a CSV row, converting values as cencessary (if value contains a character used
        as a CSV ddelimiter).  """

        delim = self.app_config.csv_delimiter if self.app_config else ';'
        delim_replacement = '_' if delim != '_' else '-'
        # elems = [str(elem if elem is not None else '').replace(delim, delim_replacement) for elem in elems]
        csv_row = []
        for elem in elems:
            if elem is None:
                elem = ''
            elif not isinstance(elem, str):
                elem = QLocale.toString(self.app_config.get_default_locale(), elem if elem is not None else '')
            csv_row.append(elem.replace(delim, delim_replacement))
        file_ptr.write(delim.join(csv_row) + '\n')


class DeadlockException(Exception):
    pass


class CloseDialogException(Exception):
    """ Raised when all processes executed inside a dialog must be aborted, because the dialog is being closing. """
    pass


class ThreadWndUtils(QObject):
    """
    Helps in calling functions interacting with GUI, executed from threads other than the main app's thread.
    """

    # signal for calling specified function in the main thread
    fun_call_signal = QtCore.pyqtSignal(object, object, object)

    def __init__(self):
        QObject.__init__(self)
        self.fun_call_signal.connect(self.funCallSignalled)
        self.fun_call_ret_value = None
        self.fun_call_exception = None

    def funCallSignalled(self, fun_to_call, args, mutex):
        """
        Function-event executed in the main thread as a result of emiting signal fun_call_signal from BG threads.
        :param fun_to_call: ref to a function which is to be called
        :param args: args passed to the function fun_to_call
        :param mutex: mutex object (QMutex) which is used in the calling thread to wait until
            function 'fun_to_call' terminates; calling mutex.unlock() will signal that
        :return: return value from fun_to_call
        """
        try:
            self.fun_call_ret_value = fun_to_call(*args)
        except Exception as e:
            logging.exception('ThreadWndUtils.funCallSignal error: %s' % str(e))
            self.fun_call_exception = e
        finally:
            mutex.unlock()

    def callFunInTheMainThread(self, fun_to_call, *args):
        """
        This method is called from BG threads. Its purpose is to run 'fun_to_call' from main thread (used for dialogs)
        and return values ruturned from it.
        :param fun_to_call: ref to a function which is to be called
        :param args: args passed to the function fun_to_call
        :return: return value from fun_to_call
        """
        exception_to_rethrow = None
        ret = None
        try:
            if threading.current_thread() != threading.main_thread():

                # check whether the main thread waits for the lock acquired by the current thread
                # if so, raise deadlock detected exception
                dl_check = thread_utils.EnhRLock.detect_deadlock(threading.main_thread())
                if dl_check is not None:

                    # find a caller of the current method (skip callers from the current module)
                    caller_file = ''
                    caller_line = ''
                    for si in reversed(traceback.extract_stack()):
                        if si.name != 'callFunInTheMainThread':
                            caller_file = si.filename
                            caller_line = si.lineno
                            break
                    raise DeadlockException('Deadlock detected. Trying to synchronize with the main thread (c), which '
                                            'is waiting (b) for a lock acquired by this thread (a).\n'
                                            '  CURRENT_THREAD ->(a)[LOCK]--->(c)[MAIN_THREAD]\n'
                                            '  MAIN_THREAD ---->(b)[LOCK]\n'
                                            '    a. file "%s", line %s\n'
                                            '    b. file "%s", line %s\n'
                                            '    c. file "%s", line %s' %
                                            (dl_check[2], dl_check[3], dl_check[0], dl_check[1], caller_file,
                                             caller_line))

                mutex = QtCore.QMutex()
                mutex.lock()
                locked = False
                try:
                    self.fun_call_exception = None
                    self.fun_call_ret_value = None

                    # emit signal to call the function fun in the main thread
                    self.fun_call_signal.emit(fun_to_call, args, mutex)

                    # wait for the function to finish; lock will be successful only when the first lock
                    # made a few lines above is released in the funCallSignalled method
                    tm_begin = time.time()
                    locked = mutex.tryLock(3600000)  # wait 1h max
                    tm_diff = time.time() - tm_begin
                    if not locked:
                        logging.exception("Problem communicating with the main thread - couldn't lock mutex. Lock "
                                          "wait time: %ss." % str(tm_diff))
                        raise Exception("Problem communicating with the main thread - couldn't lock mutex. Lock "
                                        "wait time: %ss." % str(tm_diff))
                    ret = self.fun_call_ret_value
                finally:
                    if locked:
                        mutex.unlock()
                    del mutex
                if self.fun_call_exception:
                    # if there was an exception in the fun, pass it to the calling code
                    exception_to_rethrow = self.fun_call_exception
            else:
                return fun_to_call(*args)
        except DeadlockException:
            raise
        except Exception as e:
            logging.exception('ThreadWndUtils.callFunInTheMainThread error: %s' % str(e))
            raise

        if exception_to_rethrow:
            raise exception_to_rethrow
        return ret


thread_wnd_utils = ThreadWndUtils()


class WaitWidget(QWidget):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)
        self.timer_id = None

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.setPen(QPen(Qt.NoPen))

        for i in range(6):
            if self.counter % 6 == i:
                painter.setBrush(QBrush(QColor(0, 0, 0)))
            else:
                painter.setBrush(QBrush(QColor(200, 200, 200)))
            painter.drawEllipse(
                self.width() / 2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
                self.height() / 2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
                20, 20)

        painter.end()

    def showEvent(self, event):

        self.timer_id = self.startTimer(200)
        self.counter = 0

    def timerEvent(self, event):
        self.counter += 1
        self.update()

    def hideEvent(self, event):
        if self.timer_id:
            self.killTimer(self.timer_id)
            self.timer_id = None

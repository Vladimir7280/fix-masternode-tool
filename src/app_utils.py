#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Bertrand256
# Created on: 2017-10
import decimal
from functools import partial
import hashlib
import os
import re
import base64
import binascii
import datetime
from typing import Optional, List, Tuple, ByteString, BinaryIO, Callable
from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QMessageBox, QMenu, QAction
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from dash_utils import read_varint_from_buf, num_to_varint, read_varint_from_file


class SHA256(object):
    new = hashlib.sha256


def extract_app_version(lines):
    """
    Extracts version string from array of lines (content of version.txt file)
    :param lines:
    :return: version string
    """
    for line in lines:
        parts = [elem.strip() for elem in line.split('=')]
        if len(parts) == 2 and parts[0].lower() == 'version_str':
            return parts[1].strip("'")
    return ''


def version_str_to_number(version_str):
    elems = version_str.split('.')
    if elems:
        # last element of a version string can have a suffix
        last_elem = elems[len(elems) - 1]
        if not last_elem.isdigit():
            res = re.findall(r'^\d+', last_elem)
            if res:
                elems[len(elems) - 1] = res[0]
            else:
                del elems[len(elems) - 1]

    ver_list = [n.zfill(4) for n in elems]
    version_nr_str = ''.join(ver_list)
    version_nr = int(version_nr_str)
    return version_nr


def write_bytes_buf(data: ByteString) -> bytearray:
    return num_to_varint(len(data)) + data


def write_int_list_buf(data: List[int]) -> bytearray:
    ret_data = num_to_varint(len(data))
    for item in data:
        ret_data += num_to_varint(item)
    return ret_data


def read_bytes_from_buf(data: ByteString, offset) -> Tuple[bytearray, int]:
    data_len, offset = read_varint_from_buf(data, offset)
    if offset + data_len >= len(data):
        raise ValueError('Corrupted data found.')
    return data[offset: offset + data_len], offset + data_len


def read_bytes_from_file(fptr: BinaryIO) -> bytes:
    data_len = read_varint_from_file(fptr)
    data = fptr.read(data_len)
    if len(data) < data_len:
        raise ValueError('File end before read completed.')
    return data


def read_int_list_from_buf(data: ByteString, offset) -> Tuple[List[int], int]:
    elems = []
    elems_count, offset = read_varint_from_buf(data, offset)
    for idx in range(elems_count):
        elem, offset = read_varint_from_buf(data, offset)
        elems.append(elem)
    return elems, offset


def read_int_list_from_file(fptr: BinaryIO) -> List[int]:
    elems = []
    elems_count = read_varint_from_file(fptr)
    for idx in range(elems_count):
        elem = read_varint_from_file(fptr)
        elems.append(elem)
    return elems


def encrypt(input_str, key, iterations=100000):
    """Basic encryption with a predefined key. Its purpose is to protect not very important data, just to avoid
    saving them as plaintext."""

    salt = b'D9\x82\xbfSibW(\xb1q\xeb\xd1\x84\x118'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(key.encode('utf-8')))
    fer = Fernet(key)
    h = fer.encrypt(input_str.encode('utf-8'))
    h = h.hex()
    return h


def decrypt(input_str, key, iterations=100000):
    try:
        input_str = binascii.unhexlify(input_str)
        salt = b'D9\x82\xbfSibW(\xb1q\xeb\xd1\x84\x118'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(key.encode('utf-8')))
        fer = Fernet(key)
        h = fer.decrypt(input_str)
        h = h.decode('utf-8')
    except:
        return ''
    return h


def seconds_to_human(number_of_seconds, out_seconds=True, out_minutes=True, out_hours=True, out_weeks=True,
                     out_days=True):
    """
    Converts number of seconds to string representation.
    :param out_seconds: False, if seconds part in output is to be trucated
    :param number_of_seconds: number of seconds.
    :return: string representation of time delta
    """
    human_strings = []

    weeks = 0
    days = 0
    hours = 0
    if out_weeks and number_of_seconds > 604800:
        # weeks
        weeks = int(number_of_seconds / 604800)
        number_of_seconds = number_of_seconds - (weeks * 604800)
        elem_str = str(int(weeks)) + ' week'
        if weeks > 1:
            elem_str += 's'
        human_strings.append(elem_str)

    if out_days and number_of_seconds > 86400:
        # days
        days = int(number_of_seconds / 86400)
        number_of_seconds = number_of_seconds - (days * 86400)
        elem_str = str(int(days)) + ' day'
        if days > 1:
            elem_str += 's'
        human_strings.append(elem_str)

    if out_hours and number_of_seconds > 3600:
        hours = int(number_of_seconds / 3600)
        number_of_seconds = number_of_seconds - (hours * 3600)
        elem_str = str(int(hours)) + ' hour'
        if hours > 1:
            elem_str += 's'
        human_strings.append(elem_str)

    if out_minutes and number_of_seconds > 60:
        minutes = int(number_of_seconds / 60)
        number_of_seconds = number_of_seconds - (minutes * 60)
        elem_str = str(int(minutes)) + ' minute'
        if minutes > 1:
            elem_str += 's'
        human_strings.append(elem_str)

    if out_seconds and number_of_seconds >= 1:
        elem_str = str(int(number_of_seconds)) + ' second'
        if number_of_seconds > 1:
            elem_str += 's'
        human_strings.append(elem_str)

    return ' '.join(human_strings)


def get_default_locale():
    return QLocale.system()


ctx = decimal.Context()
ctx.prec = 20


def to_string(data):
    """ Converts date/datetime or number to string using the current locale.
    """

    if isinstance(data, datetime.datetime):
        return get_default_locale().toString(data, get_default_locale().dateTimeFormat(QLocale.ShortFormat))
    elif isinstance(data, datetime.date):
        return get_default_locale().toString(data, get_default_locale().dateFormat(QLocale.ShortFormat))
    elif isinstance(data, float):
        # don't use QT float to number conversion due to weird behavior
        dp = get_default_locale().decimalPoint()
        ret_str = format(ctx.create_decimal(repr(data)), 'f')
        if dp != '.':
            ret_str.replace('.', dp)
        return ret_str
    elif isinstance(data, decimal.Decimal):
        dp = get_default_locale().decimalPoint()
        ret_str = format(data, 'f')
        if dp != '.':
            ret_str.replace('.', dp)
        return ret_str
    elif isinstance(data, str):
        return data
    elif isinstance(data, int):
        return str(data)
    elif data is None:
        return None
    else:
        raise Exception('Argument is not a datetime type')


def update_mru_menu_items(mru_file_list: List[str], mru_menu: QMenu,
                          file_open_action: Callable[[str], None],
                          current_file_name: str,
                          clear_all_actions: Callable[[None], None] = None):

    # look for a separator below the item list
    act_separator = None
    act_clear = None
    for act in mru_menu.actions():
        if act.isSeparator():
            act_separator = act
        elif act.data() == 'clearall':
            act_clear = act
        if act_clear and act_separator:
            break

    if not act_separator:
        act_separator = mru_menu.addSeparator()
    if not act_clear:
        if clear_all_actions:
            act_clear = mru_menu.addAction('Clear all')
            act_clear.setData('clearall')
            act_clear.triggered.connect(clear_all_actions)
            act_clear.setVisible(len(mru_file_list) > 0)
    else:
        act_clear.setVisible(clear_all_actions is not None and len(mru_file_list) > 0)

    action_idx = -1
    home_dir = os.path.expanduser('~')
    for idx, file_name in enumerate(mru_file_list):
        if file_name.find(home_dir) == 0:
            short_file_name = '~' + file_name[len(home_dir):]
        else:
            short_file_name = file_name

        action_idx += 1
        if action_idx < len(mru_menu.actions()) and not mru_menu.actions()[action_idx].isSeparator():
            act = mru_menu.actions()[action_idx]
            act.setText(short_file_name)
        else:
            act = QAction(short_file_name, mru_menu)
            mru_menu.insertAction(act_separator, act)
        act.triggered.disconnect()
        act.triggered.connect(partial(file_open_action, file_name))
        act.setVisible(True)
        act.setCheckable(True)
        if file_name == current_file_name:
            act.setChecked(True)
        else:
            act.setChecked(False)

    # hide all unused actions
    action_idx += 1
    for idx in range(action_idx, len(mru_menu.actions())):
        act = mru_menu.actions()[idx]
        if not (act.isSeparator() or act.data() == 'clearall'):
            act.setVisible(False)

    mru_menu.update()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Isomer - The distributed application framework
# ==============================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""

Schema: File
===========

Contains
--------

Systemwide File definition

See also
--------

Provisions


"""

from isomer.schemata.defaultform import editbuttons
from isomer.schemata.base import base_object, uuid_object

# Basic File definitions

FileSchema = base_object('file', all_roles='crew')

FileSchema['properties'].update({
    'type': {'type': 'string', 'enum': ['file', 'folder', 'link']},
    'special': {'type': 'string'},
    'hash': {'type': 'string'},
    'size': {'type': 'number'},
    'mtime': {'type': 'number'},
    'path': {'type': 'string'},
    'volume': uuid_object(display=False)
})

FileEditForm = [
    'name',
    'directory',
    'special',
    'size',
    editbuttons
]

File = {'schema': FileSchema, 'form': FileEditForm}

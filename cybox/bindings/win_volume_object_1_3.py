#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Nov 06 14:04:33 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import volume_object_1_3
import cybox_common_types_1_0

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    if Verbose_import_:
        print 'Error: LXML version 2.3+ required for parsing files'

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class WindowsVolumeAttributesListType(GeneratedsSuper):
    """A list of attributes describing this windows volume."""
    subclass = None
    superclass = None
    def __init__(self, Attribute=None):
        if Attribute is None:
            self.Attribute = []
        else:
            self.Attribute = Attribute
    def factory(*args_, **kwargs_):
        if WindowsVolumeAttributesListType.subclass:
            return WindowsVolumeAttributesListType.subclass(*args_, **kwargs_)
        else:
            return WindowsVolumeAttributesListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attribute(self): return self.Attribute
    def set_Attribute(self, Attribute): self.Attribute = Attribute
    def add_Attribute(self, value): self.Attribute.append(value)
    def insert_Attribute(self, index, value): self.Attribute[index] = value
    def validate_WindowsVolumeAttributeType(self, value):
        # Validate type WindowsVolumeAttributeType, a restriction on None.
        pass
    def export(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributesListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsVolumeAttributesListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributesListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributesListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attribute_ in self.Attribute:
            Attribute_.export(outfile, level, 'WinVolumeObj:', name_='Attribute', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Attribute
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='WindowsVolumeAttributesListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Attribute=[\n')
        level += 1
        for Attribute_ in self.Attribute:
            showIndent(outfile, level)
            outfile.write('model_.WindowsVolumeAttributeType(\n')
            Attribute_.exportLiteral(outfile, level, name_='WindowsVolumeAttributeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attribute':
            obj_ = WindowsVolumeAttributeType.factory()
            obj_.build(child_)
            self.Attribute.append(obj_)
# end class WindowsVolumeAttributesListType

class WindowsVolumeAttributeType(cybox_common_types_1_0.BaseObjectAttributeType):
    """WindowsVolumeAttributeType specifies Windows volume attributes via a
    union of the WindowsVolumeAttributeEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common_types_1_0.BaseObjectAttributeType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    element."""
    subclass = None
    superclass = cybox_common_types_1_0.BaseObjectAttributeType
    def __init__(self, end_range=None, pattern_type=None, has_changed=None, value_set=None, datatype='String', refanging_transform=None, refanging_transform_type=None, appears_random=None, trend=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, obfuscation_algorithm_ref=None, start_range=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(WindowsVolumeAttributeType, self).__init__(end_range, pattern_type, has_changed, value_set, datatype, refanging_transform, refanging_transform_type, appears_random, trend, defanging_algorithm_ref, is_obfuscated, regex_syntax, obfuscation_algorithm_ref, start_range, idref, is_defanged, id, condition, valueOf_, )
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if WindowsVolumeAttributeType.subclass:
            return WindowsVolumeAttributeType.subclass(*args_, **kwargs_)
        else:
            return WindowsVolumeAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsVolumeAttributeType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributeType'):
        super(WindowsVolumeAttributeType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsVolumeAttributeType')
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            outfile.write(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributeType', fromsubclass_=False, pretty_print=True):
        super(WindowsVolumeAttributeType, self).exportChildren(outfile, level, 'WinVolumeObj:', name_, True, pretty_print=pretty_print)
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(WindowsVolumeAttributeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='WindowsVolumeAttributeType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            showIndent(outfile, level)
            outfile.write('datatype = %s,\n' % (self.datatype,))
        super(WindowsVolumeAttributeType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(WindowsVolumeAttributeType, self).exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            self.datatype = value
        super(WindowsVolumeAttributeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class WindowsVolumeAttributeType

class WindowsDriveType(cybox_common_types_1_0.BaseObjectAttributeType):
    """WindowsDriveType specifies Windows drive types via a union of the
    WindowsDriveTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common_types_1_0.BaseObjectAttributeType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified element."""
    subclass = None
    superclass = cybox_common_types_1_0.BaseObjectAttributeType
    def __init__(self, end_range=None, pattern_type=None, has_changed=None, value_set=None, datatype='String', refanging_transform=None, refanging_transform_type=None, appears_random=None, trend=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, obfuscation_algorithm_ref=None, start_range=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(WindowsDriveType, self).__init__(end_range, pattern_type, has_changed, value_set, datatype, refanging_transform, refanging_transform_type, appears_random, trend, defanging_algorithm_ref, is_obfuscated, regex_syntax, obfuscation_algorithm_ref, start_range, idref, is_defanged, id, condition, valueOf_, )
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if WindowsDriveType.subclass:
            return WindowsDriveType.subclass(*args_, **kwargs_)
        else:
            return WindowsDriveType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsDriveType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsDriveType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsDriveType'):
        super(WindowsDriveType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsDriveType')
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            outfile.write(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsDriveType', fromsubclass_=False, pretty_print=True):
        super(WindowsDriveType, self).exportChildren(outfile, level, 'WinVolumeObj:', name_, True, pretty_print=pretty_print)
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(WindowsDriveType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='WindowsDriveType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            showIndent(outfile, level)
            outfile.write('datatype = %s,\n' % (self.datatype,))
        super(WindowsDriveType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(WindowsDriveType, self).exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            self.datatype = value
        super(WindowsDriveType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class WindowsDriveType

class WindowsVolumeObjectType(volume_object_1_3.VolumeObjectType):
    """The WindowsVolumeObjectType type is intended to characterize Windows
    disk volumes."""
    subclass = None
    superclass = volume_object_1_3.VolumeObjectType
    def __init__(self, object_reference=None, is_mounted=None, Name=None, Device_Path=None, File_System_Type=None, Total_Allocation_Units=None, Sectors_Per_Allocation_Unit=None, Bytes_Per_Sector=None, Actual_Available_Allocation_Units=None, Creation_Time=None, File_System_Flag_List=None, Serial_Number=None, Attributes_List=None, Drive_Letter=None, Drive_Type=None):
        super(WindowsVolumeObjectType, self).__init__(object_reference, is_mounted, Name, Device_Path, File_System_Type, Total_Allocation_Units, Sectors_Per_Allocation_Unit, Bytes_Per_Sector, Actual_Available_Allocation_Units, Creation_Time, File_System_Flag_List, Serial_Number, )
        self.Attributes_List = Attributes_List
        self.Drive_Letter = Drive_Letter
        self.Drive_Type = Drive_Type
    def factory(*args_, **kwargs_):
        if WindowsVolumeObjectType.subclass:
            return WindowsVolumeObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsVolumeObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attributes_List(self): return self.Attributes_List
    def set_Attributes_List(self, Attributes_List): self.Attributes_List = Attributes_List
    def get_Drive_Letter(self): return self.Drive_Letter
    def set_Drive_Letter(self, Drive_Letter): self.Drive_Letter = Drive_Letter
    def validate_StringObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.StringObjectAttributeType, a restriction on None.
        pass
    def get_Drive_Type(self): return self.Drive_Type
    def set_Drive_Type(self, Drive_Type): self.Drive_Type = Drive_Type
    def validate_WindowsDriveType(self, value):
        # Validate type WindowsDriveType, a restriction on None.
        pass
    def export(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsVolumeObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsVolumeObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsVolumeObjectType'):
        super(WindowsVolumeObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='WindowsVolumeObjectType')
    def exportChildren(self, outfile, level, namespace_='WinVolumeObj:', name_='WindowsVolumeObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsVolumeObjectType, self).exportChildren(outfile, level, 'WinVolumeObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Attributes_List is not None:
            self.Attributes_List.export(outfile, level, 'WinVolumeObj:', name_='Attributes_List', pretty_print=pretty_print)
        if self.Drive_Letter is not None:
            self.Drive_Letter.export(outfile, level, 'WinVolumeObj:', name_='Drive_Letter', pretty_print=pretty_print)
        if self.Drive_Type is not None:
            self.Drive_Type.export(outfile, level, 'WinVolumeObj:', name_='Drive_Type', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Attributes_List is not None or
            self.Drive_Letter is not None or
            self.Drive_Type is not None or
            super(WindowsVolumeObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='WindowsVolumeObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(WindowsVolumeObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(WindowsVolumeObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Attributes_List is not None:
            showIndent(outfile, level)
            outfile.write('Attributes_List=model_.WindowsVolumeAttributesListType(\n')
            self.Attributes_List.exportLiteral(outfile, level, name_='Attributes_List')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Drive_Letter is not None:
            showIndent(outfile, level)
            outfile.write('Drive_Letter=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Drive_Letter.exportLiteral(outfile, level, name_='Drive_Letter')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Drive_Type is not None:
            showIndent(outfile, level)
            outfile.write('Drive_Type=model_.WindowsDriveType(\n')
            self.Drive_Type.exportLiteral(outfile, level, name_='Drive_Type')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsVolumeObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attributes_List':
            obj_ = WindowsVolumeAttributesListType.factory()
            obj_.build(child_)
            self.set_Attributes_List(obj_)
        elif nodeName_ == 'Drive_Letter':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Drive_Letter(obj_)
        elif nodeName_ == 'Drive_Type':
            obj_ = WindowsDriveType.factory()
            obj_.build(child_)
            self.set_Drive_Type(obj_)
        super(WindowsVolumeObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsVolumeObjectType

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Volume'
        rootClass = WindowsVolumeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Volume'
        rootClass = WindowsVolumeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Windows_Volume",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Volume'
        rootClass = WindowsVolumeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('import temp as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "WindowsVolumeObjectType",
    "WindowsVolumeAttributesListType",
    "WindowsDriveType",
    "WindowsVolumeAttributeType"
    ]
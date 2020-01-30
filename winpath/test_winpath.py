# -*- coding: utf-8 -*-

import unittest
from winpath import winpath


class TestWinpath(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_detect(self):
        """Test path detection"""
        tp = winpath.PathType
        tests = (
            (r'any', tp.ANY),
            (r'path/to', tp.POSIX),
            (r'path\to', tp.WINDOWS),
            (r'/path', tp.POSIX),
            (r'\path', tp.WINDOWS),
            (r'path/', tp.POSIX),
            ('path\\', tp.WINDOWS),
            (r'\\path', tp.WINDOWS),
            (r'/日本語', tp.POSIX),
            (r'\日本語', tp.WINDOWS),
            (r'/ ', tp.POSIX),
            (r'\ ', tp.WINDOWS),
            (r'/ abc', tp.POSIX),
            (r'\ abc', tp.WINDOWS),
            (r'~/', tp.POSIX),
            (r'~', tp.ANY),
        )
        for p, e in tests:
            self.assertEqual(winpath.detect(p), e)

    def test_convert_each_other(self):
        """Test path convert"""
        tests = (
            # (windows, posix)
            (r'\a\b\c', '/a/b/c'),
            (r'\\drive\a\b', '//drive/a/b'),
            (r'\\192.168.0.1\a\b', '//192.168.0.1/a/b'),
        )
        for w, l in tests:
            self.assertEqual(winpath.to_posix(w), l)
            self.assertEqual(winpath.to_posix(w + '\\'), l + '/')
            self.assertEqual(winpath.to_windows(l), w)
            self.assertEqual(winpath.to_windows(l + '/'), w + '\\')

    def test_convert_static_c(self):
        """Test path convert C: drive"""
        tp = winpath.PathType
        mappings = [[
            {'type': tp.WINDOWS, 'prefix': 'c:'},
            {'type': tp.POSIX, 'prefix': '/mnt/c'}
        ]]
        tests = (
            ('c:', '/mnt/c'),
            (r'c:\hoge', r'/mnt/c\hoge'),
        )
        for t, e in tests:
            self.assertEqual(winpath.convert_static(t, tp.POSIX, mappings), e)
            self.assertEqual(winpath.convert_static(e, tp.WINDOWS, mappings), t)

    def test_convert_static_samba(self):
        """Test path convert Samba"""
        tp = winpath.PathType
        mappings = [[
            {'type': tp.WINDOWS, 'prefix': r'\\'},
            {'type': tp.POSIX, 'prefix': 'smb://'}
        ]]
        tests = (
            (r'\\', 'smb://'),
            (r'\\server', 'smb://server'),
            (r'\\192.168.0.10', 'smb://192.168.0.10'),
        )
        for t, e in tests:
            self.assertEqual(winpath.convert_static(t, tp.POSIX, mappings), e)
            self.assertEqual(winpath.convert_static(e, tp.WINDOWS, mappings), t)


if __name__ == '__main__':
    unittest.main()

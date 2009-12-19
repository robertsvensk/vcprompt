import os
import unittest
import vcprompt

class Base(unittest.TestCase):
    def repo(self, vcs):
        return './tests/repositories/%s' % vcs

class TestGit(Base):
    def setUp(self):
        self.repository = self.repo('git')

    def test_format_branch(self):
        string = vcprompt.vcprompt(self.repository, string="%b")
        self.assertEquals(string, 'master')

    def test_format_revision(self):
        # revision == hash
        return self.test_format_hash()

    def test_format_hash(self):
        string = vcprompt.vcprompt(self.repository, string='%r')
        self.assertEquals(string, 'eae51cf')

    def test_format_system(self):
        string = vcprompt.vcprompt(self.repository, string='%s')
        self.assertEquals(string, 'git')

    def test_format_all(self):
        format = "%s:%b(%r)"
        string = vcprompt.vcprompt(self.repository, string=format)
        self.assertEquals(string, 'git:master(eae51cf)')


class TestMecurial(Base):
    def setUp(self):
        self.repository = self.repo('hg')

    def test_format_branch(self):
        self.fail()

    def test_format_revision(self):
        self.fail()

    def test_format_hash(self):
        self.fail()


class TestBazaar(Base):
    def test_format_branch(self):
        self.fail()

    def test_format_revision(self):
        self.fail()

    def test_format_hash(self):
        self.fail()


class TestSubversion(Base):
    def test_format_branch(self):
        self.fail()

    def test_format_revision(self):
        self.fail()

    def test_format_hash(self):
        return self.test_format_revision()


if __name__ == '__main__':
    unittest.main()

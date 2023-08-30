import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

TIMEOUT=6 * 2 # VM warp factor

@ddt
class Test(testlib.TestCase):
    def do_test(self, matches, k, expected):
        """Test implementation
        - matches:		list of players' plays
        - k:			tournament parameter
        - expected:		expected result
        TIMEOUT: 2 seconds for each test
        """
        matches2 = matches.copy()
        if DEBUG:
                import program01 as program
                result = program.ex(matches, k)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_imports(allowed=['program01','_io']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result = program.ex(matches, k)
        self.assertEqual(matches, matches2,
                         ('You should not change the matches list\n'
                          '[Non dovete modificare l\'argomento matches]'))
        self.assertEqual(type(result), list,
                         ('The output type should be: list\n'
                          '[Il tipo di dato in output deve essere: list]'))
        for p in result:
            self.assertEqual(type(p), int,
                         ('The elements of the output should be: int\n '
                          '[Gli elementi della lista devono essere int.]'))
        self.assertEqual(len(result), len(expected),
                         ('The output list should have '+str(len(expected))+' elements\n'
                          '[La lista deve avere ' +str(len(expected))+' elementi\n'))
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          '[Il valore di ritorno è errato]'))
        return 1

    def test_example3(self):
        matches  = [ "aac","ccc","caa" ]
        k        = 2
        expected = [1, 0, 2]
        return self.do_test(matches, k, expected)

    def test_example3bis(self):
        matches  = [ "ccc", "caa", "aac"]
        k        = 2
        expected = [0, 2, 1]
        return self.do_test(matches, k, expected)

    def test_example4(self):
        matches  = [ "aac","ccc","caa" ]
        k        = 1
        expected = [0, 2, 1]
        return self.do_test(matches, k, expected)

    def test_example4bis(self):
        matches  = [ "ccc","caa","aac" ]
        k        = 1
        expected = [2, 1, 0]
        return self.do_test(matches, k, expected)

    @file_data("test_runic_tie.json")
    def test_runic_tie(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_emojismall_tie.json")
    def test_emojismall_tie(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_emojismall_evil.json")
    def test_emojismall_evil(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_joyokanji_random_tie.json")
    def test_joyokanji_random_tie(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_hiragana_random_tie.json")
    def test_hiragana_random_tie(self, matches, k, expected):
          return self.do_test(matches, k, expected)


    @file_data("test_emoji_random_tie.json")
    def test_emoji_random_tie(self, matches, k, expected):
          return self.do_test(matches, k, expected)

    ######################### SECRET TESTS START HERE! #########################


if __name__ == '__main__':
    Test.main()



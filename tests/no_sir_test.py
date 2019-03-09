import plugins.no_sir


class Test_no_sir(object):
    extra_plugin_dir = '.'

    def test_no_sir(self, testbot):
        testbot.push_message(r'\bsir\b', '\bSir\b', msg.body)
        assert 'Do not use sir in your conversation' in testbot.pop_message()

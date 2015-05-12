import sublime, sublime_plugin, datetime

start_time = datetime.datetime.now()

class StarttimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global start_time 
        start_time = datetime.datetime.now()
        
        start_time_stamp = "// Start Time: %s\t // Timer: 00:00:00\n" % (start_time.strftime("%H:%M:%S"))
        self.view.insert(edit, 0, start_time_stamp)
        self.view.run_command(self.view.id, "timecoder", {"start_time": start_time })
    pass


class TimecoderCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        global start_time
        time = datetime.datetime.now()
        elapsed_time = time - start_time
        s = elapsed_time.seconds
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)

        timestamp = '<%s:%s:%s>\n' % (hours, minutes, seconds)
        self.view.insert(edit, self.view.sel()[0].begin(), timestamp)

        pass
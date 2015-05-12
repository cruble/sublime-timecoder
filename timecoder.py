import sublime, sublime_plugin, datetime

start_time = datetime.datetime.now()

class StarttimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global start_time 
        start_time = datetime.datetime.now()
        
        start_time_stamp = "// Start Time: %s\t // Timer: 00:00:00\n" % (start_time.strftime("%H:%M:%S"))
        # self.view.insert(edit, self.view.sel()[0].begin(), timestamp)
        self.view.insert(edit, 0, start_time_stamp)

        # try:
        #     # line = int(text)
        #     if self.window.active_view():
        #         self.window.active_view().run_command("timecoder", {"start_time": start_time} )
        # except ValueError:
        #     pass

    #     self.view.window().run_command("timecoder", {"start_time": start_time} )
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


# class TimecoderCommand(sublime_plugin.TextCommand):
#   def run(self, edit):
#     val = time().strftime('%Y-%M-%d')
#     self.view.insert(edit, self.view.sel()[0].begin(), val)


        # print '%s:%s:%s' % (hours, minutes, seconds)
        # difference = 
        # timestamp = "-%s-\t" % (datetime.datetime.now().strftime("%H:%M:%S"))
        # timestamp = "-%s-\t" % (elapsed_time.strftime("%H:%M:%S"))


# class TimecoderCommand(sublime_plugin.EventListener):
#     """Expand `isoD`, `now`, `datetime`, `utcnow`, `utcdatetime`, 
#        `date` and `time`
#     """
#     def on_query_completions(self, view, prefix, locations):
#         if prefix in ('isoD', 'now', 'datetime'):
#             val = datetime.now().strftime('%Y-%M-%dT%H:%M:%S')
#         elif prefix in ('utcnow', 'utcdatetime'):
#             val = datetime.utcnow().strftime('%Y-%M-%dT%H:%M:%S')
#         elif prefix == 'date':
#             val = datetime.now().strftime('%Y-%M-%d')
#         elif prefix == 'time':
#             val = datetime.now().strftime('%H:%M:%S')
#         else:
#             val = None
 
#         return [(prefix, prefix, val)] if val else []
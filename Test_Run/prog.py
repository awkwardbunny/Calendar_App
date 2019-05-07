#!/usr/bin/env python3
import tkinter as tk
import pickle
import os.path
import os
import time, datetime
import csv

from datetime import date
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from httplib2 import Http
from oauth2client import file, client, tools

default_font = "Times 16"
secondary_font = "Times 14"

class GCal:

    fn_pickle = 'token.pickle'
    fn_credentials = 'credentials.json'
    service = None
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def check_token_existance(self):
        creds = None
        if os.path.exists(self.fn_pickle):
            with open(self.fn_pickle, 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(fn_credentials, self.SCOPES)
                creds = flow.run_local_server()
            with open(self.fn_pickle, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

    def fetch_events(self, n):
        page_token = None
        id = 'primary'      # defaults to primary calendar
        calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            # print(calendar_list_entry['summary'])
            if calendar_list_entry['summary'] == "TestDev1":     # retrieves the ID of the calendar
                id = calendar_list_entry['id']
                # print(calendar_list_entry['summary'])

        now = datetime.datetime.utcnow().isoformat() + 'Z'
        # print("Fetching {} events.".format(n))
        events_result = self.service.events().list(
            calendarId=id,
            timeMin = now,
            maxResults = n,
            singleEvents = True,
            orderBy = 'startTime'
        ).execute()

        return events_result.get('items', [])

class Window(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        super().grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.master = master
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Find today's date
        self.today = date.today()
        self.new_today = self.today.strftime("%Y-%m-%dT00:00:00-04:00")
        self.default_today = self.today.strftime("%Y-%m-%dT88:88:88-04:00")

        # Create text file
        self.write_file = open("file1.txt", "w+")

        # Set up all frames
        fr_tasks = tk.Frame(self)
        fr_tasks.grid(padx=5, pady=5, row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        fr_today = tk.Frame(self)
        fr_today.grid(padx=5, pady=5, row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        fr_tasks.rowconfigure(0, weight=5)
        fr_tasks.columnconfigure(0, weight=1)

        fr_form = tk.Frame(fr_tasks)
        fr_form.grid(padx=5, pady=5, row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        fr_tasks_list = tk.Frame(fr_tasks)
        fr_tasks_list.grid(padx=5, pady=5, row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        fr_notes = tk.Frame(self)
        fr_notes.grid(padx=5, pady=5, row=1, sticky=tk.N+tk.S+tk.E+tk.W)

        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        # ---------------------------------------------------------------------------
        # Right side - Today tasks
        l_today = tk.Label(fr_today, text='Today', font=default_font)
        l_today.pack(side='top', fill=tk.X)

        scrollbar = tk.Scrollbar(fr_today)
        scrollbar.pack(side='right', fill='y')

        self.lb_today = tk.Listbox(fr_today, yscrollcommand=scrollbar.set, font=secondary_font)
        self.lb_today.pack(fill=tk.BOTH, expand=True)

        # ---------------------------------------------------------------------------
        # Left side - Tasks list
        l_tasks_list = tk.Label(fr_tasks_list, text='Tasks', font=default_font)
        l_tasks_list.pack(side='top', fill=tk.X)

        scrollbar = tk.Scrollbar(fr_tasks_list)
        scrollbar.pack(side='right', fill='y')

        self.lb_tasks = tk.Listbox(fr_tasks_list, yscrollcommand=scrollbar.set, font=secondary_font)
        self.lb_tasks.pack(fill=tk.BOTH, expand=True)

        # ---------------------------------------------------------------------------
        # Entry form
        fr_form.columnconfigure(1, weight=1)

        tk.Label(fr_form, text='TYPE*', font=default_font).grid(row=0, sticky=tk.W+tk.E)
        self.type_input = tk.StringVar(self)
        self.type_input.set("")
        self.om_type = tk.OptionMenu(fr_form, self.type_input, "Event", "Reminder")
        self.om_type.grid(row=0, column=1, sticky=tk.W+tk.E)

        tk.Label(fr_form, text='TASK*', font=default_font).grid(row=1, sticky=tk.W+tk.E)
        self.e_task_name = tk.Entry(fr_form, font=default_font)
        self.e_task_name.grid(row=1, column=1, sticky=tk.W+tk.E)

        tk.Label(fr_form, text='TAGS*', font=default_font).grid(row=2, sticky=tk.W+tk.E)
        self.e_tags = tk.Entry(fr_form, font=default_font)
        self.e_tags.grid(row=2, column=1, sticky=tk.W+tk.E)

        tk.Label(fr_form, text='START', font=default_font).grid(row=3, sticky=tk.W+tk.E)
        self.e_st_time = tk.Entry(fr_form, font=default_font)
        self.e_st_time.grid(row=3, column=1, sticky=tk.W+tk.E)

        tk.Label(fr_form, text='END', font=default_font).grid(row=4, sticky=tk.W+tk.E)
        self.e_end_time = tk.Entry(fr_form, font=default_font)
        self.e_end_time.grid(row=4, column=1, sticky=tk.W+tk.E)

        tk.Button(fr_form, text='OK', command=self.create_event, font=default_font).grid(row=5, sticky=tk.W)
        tk.Button(fr_form, text='Refresh', command=self.update_event, font=default_font).grid(row=5, column=1, sticky=tk.E)

        tk.Label(fr_notes, text='Please note: ', font=default_font).grid(row=0, column=0, sticky=tk.W+tk.N)
        tk.Label(fr_notes, text='* These fields are REQUIRED\n \'Start\' and \'End\' are optional', font=default_font).grid(row=0, column=1, sticky=tk.W)

        # ---------------------------------------------------------------------------
        # Google Calendar object
        self.g = GCal()
        self.g.check_token_existance()
        self.add_events(self.g.fetch_events(20))

    def add_events(self, events):       # from Google Calendar
        for e in events:
            start = e['start'].get('dateTime', e['start'].get('date'))
            end = e['end'].get('dateTime', e['end'].get('date'))
            s = start + '\t' + end + '\t' + e['summary']
            # print(s)
            # Format is XXXX-XX-XX (Year-Month-Day)
            if start[0:10] == '2019-05-08': # self.new_today[0:10]:
                self.lb_today.insert(tk.END, self.get_start_time2(s) + ' - ' + self.get_end_time2(s) + ': ' + e['summary'])
                self.write_file.write(s + '\n')

    def create_event(self):     # from User Input
        s_type = self.type_input.get()
        s_task = self.e_task_name.get()
        s_st_time = self.e_st_time.get()
        s_end_time = self.e_end_time.get()
        self.send_line = ""
        if s_type == "Event":
            s_tags = "#event " + self.e_tags.get()
            if s_st_time != "":
                if s_end_time != "":
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {}) Start time: {}   End time: {}'.format(s_type, s_task, s_tags, s_st_time, s_end_time))
                    self.send_line = self.time_template(s_st_time) + '\t' + self.time_template(s_end_time) + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
                else:
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {}) Start time: {}'.format(s_type, s_task, s_tags, s_st_time))
                    self.send_line = self.time_template(s_st_time) + '\t' + self.default_today + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
            else:
                if s_end_time != "":
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {}) End time: {}'.format(s_type, s_task, s_tags, s_end_time))
                    self.send_line = self.default_today + '\t' + self.time_template(s_end_time) + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
                else:
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {})'.format(s_type, s_task, s_tags))
                    self.send_line = self.default_today + '\t' + self.default_today + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
        else:
            s_tags = "#reminder " + self.e_tags.get()
            if s_st_time != "":
                if s_end_time != "":
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {}) Start time: {}   End time: {}'.format(s_type, s_task, s_tags, s_st_time, s_end_time))
                    self.send_line = self.time_template(s_st_time) + '\t' + self.time_template(s_end_time) + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
                else:
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {}) Start time: {}'.format(s_type, s_task, s_tags, s_st_time))
                    self.send_line = self.time_template(s_st_time) + '\t' + self.default_today + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
            else:
                if s_end_time != "":
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {}) End time: {}'.format(s_type, s_task, s_tags, s_end_time))
                    self.send_line = self.default_today + '\t' + self.time_template(s_end_time) + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
                else:
                    self.lb_tasks.insert(tk.END, '{}: {} (Tag: {})'.format(s_type, s_task, s_tags))
                    self.send_line = self.default_today + '\t' + self.default_today + '\t' + '{}\t(Tag: {}) \n'.format(s_task, s_tags)
        self.write_file.write(self.send_line)
        self.clear_text()

    def update_event(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        # f = open(os.path.join(__location__, 'Makefile'))
        print(__location__)
        os.system("ls")
        # HELP HELP HELP
        os.system('make all')
        #
        os.system('make run')
        #
        # os.system('make clean')

        read_file = open("file2.txt", "r")
        self.delete_event()
        temp = read_file.readlines()
        for x in temp:
            start_time = self.get_start_time2(x)
            end_time = self.get_end_time2(x)
            event_name = self.get_event_name(x)
            returnable = start_time + ' - ' + end_time + ': ' + event_name
            self.lb_today.insert(tk.END, returnable)

    def delete_event(self):
        for i in range(self.lb_today.size()):
            # print(i)
            self.lb_today.delete(0)

    def get_start_time(self, time_string):
        return time_string[11:19]

    def get_end_time(self, time_string):
        return time_string[37:45]

    def get_start_time2(self, time_string):
        return time_string[11:16]

    def get_end_time2(self, time_string):
        return time_string[37:42]

    def get_event_name(self, time_string):
        return time_string[52:len(time_string)-1]

    def time_template(self, time_string):
        return self.today.strftime("%Y-%m-%dT" + time_string + ":00-04:00")

    def clear_text(self):
        self.type_input.set("")
        self.e_task_name.delete(0, 'end')
        self.e_tags.delete(0, 'end')
        self.e_st_time.delete(0, 'end')
        self.e_end_time.delete(0, 'end')

def main():
    root = tk.Tk()
    root.geometry("1100x600")
    root.title("Calendar App")
    app = Window(root)

    root.mainloop()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
import tkinter as tk
import pickle
import os.path
import time, datetime
import csv

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from httplib2 import Http
from oauth2client import file, client, tools

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
            if calendar_list_entry['summary'] == "2019 Spring":     # retrieves the ID of the calendar
                id = calendar_list_entry['id']

        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print("Fetching {} events.".format(n))
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

        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Start adding components
        # ---------------------------------------------------------------------------
        # Right side - Today tasks
        l_today = tk.Label(fr_today, text='Today')
        l_today.pack(side='top', fill=tk.X)

        scrollbar = tk.Scrollbar(fr_today)
        scrollbar.pack(side='right', fill=tk.Y)

        self.lb_tasks = tk.Listbox(fr_today, yscrollcommand=scrollbar.set)
        self.lb_tasks.pack(side='bottom', fill=tk.BOTH, expand=True)
        # ---------------------------------------------------------------------------
        # Left side - Tasks list

        scrollbar = tk.Scrollbar(fr_tasks_list)
        scrollbar.pack(side='right', fill='y')

        self.lb_tasks = tk.Listbox(fr_tasks_list, yscrollcommand=scrollbar.set)
        self.lb_tasks.pack(fill=tk.BOTH, expand=True)
        # ---------------------------------------------------------------------------
        # Entry form
        fr_form.columnconfigure(1, weight=1)
        tk.Label(fr_form, text='TASK').grid(row=0, sticky=tk.W+tk.E)
        self.e_task_name = tk.Entry(fr_form)
        self.e_task_name.grid(row=0, column=1, sticky=tk.W+tk.E)

        tk.Label(fr_form, text='TAGS').grid(row=1, sticky=tk.W+tk.E)
        self.e_tags = tk.Entry(fr_form)
        self.e_tags.grid(row=1, column=1, sticky=tk.W+tk.E)

        tk.Label(fr_form, text='START').grid(row=2, sticky=tk.W+tk.E)
        self.e_st_time = tk.Entry(fr_form)
        self.e_st_time.grid(row=2, column=1, sticky=tk.W+tk.E)

        tk.Label(fr_form, text='END').grid(row=3, sticky=tk.W+tk.E)
        self.e_end_time = tk.Entry(fr_form)
        self.e_end_time.grid(row=3, column=1, sticky=tk.W+tk.E)

        tk.Button(fr_form, text='OK', command=self.create_event).grid(row=4, sticky=tk.W+tk.E)
        # ---------------------------------------------------------------------------
        # Google Calendar object
        self.g = GCal()
        self.g.check_token_existance()
        self.add_events(self.g.fetch_events(20))

    def add_events(self, events):
        for e in events:
            start = e['start'].get('dateTime', e['start'].get('date'))
            end = e['start'].get('dateTime', e['end'].get('date'))
            s = start + '\t' + end + '\t' + e['summary']
            print(s)
            self.lb_tasks.insert(tk.END, e['summary'])

    def create_event(self):
        s_task = self.e_task_name.get()
        s_tags = self.e_tags.get()
        s_st_time = self.e_st_time.get()
        s_end_time = self.e_end_time.get()
        print("Creating a new task '{}' with tags '{}'\nStart: {}\nEnd: {}".format(s_task, s_tags, s_st_time, s_end_time))
        #self.lb_tasks.insert(tk.END, s_task + "\t" + s_tags)
        self.lb_tasks.insert(tk.END, '{} (Tag: {}) '.format(s_task, s_tags))


def main():
    root = tk.Tk()
    root.geometry("00x600")
    root.title("Calendar App")
    app = Window(root)

    root.mainloop()

if __name__ == '__main__':
    main()
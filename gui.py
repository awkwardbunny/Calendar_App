#	Create virtual environment: python3 -m venv ./calapp
#	To go to the virtual environment: source calapp/bin/activate
#	To exit the virtual environment: deactivate

# (1) https://docs.python.org/3/library/tkinter.html#the-window-manager
# (2) https://www.geeksforgeeks.org/python-gui-tkinter/
from __future__ import print_function
import datetime
import time
import pickle
import os.path

import tkinter as tk

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from httplib2 import Http
from oauth2client import file, client, tools

try:
	import argparse
	flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
	flags = None

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
file1 = open("SendFile.txt", "w+")
print(file1)

# --------------------------------------------------------------------
# GUI
class Application(tk.Frame):
	def __init__(self, master = None):
		global file1
		super().__init__(master)
		self.master = master
		self.pack()
		# self.create_widgets()
		# self.results = tk.Label(self)

		tk.Label(self, text="First Name").grid(row=0)
		tk.Label(self, text="Last Name").grid(row=1)
		self.e1 = tk.Entry(self)
		self.e2 = tk.Entry(self)
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		tk.Button(self, text='Quit', command=self.quit).grid(row=3, column=0, sticky='W', pady=4)
		tk.Button(self, text='Show', command=self.show_entry_fields).grid(row=3, column=1, sticky='W', pady=4)


		

	# def create_widgets(self):
	# 	self.hi_there = tk.Button(self)
	# 	self.hi_there["text"] = "Hello World\n(click me)"
	# 	self.hi_there["command"] = self.say_hi
	# 	self.hi_there.pack(side="top")

	# 	self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
	# 	self.quit.pack(side="bottom")

	# def say_hi(self):
	# 	print("hi there, everyone!")

	# def display_text(self, text):
	# 	self.results['text'] += text
	# 	self.results.pack(side="top")

	# def callback():
	# 	print (self.e.get())

	# def makeentry(self, parent, caption, width=None, **options):
	# 	tk.Label(parent, text=caption).pack(side='left')
	# 	entry = tk.Entry(parent, **options)
	# 	if width:
	# 		entry.config(width=width)
	# 	entry.pack(side='left')
	# 	return entry

	def show_entry_fields(self):
		print("First Name: %s\nLast Name: %s" %(self.e1.get(), self.e2.get()))
		file1.write(self.e1.get() + self.e2.get() + '\n')
		file1.flush()


	# def enter_text(self):
	# 	tk.Label(self, text='Task: ').grid(row=0)
	# 	self.e = tk.Entry(self)
	# 	self.e.grid(row=0, column = 1)
	# 	# self.e.pack()
	# 	# self.e.focus_set()

	# 	self.b = tk.Button(self, text="Get", width=25, command=self.callback)
	# 	self.b.pack()
	# 	self.text = self.e.get()

	# 	self.user = self.makeentry(self, "User name:", 10)
	# 	self.password = self.makeentry(self, "Password:", 10, show="*")

	# 	self.content = tk.StringVar()
	# 	self.entry = tk.Entry(self, text='Wheee', textvariable=self.content)

	# 	self.text = self.content.get()
	# 	self.content.set('Wheee')


# -------------------------------------------------------------------
# Deals with Google Calendar Information
class Gstuff:
	def __init__(self):
		pass

	def check_token_existance(self):
		creds = None
		# Checks the file 'token.picke' to see if user's access is already stored
		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				creds = pickle.load(token)
		# Runs if there is no valid credentials
		if not creds or not creds.valid:
			if creds and creds.expired and creds.refresh_token:
				creds.refresh(Request())
			else:
				flow = InstalledAppFlow.from_client_secrets_file(
					'credentials.json', SCOPES)
			# Saves the credentials for the next run
			with open('token.pickle', 'wb') as token:
				pickle.dump(creds, token)
		self.service = build('calendar', 'v3', credentials = creds)

	def something1(self):
		#Call the Calendar API
		now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time zone
		print('Getting the upcoming 10 events')
		events_result = self.service.events().list(calendarId='primary', timeMin=now,
	                                        maxResults=10, singleEvents=True,
	                                        orderBy='startTime').execute()
		events = events_result.get('items', [])
		return events

# -------------------------------------------------------------------
def main():
		# Sets up the GUI
	root = tk.Tk()
	app = Application(master=root)
	global file1
	# (1)
	app.master.title("Print the next ten events")	# Sets the Window Title

	g = Gstuff()
	g.check_token_existance()
	events = g.something1()

	for event in events:
		start = event['start'].get('dateTime', event['start'].get('date'))
		end = event['end'].get('dateTime', event['end'].get('date'))
		yeet = start + '\t' + end + '\t' + event['summary']+'\n'
		print(yeet)
		# app.display_text(yeet)
		file1.write(yeet)
		file1.flush()
	time.sleep(1)
	print("rawwwwwwwwww")
	time.sleep(1)
	# file1.close()
	# app.enter_text()
	app.mainloop()

if __name__ == '__main__':
	main()

# #Enables read/write to Google Calendar
# SCOPES = ['https://www.googleapis.com/auth/calendar']

# #Validates the credentials to give program access
# store = file.Storage('storage.json')
# creds = store.get()
# if not creds or creds.invalid:
# 	flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
# 	creds = tools.run_flow(flow, store, flags) \
# 		if flags else tools.run(flow, store)

# CAL = build('calendar', 'v3', http=creds.authorize(Http()))

# #Set up to push to Google Calendar
# GMT_OFF = '-04:00'		#EST
# EVENT = {
# 	'summary':	"Dinner with friends",
# 	'start':	{'dateTime': '2019-05-28T19:00:00%s' % GMT_OFF},
# 	'end':		{'dateTime': '2019-05-28T20:00:00%s' % GMT_OFF},
# }

# e = GCAL.events().insert(calendarId = 'primary', sendNotifications = True, body = EVENT).execute()

# print('''*** %r event added:
#     Start: %s
#     End:   %s''' % (e['summary'].encode('utf-8'),
#         e['start']['dateTime'], e['end']['dateTime']))
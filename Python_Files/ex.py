# https://www.geeksforgeeks.org/python-gui-tkinter/
import tkinter as tk

class Window(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master = master
		self.pack()

		tk.Label(self, text="First Name").grid(row=0)
		tk.Label(self, text="Last Name").grid(row=1)
		self.e1 = tk.Entry(self)
		self.e2 = tk.Entry(self)
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		tk.Button(self, text='Quit', command=master.quit).grid(row=3, column=0, sticky='W', pady=4)
		tk.Button(self, text='Show', command=self.show_entry_fields).grid(row=3, column=1, sticky='W', pady=4)

	def show_entry_fields(self):
		print("First Name: %s\nLast Name: %s" %(self.e1.get(), self.e2.get()))

def main():
	root = tk.Tk()
	app = Window(master=root)
	app.mainloop()

if __name__ == '__main__':
	main()
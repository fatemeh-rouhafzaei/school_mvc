import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class studentView(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        self.capacity_entry = ttk.Entry(self)
        self.capacity_entry.pack(pady=5)

        add_btn = ttk.Button(self,text="افزودن دانش آموز", command=self.add_student)
        add_btn.pack(pady=5)

        self.student_list = ttk.Treeview(self, columns=("id", "name","nationa_code" ,"password" , "mobile"), show="headings")
        self.student_list.heading("id", text="ID")
        self.student_list.heading("name", text="نام کلاس")
        self.student_list.heading("nationa_code", text="کد ملی")
        self.student_list.heading("password", text="رمز عبور")
        self.student_list.heading("mobile", text="شماره همراه")

        self.student_list.pack(fill="both", expand=True)

        self.refresh_student_list()

    def add_student(self):
        name = self.name_entry.get()
        try:
            capacity = int(self.capacity_entry.get())
            self.controller.create_student(name, capacity)
            self.refresh_student_list()
        except Exception as e:
            Messagebox.show_error(title="خطا", message=str(e))

    def refresh_student_list(self):
        for row in self.student_list.get_children():
            self.student_list.delete(row)
        for cls in self.controller.get_studentes():
            self.student_list.insert("", "end", values=cls)

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class StudentFormView(ttk.Frame):
    def init(self, master):
        super().init(master, padding=20)
        self.pack(fill=BOTH, expand=True)

        # grid 3x2
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(column=0, row=0, sticky= EW, padx=2, pady=5)
        self.name_label = ttk.Label(self, text="نام ").grid(column=1, row=0, sticky= E, padx=10, pady=5)

        # start national code ui
        self.national_code_entry = ttk.Entry(self)
        self.national_code_entry.grid(column=0, row=1, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="کد ملی").grid(column=1, row=1, sticky= E, padx=10, pady=5)
        # end national code ui

        self.mobile_entry = ttk.Entry(self)
        self.mobile_entry.grid(column=0, row=2, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="موبایل").grid(column=1, row=2, sticky= E, padx=10, pady=5)

        self.password_entry = ttk.Entry(self)
        self.password_entry.grid(column=0, row=3, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="رمز ورود").grid(column=1, row=3, sticky= E, padx=10, pady=5)

        # start grade level ui
        self.grade_level_entry = ttk.Entry(self)
        self.grade_level_entry.grid(column=0, row=4, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="پایه تحصیلی").grid(column=1, row=4, sticky= E, padx=10, pady=5)
        # end grade level ui

        # start field of study ui
        self.field_of_study_entry = ttk.Entry(self)
        self.field_of_study_entry.grid(column=0, row=5, sticky= EW, padx=2, pady=5)
        ttk.Label(self, text="رشته تحصیلی").grid(column=1, row=5, sticky= E, padx=10, pady=5)
        # end field of study ui

        self.save_button = ttk.Button(self, text="ثبت", bootstyle=SUCCESS)
        self.save_button.grid(column=0, row=6, columnspan=2, sticky= EW, padx=2, pady=5)


    def get_student_form(self):
        return{
            "name" : self.name_entry.get(),
            "national_code" : self.national_code_entry.get(),
            "mobile" : self.mobile_entry.get(),
            "password" : self.password_entry.get(),
            "grade_level" : self.grade_level_entry.get(),
            "field_of_study" : self.field_of_study_entry.get()
        }
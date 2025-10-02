from ttkbootstrap import Window
from db.db_connection import Database
from db.db_schema import create_tables
# from models.student_model import studentModel
# from controllers.student_controller import studentController
# from views.student_view import studentView
from models.student_model import StudentModel
from controllers.student_controller import StudentController
from views.student_view import studentView
def main():
    db = Database()
    create_tables(db)

    student_model = StudentModel(db)
    student_controller = StudentController(student_model)

    app = Window(themename="flatly")
    studentView(app, student_controller)
    app.mainloop()

    db.close()

# if __name__ == "__main__":
main()

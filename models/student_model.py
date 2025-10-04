class StudentModel:
    def init(self, db):
        self.db = db

    def add_student(self, name, national_code, mobile, password, grade_level, field_of_study):
        self.db.execute("INSERT INTO students (name, national_code, mobile, password, grade_level, field_of_study) VALUES (?,?,?,?,?,?)",
                        (name, national_code, mobile, password, grade_level, field_of_study))

    def get_all_students(self):
        return self.db.fetchall("SELECT id, name, national_code, mobile, grade_level, field_of_study FROM students")

    def delete_student(self, student_id):
        self.db.execute("DELETE FROM students WHERE id = ?", (student_id,))
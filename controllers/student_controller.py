from messages.errors import ErrorMessages

class StudentController:
    def __init__(self, model):
        self.model = model

    def create_student(self, name,nationa_code ,password , mobile):
        if not name:
            raise ValueError(ErrorMessages.INVALID_CLASS_NAME)
        if  not nationa_code :
            raise ValueError(ErrorMessages.INVALID_CAPACITY)
        if  not password :
            raise ValueError(ErrorMessages.INVALID_CAPACITY)
        if  not mobile :
            raise ValueError(ErrorMessages.INVALID_CAPACITY)


        self.model.add_student(name,nationa_code ,password , mobile)

    def get_student(self):
        return self.model.get_all_student()

    def update_student(self, student_id, name, capacity):
        self.model.update_student(student_id, name, capacity)

    def delete_student(self, student_id):
        self.model.delete_student(student_id)

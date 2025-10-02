def create_tables(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            capacity INTEGER NOT NULL CHECK(capacity > 0)
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
<<<<<<< HEAD
            nationa_code TEXT NOT NULL, 
            mobile TEXT NOT NULL, 
            password TEST NOT NULL
=======
            national_code TEXT NOT NULL,
            mobile TEXT NOT NULL,
            password TEXT NOT NULL
>>>>>>> c1772aff6afa1f9a439da0622fb034554b828702
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            class_id INTEGER NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(class_id) REFERENCES classes(id),
            UNIQUE(student_id, class_id)
        )
    """)

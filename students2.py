import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

students = [
("John Kamau","S001"),
("Mary Wanjiku","S002"),
("Peter Mwangi","S003"),
("Jane Njeri","S004"),
("David Maina","S005"),
("Faith Wangari","S006"),
("Brian Kariuki","S007"),
("Mercy Nyambura","S008"),
("Samuel Kibet","S009"),
("Grace Achieng","S010"),
("Kevin Kiptoo","S011"),
("Joy Chebet","S012"),
("Victor Otieno","S013"),
("Lucy Atieno","S014"),
("Dennis Mutua","S015"),
("Sarah Muthoni","S016"),
("James Kimani","S017"),
("Naomi Waithira","S018"),
("Fredrick Njuguna","S019"),
("Purity Wairimu","S020")
]

cursor.executemany(
"INSERT INTO students(name, reg_no) VALUES(?, ?)",
students
)

conn.commit()
conn.close()

print("20 students added successfully")
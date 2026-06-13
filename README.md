# 📝 To-Do List Application

A simple and user-friendly **Command Line To-Do List Application** built using Python. This project helps users manage their daily tasks efficiently by allowing them to add, view, and remove tasks through an interactive menu-driven interface.

---

## 🚀 Project Overview

The To-Do List Application is designed to help users organize their tasks directly from the terminal. It demonstrates the use of fundamental Python concepts and provides a practical example of a menu-driven application.

This project was developed as part of my **Python Programming Internship at Decode Labs**.

---

## ✨ Features

✅ Add new tasks

✅ View all saved tasks

✅ Remove completed tasks

✅ Interactive menu-driven interface

✅ Continuous execution until user chooses to exit

✅ Beginner-friendly and easy to understand

---

## 🛠️ Technologies Used

* Python 3.x
* Command Line Interface (CLI)

---

## 📂 Project Structure

```text
decode_labs-task-1-navyatha/
│
├── todo.py
└── README.md
```

### File Description

* **todo.py** – Main Python program containing the To-Do List functionality.
* **README.md** – Project documentation.

---

## ▶️ How to Run the Project

### Requirements

* Python 3.x installed on your system

### Steps

1. Download or clone the project files.
2. Open the project folder.
3. Open a terminal or command prompt in the project directory.
4. Run the following command:

```bash
python todo.py
```

5. Use the menu options to:

   * Add Tasks
   * View Tasks
   * Remove Tasks
   * Exit the Application

---

## 📸 Sample Output

```text
===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Enter your choice: 1
Enter task: Complete Python Assignment
Task added successfully!

===== TO-DO LIST =====
1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Enter your choice: 2

Your Tasks:
1. Complete Python Assignment
```

---

## 💡 Working Principle

### 1. Add Task

Users can add a new task by selecting option **1**. The task is stored in a Python list using:

```python
tasks.append(task)
```

### 2. View Tasks

Users can view all saved tasks. The program displays tasks with numbering using the `enumerate()` function.

### 3. Remove Task

Users can remove a task by selecting its corresponding number. The selected task is deleted using:

```python
tasks.pop(task_number - 1)
```

### 4. Exit Program

Selecting option **4** safely exits the application.

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Python list operations
* Looping and iteration
* Conditional statements
* User input handling
* Menu-driven application development
* Basic project documentation
* Problem-solving using Python

---

## 🔮 Future Enhancements

* Save tasks permanently using files
* Mark tasks as completed
* Add task priorities
* Include due dates and reminders
* Develop a graphical user interface (GUI)
* Store tasks using a database
* Add task search functionality

---

## 🔗 Repository Link

Repository:
https://github.com/NavyathaRameswarapu/decode_labs-task-1-navyatha

---

## 👨‍💻 Author

**Navyatha Rameswarapu**

Python Programming Intern

Decode Labs

GitHub Profile:
https://github.com/NavyathaRameswarapu

---

## 📜 License

This project is developed for educational and learning purposes as part of the Decode Labs Python Programming Internship.

---

## 🙏 Acknowledgements

* Decode Labs
* Python Community
* Open Source Learning Resources

---

### ⭐ If you found this project helpful, please consider starring the repository!

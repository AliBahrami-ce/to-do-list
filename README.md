# 📝 To-Do List (Python)

A simple and practical **To-Do List application** written in Python.  
This CLI-based program allows you to add, remove, view, and save tasks in a clean and organized way.

---

## 🚀 Features

- ➕ Add new tasks  
- ❌ Remove tasks by index  
- 📋 View all tasks  
- 💾 Save tasks to a CSV file  
- 📝 Optional comments for each task  
- 🎯 Task priority levels: `high`, `medium`, `low`  
- 🧹 Cross-platform screen clearing (Windows / Linux)  

---

## 📦 Installation & Usage

### 1. Clone the repository:

```bash
git clone https://github.com/AliBahrami-ce/to-do-list
```

### 2. Navigate into the project directory:

```bash
cd to-do-list
```
### 3. Run the Python script:

```bash
python to_do_list.py
```

---

## 🖥️ Program Menu

When you run the program, you will see:

```
1. Add new Task.
2. Remove the Task.
3. Show all Tasks.
4. Save your Tasks in csv file.
5. exit.
```

Each option performs the following action:

- **1 — Add new Task:**  
  Prompts the user for task title, priority (`high`, `medium`, `low`), and an optional comment.

- **2 — Remove a Task:**  
  Displays the current list of tasks and allows removal by task number.

- **3 — Show all Tasks:**  
  Lists all tasks with their assigned numbers, priorities, and comments.

- **4 — Save Tasks to CSV file:**  
  Exports the task list into a `tasks.csv` file in the project directory.

- **5 — Exit:**  
  Closes the program safely.

---

## 📊 Example CSV Output

When tasks are saved, the program generates a CSV file with the following structure:

| Task              | Priority | Comment            |
|-------------------|----------|--------------------|
| Buy groceries     | high     | No Comment         |
| Finish homework   | medium   | Finish by tonight  |

You can open the CSV file using Excel, Google Sheets, or any text editor.

---

## 🧠 Code Architecture Overview

### 🔹 Class: Task

Handles information related to a single task:

- `task` — title of the task

- `priority` — task priority level

- `comment` — optional description or notes

It also implements `__str__()` for clean text representation.

---

### 🔹 Class: ToDo

Responsible for the main application logic:

- Maintaining a list of `Task` objects

- Adding tasks

- Removing tasks by index

- Displaying tasks in a numbered list

- Saving tasks into a CSV file

This class keeps the program organized and easy to extend.

---

## 📦 Dependencies

This project uses only Python’s built-in libraries, so no installation is required:

- `csv` – for writing task data to a CSV file

- `os` – for clearing the screen on Windows/Linux

---

## 🤝 Contributing

Contributions are always welcome!
If you have ideas for improvements—such as adding colors, sorting, or editing tasks—feel free to open an issue or create a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 👤 Author
**Ali Bahrami**  
GitHub: https://github.com/AliBahrami-ce

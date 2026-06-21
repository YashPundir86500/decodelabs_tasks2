# Expense Tracker

> A lightweight, terminal-based personal finance tool built with Python — track your spending in real time, no setup required.

---

## Overview

**Expense Tracker** is a clean, no-dependency command-line application that helps you log expenses on the fly. Enter amounts one by one, monitor a live running total, and receive a complete financial summary — all within your terminal.

Whether you're tracking daily grocery bills, travel expenses, or project costs, this tool gives you instant clarity without any spreadsheet overhead.

---

## Features

| Feature | Description |
|---|---|
| 🔄 Live Running Total | Updates after every entry — no need to wait till the end |
| 📊 Session Summary | Final report with total count, total spent, and average per expense |
| 🛡️ Input Validation | Handles invalid text, negative values, and edge cases gracefully |
| ⚡ Zero Dependencies | Pure Python — no pip installs, no virtual environments needed |
| 🖥️ Cross-Platform | Works on Windows, macOS, and Linux out of the box |

---

## Requirements

- **Python 3.x** — [Download here](https://www.python.org/downloads/) if not already installed

Verify your installation:

```bash
python --version
```

---

## Installation

No installation needed. Just clone or download the script:

```bash
# Clone the repository
git clone https://github.com/your-username/expense-tracker.git

# Navigate into the project folder
cd expense-tracker
```

Or simply download `Expense_Tracker.py` directly.

---

## Usage

Run the script from your terminal:

```bash
python Expense_Tracker.py
```

### How It Works

1. The program prompts you to enter an expense amount
2. Type a **positive number** and press `Enter` to log it
3. A **running total** is displayed after each entry
4. Type **`quit`** when you're done to generate your summary

---

## Demo

```
=============================================
        💰  EXPENSE TRACKER  💰
=============================================
Enter each expense amount one at a time.
Type "quit" to finish and see your total.

  Expense #1: $850
  ✅ Added.  Running total: $850.00

  Expense #2: $1200.50
  ✅ Added.  Running total: $2,050.50

  Expense #3: $-50
  ⚠️  Please enter a positive amount.

  Expense #3: $320
  ✅ Added.  Running total: $2,370.50

  Expense #4: quit

=============================================
           📊  SUMMARY
=============================================
  Expenses entered : 3
  Total spent      : $2,370.50
  Average expense  : $790.17
=============================================
  Thanks for using Expense Tracker. Goodbye!
=============================================
```

---

## Input Handling

The application is designed to handle unexpected inputs without crashing:

| Input Type | Example | Behavior |
|---|---|---|
| Valid amount | `499.99` | ✅ Logged and added to total |
| Negative number | `-200` | ⚠️ Rejected with a warning |
| Non-numeric text | `hello` | ❌ Error message shown, prompt repeats |
| Exit command | `quit` | 🚪 Session ends, summary displayed |

---

## Project Structure

```
expense-tracker/
│
├── Expense_Tracker.py   # Core application logic
└── README.md            # Project documentation
```

---

## Application Flow

```
┌─────────────────────────────────────────────┐
│              Program Start                  │
│         Initialize total = 0.0              │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  Prompt Input  │◄──────────────────┐
         └───────┬────────┘                   │
                 │                            │
        ┌────────▼─────────┐                  │
        │  Input = "quit"? │                  │
        └────────┬─────────┘                  │
           No    │   Yes                      │
          ───────┘   ────────────────►  Print Summary
                                         & Exit
           ┌─────▼──────────────┐
           │  Is it a number?   │
           └─────┬──────────────┘
           No    │   Yes
     Error msg   │
     & Loop  ◄───┘
                 │
        ┌────────▼──────────┐
        │  Is it positive?  │
        └────────┬──────────┘
           No    │   Yes
    Warning &    │
    Loop     ◄───┘
                 │
        ┌────────▼──────────────────┐
        │  Add to total, increment  │
        │  counter, show running    │──────────────────► Loop
        │  total                    │
        └───────────────────────────┘
```

---

## Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch — `git checkout -b feature/your-feature-name`
3. **Commit** your changes — `git commit -m "Add: your feature description"`
4. **Push** to your branch — `git push origin feature/your-feature-name`
5. **Open** a Pull Request

### Ideas for Future Enhancements

- [ ] Category tagging for expenses (Food, Travel, Utilities, etc.)
- [ ] Export summary to CSV or PDF
- [ ] Persistent storage using SQLite or JSON
- [ ] Monthly budget limit with overspend alerts
- [ ] Multi-currency support

---

## License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it for personal or commercial purposes.

---

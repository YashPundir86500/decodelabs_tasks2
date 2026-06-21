# ============================================================
#  Expense Tracker
#  Continuously collects expense amounts from the user,
#  accumulates a running total, and reports the final sum.
# ============================================================

def main():
    # --- Accumulator variable ---
    total = 0.0
    expense_count = 0

    print("=" * 45)
    print("        💰  EXPENSE TRACKER  💰")
    print("=" * 45)
    print("Enter each expense amount one at a time.")
    print('Type "quit" to finish and see your total.\n')

    # --- Continuous input loop ---
    while True:
        user_input = input(f"  Expense #{expense_count + 1}: $").strip()

        # Exit condition
        if user_input.lower() == "quit":
            break

        # --- Input validation with try-except ---
        try:
            expense = float(user_input)

            if expense < 0:
                print("  ⚠️  Please enter a positive amount.\n")
                continue

            # Accumulate the running total
            total += expense
            expense_count += 1

            print(f"  ✅ Added.  Running total: ${total:,.2f}\n")

        except ValueError:
            # Handles anything that can't be converted to a number
            print('  ❌ Invalid input. Enter a number or "quit".\n')

    # --- Final summary ---
    print("\n" + "=" * 45)
    print("           📊  SUMMARY")
    print("=" * 45)
    print(f"  Expenses entered : {expense_count}")
    print(f"  Total spent      : ${total:,.2f}")

    if expense_count > 0:
        average = total / expense_count
        print(f"  Average expense  : ${average:,.2f}")

    print("=" * 45)
    print("  Thanks for using Expense Tracker. Goodbye!")
    print("=" * 45)


if __name__ == "__main__":
    main()
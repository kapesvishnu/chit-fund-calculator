import tkinter as tk
from tkinter import ttk

class ChitCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Chit Calculator")
        self.root.geometry("350x250")
        
        # Input fields
        ttk.Label(root, text="Total Amount:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.total_amount = ttk.Entry(root, width=15)
        self.total_amount.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Members:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.members = ttk.Entry(root, width=15)
        self.members.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Months:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.months = ttk.Entry(root, width=15)
        self.months.grid(row=2, column=1, padx=10, pady=5)
        
        ttk.Label(root, text="Bid Amount:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.bid_amount = ttk.Entry(root, width=15)
        self.bid_amount.grid(row=3, column=1, padx=10, pady=5)
        
        # Calculate button
        ttk.Button(root, text="Calculate", command=self.calculate).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Result display
        self.result = tk.Text(root, height=6, width=40)
        self.result.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
    
    def calculate(self):
        try:
            total = float(self.total_amount.get())
            members = int(self.members.get())
            months = int(self.months.get())
            bid = float(self.bid_amount.get())
            
            monthly = total / months
            winner_gets = total - bid
            dividend = bid / (members - 1)
            net_payment = monthly - dividend
            
            result_text = f"""Monthly Contribution: ₹{monthly:,.0f}
Winner Receives: ₹{winner_gets:,.0f}
Dividend per Member: ₹{dividend:,.0f}
Net Payment per Member: ₹{net_payment:,.0f}"""
            
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, result_text)
        except:
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, "Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChitCalculator(root)
    root.mainloop()
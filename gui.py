from tkinter import *


class GUI:
    def __init__(self, window):

        self.window = window
        self.frame1 = Frame(self.window)
        self.label_gross_income = Label(self.frame1, text='your gross income')
        self.entry_gross_income = Entry(self.frame1, width= 15)


        self.label_gross_income.pack(side = 'left')
        self.entry_gross_income.pack(side = 'left')
        self.frame1.pack()


        self.frame2 = Frame(self.window)
        self.label_marriage = Label(self.frame2, text='your marriage status')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_single = Radiobutton(self.frame2, text='single', variable=self.radio_1, value = 0)
        self.radio_married = Radiobutton(self.frame2, text='married', variable=self.radio_1, value =1)
        self.label_marriage.pack(side = 'left')
        self.radio_single.pack(side = 'left')
        self.radio_married.pack(side = 'left')
        self.frame2.pack()

        self.frame3 = Frame(self.window)
        self.button_calculate = Button(self.frame3, text = 'calculate', command = self.clicked)
        self.label_net_income = Label(self.frame3, text = 'Your calculated net income is:')
        self.button_calculate.pack()
        self.label_net_income.pack()
        self.frame3.pack()

        gross_income = self.entry_gross_income.get()
    def clicked(self):
        self.button_calculate.pack_forget()
        self.label_net_income.pack_forget()

        if self.radio_1 == 0:
            deduction_single = float(12950)
            taxable_income = self.entry_gross_income.get() - deduction_single
            if taxable_income <= 10275:
                tax = taxable_income * 0.1
            elif 10276 < taxable_income < 41775:
                tax = (taxable_income - 1027.5) * 0.1 + 1027.50
            elif 41776 <= taxable_income <= 89075:
                tax = (taxable_income - 41775) * 0.22 + 4807.50
            elif 89076 <= taxable_income <= 170050:
                tax = (taxable_income - 89075) * 0.24 + 15213.50
            elif 170051 <= taxable_income <= 215950:
                tax = (taxable_income - 170050) * 0.32 + 34647.50
            elif 215951 <= taxable_income <= 539900:
                tax = (taxable_income - 215951) * 0.35 + 49335.50

            else:
                tax = (taxable_income - 539901) * 0.37 + 162718

            net_income = gross_income - tax
            return net_income

        elif self.radio_1==1:
            deduction_married = float(25900)
            taxable_income = self.entry_gross_income.get() - deduction_married
            if taxable_income <= 20550:
                tax = taxable_income * 0.1
            elif 20551 < taxable_income < 83550:
                tax = (taxable_income - 20550) * 0.1 + 2055
            elif 83551 <= taxable_income <= 178150:
                tax = (taxable_income - 83550) * 0.22 + 9615
            elif 178151 <= taxable_income <= 340100:
                tax = (taxable_income - 178150) * 0.24 + 30427
            elif 340101 <= taxable_income <= 431900:
                tax = (taxable_income - 340100) * 0.32 + 69295
            elif 431900 <= taxable_income <= 647850:
                tax = (taxable_income - 431900) * 0.35 + 98671

            else:
                tax = (taxable_income - 647850) * 0.37 + 174253.50

            net_income = gross_income - tax
            return net_income

        self.frame4 = Frame(self.window)
        self.button_calculate = Button(self.frame4, text = 'calculate')
        self.label_net_income = Label(self.frame4, text = 'Your calculated net income is:')

        self.button_calculate.pack()
        self.label_net_income.pack()
        self.frame4.pack()
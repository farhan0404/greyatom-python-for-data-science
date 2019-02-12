# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)






# code ends here


# --------------
# code starts here
#print(bank.head())
banks  = bank.drop('Loan_ID', axis=1)
print(banks.head())
#banks.isnull().sum()

bank_mode = banks.mode()
#print(bank_mode)
banks = banks.fillna("")
print(banks.head())
#code ends here


# --------------
# code starts here

# check the avg_loan_amount
avg_loan_amount = 0
avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


print (avg_loan_amount)
# code ends here


# --------------
# code starts here

#print(banks.head())

Loan_Status = 614

#print(banks[ (banks['Self_Employed'] == 'Yes') & (banks[ 'Loan_Status'] == 'Y') ].shape)
# We just need count of rows
loan_approved_se = banks[ (banks['Self_Employed'] == 'Yes') & (banks[ 'Loan_Status'] == 'Y') ].shape[0]
#print(loan_approved_se)

loan_approved_nse = banks[ (banks['Self_Employed'] == 'No') & (banks[ 'Loan_Status'] == 'Y') ].shape[0]
#print(loan_approved_nse)


percentage_se = loan_approved_se/Loan_Status*100;
print(percentage_se)

percentage_nse = loan_approved_nse/Loan_Status*100;
print(percentage_nse)

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply( lambda  x : x/12)
#print(loan_term)

b_loan_term = []

for element in loan_term :
    if element >= 25:
        b_loan_term.append(element)

big_loan_term = len(b_loan_term)

print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')
print(loan_groupby.head)

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()

print(mean_values)

# code ends here



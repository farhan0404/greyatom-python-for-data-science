# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code starts here

data = pd.read_csv(path)

loan_status = data['Loan_Status'].value_counts()
print(loan_status)

loan_status.plot(kind='bar', figsize=(10,5))


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
print(property_and_loan)

property_and_loan = property_and_loan.size().unstack()

property_and_loan.plot(kind='bar', stacked='Fale', figsize=(10,5))

plt.xlabel('Property Area', rotation=45)
plt.ylabel('Loan Status')


# --------------
#Code starts here

education_and_loan = data.groupby(['Education', 'Loan_Status'])

#education_and_loan = education_and_loan.size()
#print(education_and_loan)
#education_and_loan = education_and_loan.unstack()
#print(education_and_loan)

education_and_loan = education_and_loan.size().unstack()

education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))

plt.xlabel('Education Status', rotation=45)
plt.ylabel('Loan Status')



# --------------
#Code starts here
graduate = data[ data['Education'] == 'Graduate' ]
not_graduate = data[ data['Education'] == 'Not Graduate' ]

#print(graduate)

graduate.plot(x='Education', y='LoanAmount', kind='density', label='Graduate')


not_graduate.plot(x='Education', y='LoanAmount', kind='density', label='Not Graduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(10,5))

data.plot.scatter('ApplicantIncome', 'LoanAmount', ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter('CoapplicantIncome', 'LoanAmount', ax=ax_2)
ax_1.set_title('Coapplicant Incom')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

data.plot.scatter('ApplicantIncome', 'LoanAmount', ax=ax_3)
ax_1.set_title('Total Income')



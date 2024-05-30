import pandas as pd
import matplotlib as plot
data = pd.read_csv('Salary_dataset.csv')
def finding_line(m,n,points,L):
    m_gradient=0
    n_gradient=0
    n=len(points)

    for i in range(n):
        x=points.iloc[i].YearsExperience
        y=points.iloc[i].Salary

        m_gradient=m_gradient+(-(n/2)*(x)*(y-((m*x)+n)))
        n_gradient=n_gradient+(-(n/2)*(y-((m*x)+n)))
        


    m=m-(m_gradient*L)
    n=n-(n_gradient*L)
    return m, n

def linearregprediction(m,n,x):
    y=(m*x)+n
    return y
m=0
n=0
points=data
L=0.0001
epoch=10000
for i in range(epoch):
    if(i%50==0):
        print("epoch:",i)
    m,n=finding_line(m,n,points,L)
yearsofexp=float(input("enter your years of expereince"))
print("the expected salary is:",linearregprediction(m,n,yearsofexp))

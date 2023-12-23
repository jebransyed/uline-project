import pandas as pd

def main():
    callsBought = pd.read_excel('data.xlsx', usecols='A:C')
    print(callsBought)
    putsBought = pd.read_excel('data.xlsx', usecols='D:F')
    print(putsBought)
    putsSold = pd.read_excel('data.xlsx', usecols='G:I')
    print(putsSold)
main()
	

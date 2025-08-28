def main():
    import pandas as pd # Please install pandas and matplotlib before you run this example
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy
    import genomap as gp

    data = pd.read_csv('./data/TM_data.csv', header=None,
                    delim_whitespace=False)
    colNum=33 # Column number of genomap
    rowNum=33 # Row number of genomap

    dataNorm=scipy.stats.zscore(data,axis=0,ddof=1) # Normalization of the data

    genoMaps=gp.construct_genomap(dataNorm,rowNum,colNum,epsilon=0.0,num_iter=200) # Construction of genomaps

    findI=genoMaps[10,:,:,:]

    plt.figure(1) # Plot the first genomap
    plt.imshow(findI, origin = 'lower',  extent = [0, 10, 0, 10], aspect = 1)
    plt.title('Genomap of a cell from TM dataset')
    plt.show()

if __name__=='__main__':
    main()
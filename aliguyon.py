import numpy as np

def bott0(X,Y):
    """
    Returns the dimension 0 bottleneck distace between two persistence diagrams.
    All components are assumed to be born at the beginning of the filtration, 
    that is, all non-trivial points lie in the vertical axis.   
    
    Parameters
    ----------
    X : 1D numpy array
        Array of death times for persistence diagram 1.
    Y : 1D numpy array
        Array of death times for persistence diagram 2.
           
    Returns
    -------
    d : float
        The bottleneck distance between X and Y.
        
    Examples
    --------
    >>> X = numpy.array([109.01312371,   6.05218697,  68.54887031,  43.17754162,
                         66.514876  ,  73.74001403, 136.64334121,  55.74159051,
                         67.10843369,  31.24178587])
    >>> Y = numpy.array([0.96503372, 0.59901363, 0.91057621, 0.99692426, 
                         0.01674558, 0.09542911, 0.32735304, 0.86144547])
    >>> bott0(X,Y)
    68.321670605
      
    """
    #Swap if Y is longer
    if len(Y) < len(X):
        X_copy = X
        X = Y
        Y = X_copy  
        
    #Initialize
    X=-np.sort(-X) 
    Y=-np.sort(-Y)
    N = len(X) 
    Z = abs(X-Y[0:N]) 
    #Compare Z with the trivial matchings. Update Z
    for i in range(N):
        if Z[i]>0.5*max(X[i],Y[i]):
            Z[i]=0.5*max(X[i],Y[i])
    d=max(Z)
    if N != len(Y) and d < 0.5*Y[N]:
        d = 0.5*Y[N] 
    
    return d




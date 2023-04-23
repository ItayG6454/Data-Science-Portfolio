import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.optimize import curve_fit


###################
#    D  F  T      # 
###################
def dft_1d(vec, direction):
    '''
    Function to calculate the discrete Fourier Transform of a signal vec
    Input : vec - complex 1d vector. direction - operator for chosen method. 
    Output: the iDFT/DFT for the given vec (FFTW_FORWARD/FFTW_BACKWARD). 
    '''
    N = len(vec)
    # Forward algorithm
    if direction == "FFTW_FORWARD":
        A = np.zeros(N, dtype=np.complex128)
        for j in range(N):
            for k in range(N):
                # Calculate by formula
                A[k] += vec[j] * np.exp( 2j * np.pi * j * k / N)
        return A
    # Backward algorithm
    elif direction == "FFTW_BACKWARD":
        y = np.zeros(N, dtype=np.complex128)
        for k in range(N):
            for j in range(N):
                y[k] += vec[j] * np.exp( -2j * np.pi * j * k / N)
            y[k] /= N
        return y

###################
#     TASK 2      #
###################

def test_dft_1d():
    """
    Testing the function 'dft_1d'. 
    Input : None
    Output: The function prints PASS/FAIL according to 3 tests. 
    """
    tests = np.array([True, True, True]) # tests results
    input = [1, 2+1j, 3, 4-1j]           # input sequence 
    exp_res_dft = [10, -4-2j, -2, 2j]    # expected value for DFT(input), calc by hand
    '''
    TEST I  : comparing our DFT's results to expected results. 
    '''
    if not np.allclose(dft_1d(input, 'FFTW_FORWARD'), exp_res_dft, atol=1e-6): tests[0] = False
    '''
    TEST II  : cheking that iDFT(DFT) = I  
    '''
    if not np.allclose(dft_1d(exp_res_dft, 'FFTW_BACKWARD') ,input, atol=1e-6) : tests[1]=False
    '''
    TEST III  : checking that DFT(iDFT)=I 
    '''
    idft = dft_1d(input, 'FFTW_BACKWARD')
    if not np.allclose(dft_1d(idft, 'FFTW_FORWARD') ,input, atol=1e-6) : tests[2]=False
    # Print the output
    if tests.all(): print("PASS")
    else:  print('FAIL')

###################
#     TASK 3      #
################### 

def dft_1d_matrix(vec,direction):  
    '''
    Function that calculate DFT using matrix multiplication. 
    Input : vec - complex 1d vector. direction - operator for chosen method. 
    Output: the iDFT/DFT for the given vec (FFTW_FORWARD/FFTW_BACKWARD). 
    '''
    # setup dims vectors:
    N = len(vec)
    n = np.arange(N)
    k = n.reshape((N, 1))
    # Forward algorithm
    if direction == "FFTW_FORWARD":
        e = np.exp(2j * np.pi * k * n / N)
        # Compute the DFT of the input
        A = np.dot(e, vec)
        return A
    # Backward algorithm
    elif direction == "FFTW_BACKWARD":
        F = np.exp(-2j * np.pi * k * n / N)
        # Compute the IDFT of the input
        y = np.dot(F, vec) / N
        return y

###################
#     TASK 4     #
################### 

def plot_dft_timing():
    '''
    Function that analalyzing the runnning time of DFT's method we haved implemented ('dft_1d' Vs. 'dft_1d_matrix').
    Input : None. 
    Output: void. Plotting graph of the data with extimated coefs. 
    '''
    '''
    Part I - Calculations of time curves
    '''
    N = 100 # max size of input
    # Create  calculation result vector for dft_1d (ordinary form)
    ord = np.zeros(N) 
    # Create  calculation result vector for dft_1d_matrix
    mat = np.zeros(N)
    # looping for each n - size of input vector and measuring running time
    for n in range(1,N):
        # Create random data to transform
        x = np.random.uniform(-1 * n, n, n) + 1.j * np.random.uniform(-1 * n, n, n)
        # estimating ordinary function's time
        start_time = time.time()
        dft_1d(x, "FFTW_FORWARD")
        ord[n] = time.time() - start_time
        # estimating matrix function's time
        start_time = time.time()
        dft_1d_matrix(x, "FFTW_FORWARD")
        mat[n] = time.time() - start_time
    """
    Part II -Eestimating curve's coeffients & Plotting results
    """
    # Create X axis vector
    x_axis = np.linspace(1, N, N)
    # plot measured curves
    plt.plot(x_axis, ord, 'g-', label='dft_1d')
    plt.plot(x_axis, mat, 'b-', label='dft_1d_matrix')
    # estimate curve's coeffients using curve_fit from 'scipy.optimize' (see notes below)
    ord_coef, ord_tmp = curve_fit(curve_fit_func, x_axis, ord)
    matrix_coef, matrix_tmp = curve_fit(curve_fit_func, x_axis, mat)
    # plotting the fitted curve's
    plt.plot(x_axis, curve_fit_func(x_axis, *ord_coef), 'r-',
             label='dft_1d fit: c=%g, a=%g' % tuple(ord_coef))
    plt.plot(x_axis, curve_fit_func(x_axis, *matrix_coef), 'y-',
             label='dft_1d_matrix fit: c=%g, a=%g' % tuple(matrix_coef))
    plt.xlabel('input size')
    plt.ylabel('time')
    plt.legend()
    plt.show()

# The curve fit function
def curve_fit_func(n, c, a):
    return c * (n ** a)


# plot_dft_timing()




"""
Notes about curve_fit:
Method : Use non-linear least squares to fit a function, f, to data.
Reuturn 1 - popt (1-d array) : Optimal values for the parameters so that the sum of the squared residuals
                                of f(xdata, *popt) - ydata is minimized.
Return  2 - pcov (2-d array) : The estimated covariance of popt.
                                The diagonals provide the variance of the parameter estimate. 
"""

# Sanity Check (using Ex 1)
input = [1, 2, 3, 4 ,5 ,6]           
A1_1  = [15 ,   -2.5-3.44j ,-2.5-0.81j ,-2.5+0.81j ,-2.5+3.44j]
print(np.around(dft_1d_matrix(input, 'FFTW_FORWARD'),2))
print(np.around(dft_1d_matrix(A1_1, 'FFTW_BACKWARD'),2))

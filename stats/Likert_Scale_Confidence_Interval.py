#coding=utf-8
import scipy.stats as stats
import numpy as np

def confidenceInterval(n_respondents, n_total, n_LikertLevels=3, significanceLevel=0.05, debug=False):
    """
    Description:
    --------------------
    This calculates the confidence interval for a Likert Response with k Likert scale levels.
    
    It uses the equation:
    
    Response% +/- ConfidenceInterval = 
    
    (n_i + B/2) / (n + B) +/- sqrt( (B**2/4 + B * n_i * (1 - n_i/n)) / (n + B)**2 )
    
    where:
    
    n_i = number of respondents choosing the i-th level
    
    n = SUM(n_i, from:i=1, to:k), i.e. the total number of responses to the question
    
    k = maximum Likert scale levels (in our case, 3 after data is condensed)
    
    B = upper (alpha / k) 100th percentile of the chisquare distribution
        with 1 degree of freedom. (in this case 95%)
        
    EXAMPLE:
    --------
    Sample Question: "When doing a physics experiment, I don't think much 
    about sources of systematic error. What do YOU think?"
    
    Data:
    -----
    Strongly Agree    : 95
    Agree             : 218
    Neutral           : 196
    Disagree          : 86
    Strongly Disagree : 27
    N/A               : 11
    
    for 6 scale likert scale (Strongly Agree to Strongly Disagree + N/A)
    95% Confidence Interval, alpha=0.05, k=6:
    
    Using R:
    > qchisq(0.05/6,1, lower.tail=FALSE)
    [1] 6.960401
            
    NOTE, in R:
    
    lower.tail logical; if TRUE (default), probabilities are P[X ≤ x], 
    otherwise, P[X > x].

    
    But since this is Python:
    
    In [1]: import scipy.stats as stats

    In [2]: stats.chi2.ppf(1-0.05/6,1)
    Out[2]: 6.96040144105298
    
    NOTE, in Python:
    
    There is no 'lower.tail' to switch the range of the probability, thus
    we do '1-0.05/6'. (remember that 6 is just the number of Likert options
    in this example).
    
    Confidence Interval for percent saying "Strongly Agree":
    
    StronglyAgree% +/- CI = (95 + 6.96/2) / (633 + 6.96) +/- sqrt( (6.96**2/4 + 6.96 * 95 * (1 - 95/633)) / (633 + 6.96)**2 )
    StronglyAgree% +/- CI = 0.154 +/- 0.037
    
    Sources:
    [1] slide 13-14, http://faculty.nps.edu/rdfricke/OA4109/Lecture%209-1%20--%20Introduction%20to%20Survey%20Analysis.pdf
    [2] Accepted response, http://stackoverflow.com/questions/18070299/is-there-a-python-equivalent-of-rs-qchisq-function
    [3] scipy documentation, http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html
    [4] R documentation, https://stat.ethz.ch/R-manual/R-patched/library/stats/html/Chisquare.html
    
    Parameters:
    -------------------
    n_respondents : int (n_i)
    number of respondents with likert scale
    
    n_LikertLevels : int (k) : Default=3
    number of Likert Levels. Default is 3 due to combination of Likert
    responses (Strongly Dis/Agree and Dis/Agree)
    
    n_total : int (n)
    number of total responses to question
    
    significanceLevel : float (alpha = B * k) : Default=0.05
    The significance level typically known as 'alpha'. Default is 0.05.
    
    debug: Boolean : Default=False
    If True, returns B value.
    
    Returns:
    -------------------
    B : float : Default does not return
    The value returned from scipy.stats.chi2.ppf
    
    ResponsePercent : float
    Value responding with selected response.
    
    ConfidenceInterval : float
    The upper and lower bound of the interval.
    """
    if isinstance(n_respondents, int)==False:
        raise ValueError('n_respondents needs to be an integer.')
        
    if isinstance(n_LikertLevels, int)==False:
        raise ValueError('n_LikertLevels needs to be an integer.')
        
    if isinstance(n_total, int)==False:
        raise ValueError('n_total needs to be an integer.')
        
    if isinstance(significanceLevel, float)==False:
        raise ValueError('significanceLevel needs to be a float.')
        
    if significanceLevel > 1 or significanceLevel < 0:
        raise ValueError('significanceLevel needs to be between 0 and 1.')
    
    if n_respondents <= 0:
        raise ValueError('n_respondents needs to be greater than 0.')

    if n_LikertLevels <= 0:
        raise ValueError('n_LikertLevels needs to be greater than 0.')
        
    if n_total <= 0:
        raise ValueError('n_total needs to be greater than 0.')
    
    B = stats.chi2.ppf(1-significanceLevel/n_LikertLevels, 1)
    
    ResponsePercent = (n_respondents + B/2) / (n_total + B)
    ConfidenceInterval = np.sqrt(((B**2)/4 + B * n_respondents * (1 - n_respondents/n_total))/(n_total + B)**2)
    
    if debug==True:
        return B, ResponsePercent, ConfidenceInterval
    else:
        return ResponsePercent, ConfidenceInterval
    
    

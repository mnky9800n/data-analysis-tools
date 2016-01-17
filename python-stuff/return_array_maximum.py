def return_maximum_index(twoDarray):
    """
    returns maximum of 2d array
    """
    m_local = 0
    m_i = 0
    m_a = 0
    for n,m in enumerate(twoDarray):
        if m.max() > m_local:
            m_local = m.max()
            m_i = m.argmax()
            m_a = n

    return m_local, m_i, m_a

import numpy as np

def TransmissaoMIMO(H,s,SNR=15):
    """
    TransmissaoMIMO(H,s,power=1,N0=1)
    Descrição:
        Realiza uma transmissão MIMO pelo canal H especificado 
        e adiciona um ruído branco e gaussiano no resultado.
    Parâmetros:
        - H: Canal de dimensão M*K
        - s: Sinal com dimensões K*(message length)
        - SNR: Signal to Noise Ratio em dB (default 15)
    Retorna:
        - y: Sinal recebido de dimensões M*(message length)
    """

    noise = np.random.normal(0,1,size=(H.shape[0],s.shape[1]))
    return (np.sqrt(10**(SNR/20)))*np.matmul(H,s) + noise

def Quantizador(data):
    """
    Quantizador(signal)
    Descrição:
        Realiza a quantização do sinal recebido. 
        A quantização é equivalente à modulação QPSK.
    Parâmetros:
        - signal: O sinal (complexo) a ser quantizado. 
    Retorna:
        - Sinal quantizado. 
    """
    return (np.sign(np.real(data))+1j*np.sign(np.imag(data)))/np.sqrt(2)

def ReceptorZF(H_est,signal=None):
    """
    ReceptorZF(H_est,signal)
    Calcula o receptor ZF com base no `H_est` e o aplica no `signal`.
    Parâmetros:
        - H_est: Estimativa do canal para aplicar o receptor
        - signal: Sinal na qual processar o receptor
    Retorna:
        - sinal_estimado: O sinal estimado pelo receptor
    """
    # Error detection
    if type(H_est) != np.matrix:
        raise Exception("H_est type must be matrix")
    
    # Calculo do receptor
    receptor = np.linalg.inv(np.matmul(H_est.H,H_est))
    receptor = np.matmul(receptor,H_est.H)
    
    if signal:
        # Aplicacao do receptor ao resultado
        return np.matmul(receptor[np.newaxis,:,:],np.swapaxes(signal,1,0)[:,:,np.newaxis])
    
    return receptor

def ReceptorMRC(H_est,signal=None):
    """
    ReceptorMRC(H_est,signal)
    Descrição: 
        Calcula o receptor MRC com base em `H_est` e aplica em `signal`
        Mesmos parametros e retorno de `ReceptorZF`
    """
    # Error detection
    if type(H_est) != np.matrix:
        raise Exception("H_est type must be matrix")
    
    # Calculo do receptor
    receptor = H_est.H
    
    if signal:
        # Aplicacao do receptor ao resultado
        return np.matmul(receptor[np.newaxis,:,:],np.swapaxes(signal,1,0)[:,:,np.newaxis])
    
    return receptor

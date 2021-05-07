import numpy as np

class Fourier():
    @staticmethod
    def fast(data):
        return np.fft.fft(data)
    
    @staticmethod
    def fast2d(data):
        return np.fft.fft2(data)
    
    @staticmethod
    def inverse(data):
        return np.fft.ifft(data)
    
    @staticmethod
    def inverse2d(data):
        return np.fft.ifft2(data)
    
    @staticmethod
    def frequency(n):
        return np.fft.fftfreq(n)

    @staticmethod
    def real(data):
        return data.real
    
    @staticmethod
    def imaginary(data):
        return data.imag
    
    @staticmethod
    def magnitude(data):
        return np.abs(data)
    
    @staticmethod
    def phase(data):
        return np.angle(data)

    @staticmethod
    def magnitude_gain(data,factor):
        return Fourier.magnitude(data) * factor * np.exp(Fourier.phase(data) * 1j)
    
    @staticmethod
    def phase_gain(data,factor):
        return Fourier.magnitude(data) * np.exp(Fourier.phase(data) * factor * 1j)
    
    @staticmethod
    def real_gain(data,factor):
        return Fourier.real(data) * factor + Fourier.imaginary(data) * 1j
    
    @staticmethod
    def imaginary_gain(data,factor):
        return Fourier.real(data) + Fourier.imaginary(data) * factor * 1j
    
    @staticmethod
    def unimagnitude(data):
        return 1 * np.exp(Fourier.phase(data) * 1j)
    
    @staticmethod
    def uniphase(data):
        return Fourier.magnitude(data)
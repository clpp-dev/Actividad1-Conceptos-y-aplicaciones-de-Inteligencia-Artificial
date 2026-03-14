"""
Programa de ejemplo: Visualización de Funciones de Activación
Este programa demuestra el uso de NumPy y Matplotlib para visualizar
funciones de activación comúnmente usadas en Redes Neuronales.
"""

import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    """Función de activación Sigmoid"""
    return 1 / (1 + np.exp(-x))


def tanh(x):
    """Función de activación Tanh"""
    return np.tanh(x)


def relu(x):
    """Función de activación ReLU (Rectified Linear Unit)"""
    return np.maximum(0, x)


def main():
    # Generar datos usando NumPy
    x = np.linspace(-5, 5, 100)
    
    # Calcular las funciones de activación
    y_sigmoid = sigmoid(x)
    y_tanh = tanh(x)
    y_relu = relu(x)
    
    # Crear visualización usando Matplotlib
    plt.figure(figsize=(12, 4))
    
    # Subplot 1: Sigmoid
    plt.subplot(1, 3, 1)
    plt.plot(x, y_sigmoid, 'b-', linewidth=2)
    plt.grid(True, alpha=0.3)
    plt.title('Función Sigmoid')
    plt.xlabel('x')
    plt.ylabel('sigmoid(x)')
    
    # Subplot 2: Tanh
    plt.subplot(1, 3, 2)
    plt.plot(x, y_tanh, 'g-', linewidth=2)
    plt.grid(True, alpha=0.3)
    plt.title('Función Tanh')
    plt.xlabel('x')
    plt.ylabel('tanh(x)')
    
    # Subplot 3: ReLU
    plt.subplot(1, 3, 3)
    plt.plot(x, y_relu, 'r-', linewidth=2)
    plt.grid(True, alpha=0.3)
    plt.title('Función ReLU')
    plt.xlabel('x')
    plt.ylabel('ReLU(x)')
    
    plt.tight_layout()
    plt.savefig('funciones_activacion.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfica guardada como 'funciones_activacion.png'")
    plt.show()


if __name__ == "__main__":
    print("Generando visualización de funciones de activación...")
    print("Usando NumPy para cálculos y Matplotlib para visualización\n")
    main()

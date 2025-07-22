import cv2 # type: ignore
import numpy as np

# instale as dependências pip install opencv-python scikit-image
# Esse código imprime um valor entre -1 e 1, onde 1 significa imagens idênticas.


# Função para comparar duas imagens e detectar diferenças
def comparar_imagens(img1_path, img2_path):
    # Carrega as duas imagens
    imagem1 = cv2.imread(img1_path)
    imagem2 = cv2.imread(img2_path)

    # Verifica se as imagens têm o mesmo tamanho
    if imagem1.shape != imagem2.shape:
        print("As imagens têm tamanhos diferentes.")
        return

    # Converte para escala de cinza
    gray1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

    # Calcula a diferença absoluta
    diff = cv2.absdiff(gray1, gray2)

    # Threshold para realçar as diferenças
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Mostra as imagens
    cv2.imshow("Imagem 1", imagem1)
    cv2.imshow("Imagem 2", imagem2)
    cv2.imshow("Diferencas Detectadas", thresh)

    # Calcula porcentagem de semelhança
    total_pixels = gray1.size
    diferentes = np.count_nonzero(thresh)
    similaridade = ((total_pixels - diferentes) / total_pixels) * 100

    print(f"Similaridade: {similaridade:.2f}%")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemplo de uso
comparar_imagens('imagem1.jpg', 'imagem2.jpg')

programa {
  inclua biblioteca Graficos --> g
  inclua biblioteca Util --> u

  funcao lgbt() {
    g.iniciar_modo_grafico(verdadeiro)
    g.definir_dimensoes_janela(800, 600)
    
    g.definir_fonte_texto("Comic Sans MS")
    g.definir_tamanho_texto(48)
    enquanto (verdadeiro) {
      inteiro cores[6] = {0xE40303, 0xFF8C00, 0xFFED00, 0x008026, 0x004DFF, 0x750787}
      cadeia texto = "Você é LGBTQIAPN+"
      inteiro largura = g.largura_texto(texto)
      inteiro altura = 32
      inteiro x = 400 - largura / 2
      inteiro y = 300 + altura / 2
      inteiro transbordamento = 12

      para (inteiro i = 0; i < 6 ; i++) {
        g.definir_cor(cores[i])
        g.desenhar_retangulo(0, i * 100, 800, 100, falso, verdadeiro)
      }

      g.definir_cor(g.COR_BRANCO)
      g.desenhar_retangulo(x - transbordamento, y - altura - transbordamento, largura + transbordamento * 2, altura + transbordamento * 2, falso, verdadeiro)

      g.definir_cor(g.COR_PRETO)
      g.desenhar_texto(x, y, texto)

      g.renderizar()
    }
  }

  funcao inicio() {
    /*inteiro presente, i
    caracter resposta

    escreva("Você aceita o presente? (s/n): ")
    leia(resposta)
    
    se (resposta == "s") {
      para (i = 0; i < 4; i++) {
        escreva("PLAYSTATION! ")
        u.aguarde(1250)
      }
      
      presente = u.sorteia(0, 3)

      se (presente == 0) {
        escreva("\nO presente está vazio, que pena...")
      } senao se (presente == 1) {
        escreva("\nParabéns mano, você ganhou um PlayStation 5 Pro com GTA 6 comprado na pré-venda. Aproveite!")
      } senao se (presente == 2) {
        escreva("\nOloko mano, você adquiriu os poderes malignos do Tio Léo e do Geraldo. Use-os com sabedoria e moderação...")
      } senao {
        lgbt()
      }
    } senao se (resposta == "n") {
      escreva("Evapore então, seu merda.")
    } senao {
      escreva("Você só tinha UM trabalho, que era digitar o solicitado, e não o fez... (s/n)")
    } */
    lgbt()
  }
}

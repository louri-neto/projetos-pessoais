programa {
  inclua biblioteca Graficos --> g
  inclua biblioteca Util --> u

  funcao lgbt() {
    inteiro cores[6][3] = {
      {228, 3, 3},
      {255, 140, 0},
      {255, 237, 0},
      {0, 128, 38},
      {0, 76, 255},
      {119, 0, 136}
    }

    g.iniciar_modo_grafico(verdadeiro)
    g.definir_dimensoes_janela(640, 480)
    
    g.definir_fonte_texto("Comic Sans MS")
    g.definir_tamanho_texto(40)

    enquanto (verdadeiro) {
      para (inteiro i = 0; i < 6 ; i++) {
        g.definir_cor(g.criar_cor(cores[i][0], cores[i][1], cores[i][2]))
        g.desenhar_retangulo(0, i * 80, 640, 480, falso, verdadeiro)
      }

      g.definir_cor(g.COR_BRANCO)
      g.desenhar_retangulo(120, 200, 410, 80, falso, verdadeiro)

      g.definir_cor(g.COR_PRETO)
      g.desenhar_texto(127, 253, "Você é LGBTQIAPN+")

      g.renderizar()
    }
  }

  funcao inicio() {
    inteiro presente, i
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
    }
  }
}

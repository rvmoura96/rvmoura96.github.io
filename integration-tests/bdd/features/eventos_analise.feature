Funcionalidade: Eventos da tela análise

Cenário: Validando evento de Pageview
  Quando acesso a home
  E clico no botão para a próxima página
  Então deverá ser enviado um evento de Pageview
    | tipo     |
    | pageview |

Cenário: Validando evento do botão Lorem
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão "Lorem"
  Então deverá ser enviado o seguinte evento
    | categoria | ação     | rótulo |
    | analise   | ver_mais | Lorem  |

Cenário: Validando evento do botão Ipsum
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão "Ipsum"
  Então deverá ser enviado o seguinte evento
    | categoria | ação     | rótulo |
    | analise   | ver_mais | Ipsum  |

Cenário: Validando evento do botão Dolor
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão "Dolor"
  Então deverá ser enviado o seguinte evento
    | categoria | ação     | rótulo |
    | analise   | ver_mais | Dolor  |

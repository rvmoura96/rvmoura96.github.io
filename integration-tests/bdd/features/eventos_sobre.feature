Funcionalidade: Eventos da tela análise

Cenário: Validando evento de Pageview
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão para a próxima página
  Então deverá ser enviado um evento de Pageview
    | tipo     |
    | pageview |


Cenário: Validando evento do campo nome
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão para a próxima página
  Quando preencho o campo "nome"
  Então deverá ser enviado o seguinte evento
    | categoria | ação | rótulo    |
    | contato   | nome | preencheu |

Cenário: Validando evento do campo email
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão para a próxima página
  Quando preencho o campo "email"
  Então deverá ser enviado o seguinte evento
    | categoria | ação  | rótulo    |
    | contato   | email | preencheu |

Cenário: Validando evento do campo telefone
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão para a próxima página
  Quando preencho o campo "telefone"
  Então deverá ser enviado o seguinte evento
    | categoria | ação     | rótulo    |
    | contato   | telefone | preencheu |

Cenário: Validando evento do campo aceito
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão para a próxima página
  Quando preencho o campo "aceito"
  Então deverá ser enviado o seguinte evento
    | categoria | ação     | rótulo    |
    | contato   | aceito   | preencheu |


Cenário: Validando evento do modal
  Quando acesso a home
  E clico no botão para a próxima página
  E clico no botão para a próxima página
  E preencho o campo "nome"
  E preencho o campo "email"
  E preencho o campo "telefone"
  E preencho o campo "aceito"
  E clico no botão submit
  Então deverá ser enviado o seguinte evento
    | categoria | ação    | rótulo  |
    | contato   | enviado | enviado |

Funcionalidade: Eventos globais

Cenário: Validando evento de pageview na home
  Quando acesso a home
  Então deverá ser enviado um evento de Pageview
    | tipo     |
    | pageview |

Cenário: Validando evento de download
  Dado que acesse a home
  Quando clico no botão de "download"
  Então deverá ser enviado o seguinte evento
    | categoria | ação         | rótulo       |
    | menu      | download_pdf | download_pdf |

Cenário: Validando evento de download
  Dado que acesse a home
  Quando clico no botão de "download"
  Então deverá ser enviado o seguinte evento
    | categoria | ação         | rótulo       |
    | menu      | download_pdf | download_pdf |


Cenário: Validando evento de contato
  Dado que acesse a home
  Quando clico no botão de "contato"
  Então deverá ser enviado o seguinte evento
    | categoria | ação             | rótulo       |
    | menu      | entre_em_contato | link_externo |

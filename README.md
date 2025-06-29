# Projeto de Estudo de Padrões de Desenvolvimento

## Integrante do Grupo
* **Nome:** Henrique Fonseca da Silveira

---

## Padrão de Projeto Estudado: Singleton (Criacional)

### Definição
O padrão **Singleton** é um padrão de projeto criacional que garante que uma classe tenha apenas uma única instância em toda a aplicação e fornece um ponto de acesso global para essa instância. Isso é útil quando você precisa de um controle estrito sobre um recurso compartilhado, como uma conexão de banco de dados, um gerenciador de configurações ou, no nosso caso, um sistema de log.

### Cenário de Aplicação
Imagine um sistema de log para uma aplicação. Não faz sentido ter múltiplas instâncias do logger, pois cada uma poderia tentar gerenciar o mesmo arquivo de log de forma independente, causando erros ou perda de informações. Com o Singleton, garantimos que todas as partes do código usem o mesmo objeto para escrever os logs.

### Implementação em Python
Este projeto demonstra a implementação de um logger de duas maneiras: sem o padrão Singleton e com o padrão.

* **Solução sem o padrão (`solucao_sem_padrao.py`):** Mostra como é possível criar múltiplas instâncias da classe `Logger`, o que pode ser ineficiente e levar a problemas em um cenário real.
* **Solução com o padrão (`solucao_com_padrao.py`):** Apresenta a implementação do Singleton, garantindo que apenas uma instância da classe `LoggerSingleton` seja criada e reutilizada.

Para executar os códigos, basta rodar os arquivos Python:
`python solucao_sem_padrao.py`
`python solucao_com_padrao.py`

### Análise Crítica (Pontos Fortes e Fracos)

**Pontos Fortes:**
* **Controle de Instância:** Garante que haja apenas uma instância, o que é ideal para recursos compartilhados.
* **Ponto de Acesso Global:** Facilita o acesso à instância de qualquer parte do código.
* **Economia de Recursos:** Evita a criação desnecessária de objetos, economizando memória.

**Pontos Fracos:**
* **Quebra do Princípio da Responsabilidade Única:** A classe se torna responsável não apenas por sua lógica, mas também por controlar sua própria criação.
* **Dificulta Testes:** A natureza global do Singleton pode dificultar a criação de testes de unidade, pois as instâncias são "fixas".
* **Acoplamento:** O código que depende do Singleton fica fortemente acoplado a ele, reduzindo a flexibilidade.

## Conclusões
O padrão Singleton é uma ferramenta poderosa para resolver problemas específicos, como o gerenciamento de recursos globais. No entanto, sua aplicação deve ser considerada com cuidado devido aos seus pontos fracos, especialmente em relação a testes e acoplamento. Entender quando e por que usá-lo é crucial para o desenvolvimento de software robusto.

## Apresentação do Projeto
**Link para o vídeo da apresentação:** https://youtu.be/BHR9AiaJv2s

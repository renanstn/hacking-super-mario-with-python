# Hacking Super Mario World with Python

![screenshot](https://github.com/renanstd/hacking-super-mario-with-python/blob/master/screenshots/screen01.png)

Script feito em python, que se conecta ao processo de um emulador **snes9x** rodando **Super Mario World**, e altera os valores de moedas e status do Mario.

- Mantém as moedas sempre em 99, assim, qualquer moeda que você pegue, ganha uma vida
- Mantém o Mario sempre com a capa, mesmo que você seja atingido, você nunca perde a capa, ficando assim invencível.

Este estudo foi possível graças a [este](https://github.com/danilo94/SuperMarioHack) repositório, utilizado [neste](https://www.youtube.com/watch?v=T2NMErG2cJY) vídeo onde tal proposta é apresentada e explicada (agadecimentos ao [Dan Maker](https://github.com/danilo94)). Porém, fiz várias correções e adaptações ao código para facilitar a minha própria compreensão do mesmo.

## Como funciona

Para que este script funcione, você precisa encontrar os **endereços de memória** no emulador, que armazenam a quantidade de moedas, e o status do Mario. Este processo geralmente é fácil de fazer se você utilizar o [Cheat Engine](https://www.cheatengine.org/), você pode aprender como fazer isso [aqui](https://www.youtube.com/watch?v=4jZE6XP0_QQ).

Após encontrar os endereços, mantenha o emulador aberto, e insira os mesmos no arquivo `src/addresses.py`, nos campos `COINS` e `STATUS`.

Ao executar o script, ele irá se conectar com o processo do snes9x, e constantemente ler e sobrescrever na memória os valores de moedas e o status do Mario.

## Executando

- (Opcional) Crie e inicialize um ambiente virtual
```
python -m venv venv
venv\Scripts\activate
```
- Instale as dependências
```
pip install -r requirements.txt
```

- Execute
```
python src/main.py
```

## Observação

Este projeto funciona somente em **Windows**.

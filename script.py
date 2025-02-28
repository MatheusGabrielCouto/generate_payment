import json
from PIL import Image, ImageDraw, ImageFont
import os
import uuid

# Carregar transações do JSON
with open('transacoes.json', 'r', encoding='utf-8') as file:
    transacoes = json.load(file)

# Carregar imagem modelo
modelo_path = 'pix.jpg'

# Definir fonte (ajuste conforme seu sistema)
fontTitle = ImageFont.truetype('fonts/Roboto-SemiBold.ttf', 60)
font = ImageFont.truetype('fonts/Roboto-Regular.ttf', 50)
fontId = ImageFont.truetype('fonts/Roboto-Regular.ttf', 45)

fontEstorno = ImageFont.truetype('fonts/Roboto-Medium.ttf', 50)


for i, transacao in enumerate(transacoes):
    image = Image.open(modelo_path)
    draw = ImageDraw.Draw(image)
    new_uuid = uuid.uuid4()

    draw.text((64, 200), transacao['titulo'], font=fontTitle, fill='black')
    draw.text((74, 590), transacao['data'], font=font, fill='black')
    draw.text((74, 730), f'R$ {transacao['valor']}', font=font, fill='black')
    draw.text((74, 970), transacao['nome_recebedor'], font=font, fill='black')
    draw.text((144, 1160), transacao['cpf_cnpj_recebedor'], font=font, fill='black')
    draw.text((74, 1290), transacao['instituicao_recebedor'], font=font, fill='black')

    draw.text((74, 1575), transacao['nome_remetente'], font=font, fill='black')
    draw.text((144, 1775), transacao['cpf_cnpj_remetente'], font=font, fill='black')
    draw.text((74, 1915), transacao['instituicao_remetente'], font=font, fill='black')
    draw.text((74, 2155), f'{new_uuid}', font=fontId, fill='black')

    if transacao['estorno']:
        draw.text((74, 440), 'Valor Estornado', font=fontEstorno, fill='#F99F1C')
        pass

    image.save(f'comprovantes/{new_uuid}.jpg')


os.makedirs("comprovantes", exist_ok=True)



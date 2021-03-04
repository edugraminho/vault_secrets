import os
import hvac
from requests.exceptions import ConnectionError
from hvac.exceptions import InvalidPath

token = os.environ.get('HCV_TOKEN')
print(token)

try:
    client = hvac.Client(
        token=token
    )
    print(client.is_authenticated())
    if not client.is_authenticated():
        raise ValueError('Verifique seu Token')
except ConnectionError as e:
    print('Verifique se o Vault esta em execucao e se as variaveis de ambiente, descritas na documentacao, estao configuradas')

try:
    hvreponse = \
        client.secrets.kv.read_secret_version(path='opme')
    print(hvreponse['data']['data'])
except InvalidPath as e:
    msg = f'Verifique se o path {path} esta criado no vault seguindo o '
    f'padrao da documentacao dessa lib'
    logger.error(f'{e}\n{msg}')
except KeyError as e:
    logger.error(f'Ocorreu um erro ao extrair os dados da '
                 f'resposta {hvreponse}\n '
                 f'Verifique a resposta')
    raise e

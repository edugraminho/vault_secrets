1- Baixar o Vault - https://www.vaultproject.io/downloads


2- Colocar o arquivo .exe dentro de uma pasta: C:\Vault


3- Adicionar dentro de uma variável de amb do sistema 
Path > “Editar” > “Novo” > C:\Vault

    Para testar abre o terminal e digita>  vault

    Deve aparecer algo assim...
``` 
    read        Read data and retrieves secrets
    write       Write data, configuration, and secrets
    delete      Delete secrets and configuration
    list        List data or secrets
    login       Authenticate locally
    agent       Start a Vault agent
    server      Start a Vault server
    status      Print seal and HA status
    unwrap      Unwrap a wrapped secret

Other commands:
    audit          Interact with audit devices
    auth           Interact with auth methods
    debug          Runs the debug command
    kv             Interact with Vault's Key-Value storage
    lease          Interact with leases
    monitor        Stream log messages from a Vault server
    namespace      Interact with namespaces
    operator       Perform operator-specific tasks
    path-help      Retrieve API help for paths
    plugin         Interact with Vault plugins and catalog
    policy         Interact with policies
    print          Prints runtime configurations
    secrets        Interact with secrets engines
    ssh            Initiate an SSH session
    token          Interact with tokens
```

4- Dentro de C:\Vault criar uma pasta “data” 

5- Dentro de C:\Vault criar um arquivo config.hcl, com esse script:
```
    storage "file" {
    path    = "./data"
    }

    listener "tcp" {
    address     = "127.0.0.1:8200"
    tls_disable = 1
    }

    disable_mlock = true

    api_addr = "http://127.0.0.1:8200"
    ui = true
```

6- Em Variável de amb do Sistema ou de Usuario
Novo >
Nome da Var:    VAULT_ADDR
Valor da Var:   http://127.0.0.1:8200

    Para testar, abre o powershell:
    $Env:VAULT_ADDR
    deve aparecer "http://127.0.0.1:8200"


7- Abre o terminal no caminho: 
    C:\Vault>  
e digita:   
    vault server -config='config.hcl'

    E DEIXA ABERTO!!

    deve aparecer algo assim:

    ```
    ==> Vault server configuration:

             Api Address: http://127.0.0.1:8200
                     Cgo: disabled
         Cluster Address: https://127.0.0.1:8201
              Go Version: go1.15.7
              Listener 1: tcp (addr: "127.0.0.1:8200", cluster address: "127.0.0.1:8201", max_request_duration: "1m30s", max_request_size: "33554432", tls: "disabled")
               Log Level: info
                   Mlock: supported: false, enabled: false
           Recovery Mode: false
                 Storage: file
                 Version: Vault v1.6.3
             Version Sha: .............

    ==> Vault server started! Log data will stream in below:

        2021-03-04T11:34:02.076-0300 [INFO]  proxy environment: http_proxy= https_proxy= no_proxy=
    ```

8- Com o terminal aberto, abre um novo terminal e digita esse comando:
    vault operator init -key-shares=1 -key-threshold=1

    Ele te dara essa Key e esse Token, salve em algum lugar.

    Unseal Key 1: ....
    Initial Root Token: ....


9- Agora com seu Token e sua Key, vc armazena em uma var de ambiente
    - HCV_SEAL  com o valor da Unseal Key 1:
    - HCV_TOKEN com o valor da Initial Root Token:

    teste em seu terminal $env:

10- No seu Navegador entra em http://127.0.0.1:8200/ui/
    primeiro campo coloca seu Unseal Key 1

    vai abrir uma caixa de login:
    Token
    Seu:    Initial Root Token


11- Vai abrir Secrets Engines. Clica em >  Enable new engine +   >   KV   >    Next
    Em Path:    secret
    Version     2

    Enable Engine

12- Em secret clica em  >   Create secret +
    Path for this secret    >   opme
    Maximum Number of Versions  >  20

    para testar
    Version data
    Key:    User
    Value:    t01202

    Add 
    Save

13- Abra o arquivo test_vault pelo terminal > instala o virtualenv > ativa a maq virtual
    instala o requests e o hvac
    pip install hvac requests

    executa esse script

14- este arquivo vault_runner cria um powershell e inicia o servidor e outro para desbloquear

15- Vai em Agendador de Tarefas (exec como ADM)
    Clica com o direito em cima de Biblioteca do Agendador > Cria uma pasta RPA_TOOLS
    Clica com o direitor RPA_TOOLS > criar nova tarefa
    > Geral
    Nome: Vault
        Executar usuario conectado ou nao 
        Conf para Win 10

    > Disparador
        Novo
        Seleciona > Ao Inicializar e OK

    > Acoes
        Novo
        Iniciar um Programa
        Procurar:   C:\Vault\vault_runner.bat
        iniciar em:     C:\Vault

    > Condicoes
        Tirar a "interrompoer se o comp passar a usar a bateria"
        Marcar Iniciar somente se a seguinte conecao estiver disponivel

    > se vc nao tiver senha de usuario vai em 
        Adicionar ou remover usuarios > Opcoes de entrada > Senha

    > se precisar finalizar vai no gerenciador de tarefas do Win e encontra o vault.exe


16- Finalizado isso vc pode criar as secrets do projeto que esta trabalhando junto com a equipe.
    > Secrets
    > Create Secret + 
    > JSON 
        E cola as secrets do Projeto...

document.addEventListener('DOMContentLoaded', function() {
    // Selecionando o formulário e os campos
    const form = document.querySelector('form');
    const nomeInput = form.querySelector('input[name="nome"]');
    const enderecoInput = form.querySelector('input[name="endereco"]');

    // Função para exibir uma mensagem de erro
    function exibirErro(campo, mensagem) {
        let erro = campo.nextElementSibling; // Procurar a mensagem de erro depois do campo
        if (!erro || !erro.classList.contains('error-message')) {
            erro = document.createElement('span');
            erro.classList.add('error-message');
            campo.parentNode.appendChild(erro);
        }
        erro.textContent = mensagem;
    }

    // Função para limpar mensagens de erro
    function limparErros() {
        const mensagensErro = document.querySelectorAll('.error-message');
        mensagensErro.forEach(function(mensagem) {
            mensagem.remove();
        });
    }

    // Validar campos ao submeter
    form.addEventListener('submit', function(event) {
        limparErros(); // Limpa qualquer erro anterior

        let valido = true;
        
        // Validar nome
        if (nomeInput.value.trim() === '') {
            exibirErro(nomeInput, 'O nome da empresa é obrigatório.');
            valido = false;
        }

        // Validar endereço
        if (enderecoInput.value.trim() === '') {
            exibirErro(enderecoInput, 'O endereço é obrigatório.');
            valido = false;
        }

        // Se o formulário não for válido, previne o envio
        if (!valido) {
            event.preventDefault();
        } else {
            // Confirmação antes de enviar
            const confirmacao = confirm('Você tem certeza que deseja cadastrar a empresa?');
            if (!confirmacao) {
                event.preventDefault(); // Impede o envio do formulário se o usuário cancelar
            }
        }
    });
});
document.addEventListener('DOMContentLoaded', function() {
    // Selecionando o formulário e o campo de endereço
    const form = document.querySelector('form');
    const enderecoInput = form.querySelector('input[name="endereco"]');

    // Função para exibir uma mensagem de erro
    function exibirErro(campo, mensagem) {
        let erro = campo.nextElementSibling; // Procurar a mensagem de erro depois do campo
        if (!erro || !erro.classList.contains('error-message')) {
            erro = document.createElement('span');
            erro.classList.add('error-message');
            campo.parentNode.appendChild(erro);
        }
        erro.textContent = mensagem;
    }

    // Função para limpar mensagens de erro
    function limparErros() {
        const mensagensErro = document.querySelectorAll('.error-message');
        mensagensErro.forEach(function(mensagem) {
            mensagem.remove();
        });
    }

    // Validar campo ao submeter
    form.addEventListener('submit', function(event) {
        limparErros(); // Limpa qualquer erro anterior

        let valido = true;
        
        // Validar endereço
        if (enderecoInput.value.trim() === '') {
            exibirErro(enderecoInput, 'O endereço do local é obrigatório.');
            valido = false;
        }

        // Se o formulário não for válido, previne o envio
        if (!valido) {
            event.preventDefault();
        } else {
            // Confirmação antes de enviar
            const confirmacao = confirm('Você tem certeza que deseja cadastrar o local de reciclagem?');
            if (!confirmacao) {
                event.preventDefault(); // Impede o envio do formulário se o usuário cancelar
            }
        }
    });
});

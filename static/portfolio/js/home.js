document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('skillsChart');
    if (!canvas) return;

    const labels = JSON.parse(canvas.dataset.labels);
    const values = JSON.parse(canvas.dataset.values);
    const colors = JSON.parse(canvas.dataset.colors);

    new Chart(canvas, {
        type: 'doughnut',
        data: {
            labels,
            datasets: [{
                data: values,
                backgroundColor: colors,
                borderWidth: 0
            }]
        },
        options: {
            cutout: '65%',
            plugins: {
            legend: {
            display: false
        }
    }
        }
    });
});

/* botão menu hamburguer */
function animar() {
    document.querySelector('.btn-hamburguer')
        .classList.toggle('ativar');

    document.getElementById('menu-hamb')
        .classList.toggle('ativar');

    document.querySelector('.opcoes-hamburguer')
        .classList.toggle('ativar');
}

const btnHamb = document.getElementById('menu-hamb');
const menu = document.querySelector('.opcoes-hamburguer');
const container = document.querySelector('.btn-hamburguer');

btnHamb.addEventListener('click', (e) => {
    e.stopPropagation(); 

    container.classList.toggle('ativar');
    btnHamb.classList.toggle('ativar');
    menu.classList.toggle('ativar');
});


document.addEventListener('click', (e) => { /* para fechar o menu ao clicar fora */
    if (!container.contains(e.target)) {
        container.classList.remove('ativar');
        btnHamb.classList.remove('ativar');
        menu.classList.remove('ativar');
    }
});

menu.querySelectorAll('a').forEach(link => {  /* fechar ao clicar em algum link do menu */
    link.addEventListener('click', () => {
        container.classList.remove('ativar');
        btnHamb.classList.remove('ativar');
        menu.classList.remove('ativar');
    });
});


/* Texto dinamico */
const textos = ["estudante de sistemas de informação", "desenvolvedor de software"];
const velocidadeDigitacao = 100; // velocidade da digitação
const velocidadeApagar = 50;   // velocidade de apagar
const delayApagar = 1500;       // pausa antes de apagar

let textIndex = 0;
let charIndex = 0;
let isDeleting = false;

const textoAnimado = document.getElementById("texto-animado");

function type() {
    const current = textos[textIndex];

    if (!isDeleting) {
        textoAnimado.textContent = current.substring(0, charIndex + 1);
        charIndex++;

        if (charIndex === current.length) {
            isDeleting = true;
            setTimeout(type, delayApagar);
        } else {
            setTimeout(type, velocidadeDigitacao);
        }
    } else {
        textoAnimado.textContent = current.substring(0, charIndex - 1);
        charIndex--;

        if (charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % textos.length;
            setTimeout(type, velocidadeDigitacao);
        } else {
            setTimeout(type, velocidadeApagar);
        }
    }
}

type();


/* Header animado */
const header = document.getElementById("header");

if (header) {
    window.addEventListener("scroll", () => {
        if (window.scrollY > 50) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    });
}


/* fetch */
const form = document.querySelector(".form-contato");

form.addEventListener("submit", function (event) {

    event.preventDefault(); /* intercepta o submit */

    const formData = new FormData(form);

    fetch("", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": form.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    
    .then(response => response.json())
    .then(data => {
        console.log("Resposta:", data);

        if (data.status === "ok") {
            mostrarOverlay();
            form.reset();
        }
    })
    .catch(error => {
        console.error(error);
        alert("Erro ao enviar");
    });
});

/* função para mostrar a mensagem de sucesso */
function mostrarOverlay(){
    const toast = document.querySelector(".form-overlay");
    toast.classList.add("ativo");

    setTimeout(() => {
        toast.classList.remove("ativo"); 
    }, 3000);
}



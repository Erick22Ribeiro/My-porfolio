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



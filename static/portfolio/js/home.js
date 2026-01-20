/* Grafico desktop */
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

/* Grafico mobile */
document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('skillsChart-2');
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
const textosPorIdioma = {
    pt: [
        "estudante de sistemas de informação",
        "desenvolvedor backend"
    ],
    en: [
        "information systems student",
        "backend developer"
    ]
};

let idiomaAtual = localStorage.getItem("lang") || "pt";

let textos = textosPorIdioma[idiomaAtual];

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
            typingTimeout = setTimeout(type, delayApagar);
        } else {
            typingTimeout = setTimeout(type, velocidadeDigitacao);
        }

    } 
    else {
        textoAnimado.textContent = current.substring(0, charIndex - 1);
        charIndex--;

        if (charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % textos.length;
            typingTimeout = setTimeout(type, velocidadeDigitacao);
        } else {
            typingTimeout = setTimeout(type, velocidadeApagar);
        }
    }
}

let typingTimeout;

type();

document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
        clearTimeout(typingTimeout);
    } else {
        type();
    }
});



/* Header animado */
const header = document.getElementById("header");

let headerAtivo = false;

window.addEventListener("scroll", () => {
    if (window.scrollY > 50 && !headerAtivo) {
        header.classList.add("scrolled");
        headerAtivo = true;
    } 
    else if (window.scrollY <= 50 && headerAtivo) {
        header.classList.remove("scrolled");
        headerAtivo = false;
    }
});



/* fetch */
const form = document.querySelector(".form-contato"); /* Desativar o botão + animação enviando */
const btnEnviar = document.querySelector('.btn-enviar');
const enviarText = document.querySelector('.text-enviar');

form.addEventListener("submit", function (event) {

    event.preventDefault(); /* intercepta o submit */

    btnEnviar.disabled = true;
    btnEnviar.classList.add("loading");
    enviarText.classList.add("remover-text") /* remove o texto do btn */

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

            btnEnviar.disabled = false;
            btnEnviar.classList.remove("loading");
            enviarText.classList.remove("remover-text") /* adiciona novamente o texto do btn */
        }
    })
    .catch(error => {
        console.error(error);
        alert("Erro ao enviar");

        btnEnviar.disabled = false;
        btnEnviar.classList.remove("loading");
        enviarText.classList.remove("remover-text") /* adiciona novamente o texto do btn */
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




/* TRADUÇãO */
function toggleLanguage() {
    const currentLang = document.documentElement.lang || "pt";
    const newLang = currentLang === "pt" ? "en" : "pt";
    setLanguage(newLang);
}


const translationsCache = {};

async function setLanguage(lang) {
    // Busca traduções do Django
    let data;

    if (translationsCache[lang]) {
        data = translationsCache[lang];
    } 
    else {
        const response = await fetch(`/?translations=true&lang=${lang}`);
        data = await response.json();
        translationsCache[lang] = data;
    }

    
    /* console.log('Dados recebidos:', data); */ /* pra mostrar os objetos recebidos no console(debug) */
    
    // Traduz textos estáticos (menu, topo, hab, sobre)
    document.querySelectorAll("[data-i18n]").forEach(el => {

        const keys = el.dataset.i18n.split(".");
        let text = data.static;
        
        keys.forEach(k => { /* k = key, nome da variável que representa cada parte do caminho */
            text = text?.[k];
        });
        
        if (text) {
            el.textContent = text;
        }

    });

    //Traduz placeholders
    document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
        const keys = el.dataset.i18nPlaceholder.split("."); /* split separa a string em várias partes, pega o valores e divide removendo o . / topo.ola = ["topo", "ola"] */
        let text = data.static;
        
        keys.forEach(k => { 
            text = text?.[k];
        });
        
        if (text) {
            el.setAttribute('placeholder', text);  // Usa setAttribute em vez de textContent
        }
    });
    
    // Traduz projetos dinâmicos
    data.projetos.forEach(projeto => {

        /* busca o card do projeto no html */
        const projetoEl = document.querySelector(`[data-projeto-id="${projeto.id}"]`);
        
        if (projetoEl) {
            const tituloEl = projetoEl.querySelector('.titulo');
            const descricaoEl = projetoEl.querySelector('.descricao');
            
            if (tituloEl) tituloEl.textContent = projeto.titulo;
            if (descricaoEl) descricaoEl.textContent = projeto.descricao;
        }
    });

    document.documentElement.lang = lang;
    localStorage.setItem("lang", lang);
    
    // Atualiza textos da animação
    idiomaAtual = lang;
    textos = textosPorIdioma[lang];
    
    // Reset animação
    textIndex = 0;
    charIndex = 0;
    isDeleting = false;

    /* btn idioma */
    ["btn-lang", "btn-lang-mobile"].forEach(id => {
    const btn = document.getElementById(id);
    if (btn) {
        btn.classList.toggle("en", lang === "en");
    }
    });


}

// Carrega idioma salvo, ao abrir vai estar no idioma definido antes
const savedLang = localStorage.getItem("lang") || "pt";
setLanguage(savedLang);


function moveChart() {
    const canvas = document.getElementById('skillsChart');
    const desktop = document.querySelector('.desktop-anchor');
    const mobile = document.querySelector('.mobile-anchor');

    if (!canvas || !desktop || !mobile) return;

    if (window.innerWidth <= 768) {
        mobile.appendChild(canvas);
    } else {
        desktop.appendChild(canvas);
    }
}

window.addEventListener('load', moveChart);
window.addEventListener('resize', moveChart);

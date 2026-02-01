import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="💝 Saint-Valentin", page_icon="💝", layout="centered")

# CSS et JavaScript personnalisé
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        padding: 20px;
        font-family: 'Arial', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .container {
        text-align: center;
        background: white;
        padding: 50px;
        border-radius: 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        position: relative;
        overflow: visible;
    }
    
    h1 {
        color: #e91e63;
        font-size: 2.5em;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .emoji {
        font-size: 80px;
        margin-bottom: 20px;
        animation: heartbeat 1.5s infinite;
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .buttons-container {
        margin-top: 40px;
        position: relative;
        height: 300px;
    }
    
    button {
        font-size: 1.2em;
        padding: 15px 40px;
        margin: 10px;
        border: none;
        border-radius: 50px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: bold;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
    }
    
    #btnOui {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        top: 50px;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
    }
    
    #btnOui:hover {
        transform: translateX(-50%) scale(1.1);
        box-shadow: 0 15px 40px rgba(245, 87, 108, 0.6);
    }
    
    #btnNon {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        color: #666;
        top: 150px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .celebration {
        display: none;
        text-align: center;
    }
    
    .celebration h2 {
        color: #e91e63;
        font-size: 3em;
        animation: bounce 0.5s;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    .hearts {
        font-size: 50px;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
</style>
</head>
<body>
<div class="container">
    <div id="question">
        <div class="emoji">💝</div>
        <h1>Veux-tu être ma Valentine ? 🌹</h1>
        <div class="buttons-container">
            <button id="btnOui" onclick="direOui()">Oui ! 💕</button>
            <button id="btnNon">Non...</button>
        </div>
    </div>
    
    <div id="celebration" class="celebration">
        <h2>Yaaaay ! 🎉</h2>
        <div class="hearts">💖 💝 💗 💓 💞</div>
        <p style="font-size: 1.5em; color: #e91e63; margin-top: 20px;">
            Je savais que tu dirais oui ! 😊
        </p>
    </div>
</div>

<script>
    const btnNon = document.getElementById('btnNon');
    const btnOui = document.getElementById('btnOui');
    let ouiScale = 1;
    
    btnNon.addEventListener('mousemove', function(e) {
        const rect = btnNon.getBoundingClientRect();
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        const btnCenterX = rect.left + rect.width / 2;
        const btnCenterY = rect.top + rect.height / 2;
        
        const distance = Math.sqrt(
            Math.pow(mouseX - btnCenterX, 2) + 
            Math.pow(mouseY - btnCenterY, 2)
        );
        
        // Si la souris est proche du bouton Non (moins de 100px)
        if (distance < 100) {
            // Agrandir le bouton Oui
            ouiScale += 0.05;
            btnOui.style.transform = `translateX(-50%) scale(${ouiScale})`;
            
            // Déplacer le bouton Non aléatoirement
            const container = btnNon.parentElement;
            const containerRect = container.getBoundingClientRect();
            
            const maxX = containerRect.width - rect.width;
            const maxY = containerRect.height - rect.height;
            
            const newLeft = Math.random() * maxX;
            const newTop = Math.random() * maxY;
            
            btnNon.style.left = newLeft + 'px';
            btnNon.style.top = newTop + 'px';
            btnNon.style.transform = 'none';
        }
    });
    
    // Au cas où quelqu'un clique sur Non
    btnNon.addEventListener('click', function() {
        ouiScale += 0.3;
        btnOui.style.transform = `translateX(-50%) scale(${ouiScale})`;
        
        const container = btnNon.parentElement;
        const rect = btnNon.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();
        
        const newLeft = Math.random() * (containerRect.width - rect.width);
        const newTop = Math.random() * (containerRect.height - rect.height);
        
        btnNon.style.left = newLeft + 'px';
        btnNon.style.top = newTop + 'px';
        btnNon.style.transform = 'none';
    });
    
    function direOui() {
        document.getElementById('question').style.display = 'none';
        document.getElementById('celebration').style.display = 'block';
        
        // Créer des confettis
        createConfetti();
    }
    
    function createConfetti() {
        const colors = ['#e91e63', '#f093fb', '#f5576c', '#ff6b9d', '#ffc0cb'];
        for (let i = 0; i < 50; i++) {
            setTimeout(() => {
                const confetti = document.createElement('div');
                confetti.style.position = 'fixed';
                confetti.style.left = Math.random() * 100 + '%';
                confetti.style.top = '-10px';
                confetti.style.width = '10px';
                confetti.style.height = '10px';
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.borderRadius = '50%';
                confetti.style.pointerEvents = 'none';
                confetti.style.zIndex = '1000';
                document.body.appendChild(confetti);
                
                const duration = Math.random() * 3 + 2;
                const animation = confetti.animate([
                    { transform: 'translateY(0) rotate(0deg)', opacity: 1 },
                    { transform: `translateY(${window.innerHeight + 50}px) rotate(${Math.random() * 360}deg)`, opacity: 0 }
                ], {
                    duration: duration * 1000,
                    easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
                });
                
                animation.onfinish = () => confetti.remove();
            }, i * 30);
        }
    }
</script>
</body>
</html>
"""

# Afficher le composant HTML
components.html(html_code, height=800, scrolling=False)

// Mapeamento de doramas para IDs do YouTube (originais do app)
const doramaVideos = {
  'Ele a Procurou por Todo Esse Tempo': 'VLTvfq8IrLo',
  'Fuga do Casamento': 'ZyfWKGuH7GY',
  'Herdeira de Bilhões': 'RPn1a_FAWMQ',
  'Mimada como uma Rainha': 'UEkkVyFBdBc',
  'Um Tapa no CEO': '09iQYTcZfsg',
  'A Faxineira e o Bilionário': 'nsHJX5QGhYc',
  'Atropelada e Casada num Flash': 'XtzPQ-VXqPk',
  'A Mesa Errada': 'emywT4z7Eps',
  'A Mesa Errada (Parte 2)': '5YQbwGcAm-M',
  'O CEO Entregador': '9XfWAkwN4Ms',
  'Vingança Bilionária': '7BYqD6rhlw0',
  'Salvo do Fogo': 't3Kd5-vI6zc',
  'A Mãe Escolhida': 'SanSc_fZlgA',
  'O CEO que Fingiu ser Cego': 'z06aaEgKnyk',
  'Vingança em Kung-Fu': 'tnbIP95rYPM',
  'Um Favor de Bilhões': '1O73X_1HAG8',
  'Forçada a Casar com o CEO': 'IEnw0cHqeJQ',
  'A Enfermeira e o CEO': 'KiZVO_nLLDg',
  'Coach de Amor': '2Qjazbyy6F0',
  'Belas Espiãs': 'E519D8qHTnE',
  'Uma Tigela de Chá': 'NZ8BMz6yIis',
  'Vendida para o Campo': 'GH1y7hsZDV4',
  'A Garota do Taco': 'CR7tQD2w2vk',
  'Ela Salvou um Bilionário': 'KBFARvbxTNA',
  'A Confeiteira Traída': 'dCqEq8tzFJo',
  'O Casamento Recusado': '1JFLVEs8izM',
  'A CEO Disfarçada de Estudante': 'T9ye-RPMWQI',
  'A Esposa Ignorada': 'pMhil8m_CzU',
  'A Irmã e a CEO': 'FUE_6Ls--TI',
  'Humilhada na Empresa': 'pBfEXXTZh7c',
  'Casamento pela Mãe': 'jf-Nsn14aLc',
  'O Marido Contratado': 'B3Tv0dm3HAs',
  'A Irmã Gêmea': 'X-4r0X4vjBk',
  'O Presidente Mecânico': '67K5SK2hHLg',
  'A Filha Perdida': 'nubU-5C71zI',
  // Títulos novos adicionados
  'Ela ouviu o namorado ir buscar a ex no aeroporto e decidiu sumir para sempre!': 'gEacqyHO1D4',
  'No dia do casamento, ela pegou o noivo traindo e chamou um bilionário de noivo falso!': 'NRVCpQ8sxeA',
  'Garota pobre faz coração para um carrão. O CEO vê, se apaixona e casa com ela!': '0ycWcvAEe5M',
  'Uma Mecânica Indomável Conquistou o Coração de Um Herdeiro Bilionário': 'VeGy8mK-_MU',
  'Ela salvou uma idosa bilionária! A avó ordenou que seu neto CEO se casasse com ela!': 'D_RCAL23TVg',
  'Escolhe um cadeirante como noivo. Ele é um CEO influente e a rival enlouquece de inveja!': 'FLCqxrB3rOU',
  'CEO atropela uma garota cega e, ao ver seu pingente de jade, reconhece seu grande amor!': 'izfqPk08Vkk',
  'Trocou de noivo na boda! O estranho escolhido era o CEO real e a mima como madame rica!': 'l6A_2fVMJPQ',
  'No primeiro dia como chef, é escolhida pela avó do CEO e acaba se casando com ele!': 'J3DfQn1K6rg',
  'Trocada no altar, ela casou com o homem mais temido para se vingar!': 'awkcQu7OVZ8',
  'Sua Melhor Amiga Matou Sua Mãe e Ela Descobriu que o Próprio Marido Protegia a Assassina!': 'ym1e67vyBbQ',
  'Dispensado pela ex, ele casou de repente com uma CEO linda e poderosa': '9Y1ztjlbXUk',
  'Eles Roubaram Sua Casa e Sua Herança, Mas Ela Voltou com a Prova Definitiva!': 'aoAOkaLofAI',
  'CEO bilionário solteiro há 30 anos evita mulheres, mas se apaixona por estagiária no ônibus': 'q2Ybp21Eing',
  'CEO evitava mulheres até uma empregada que dançava mudar completamente a sua vida!': 'MnY3mzZeyv8',
  'CEO Finge Ser Pobre No Encontro, Todas Fogem! Só Ela Aceita Casar e Ele Se Apaixona!': 'qROR2BTupVE',
  'Seu marido por contrato é seu chefe! Ele manda ficar longe, mas enlouquece de ciúmes!': 'FubJEZkBIew',
  'Família Bilionária Finge Falência Para Testar Noiva, Mas Ela Gasta Tudo Com Eles!': 'u3jmEqIoY3A',
  'Garota Pobre É Forçada A Casar Com Fazendeiro Pela Meia-Irmã! Ele Era O CEO Mais Rico!': 'Ty5EdzgvcUA',
  'Magnata Finge Ser Guarda Pobre Num Encontro. Só A Caipira Gasta Tudo Em Wontons Pra Ele!': 'xDxGu3anP_M',
  'CEO Não Ri Há 20 Anos Até Ver A Noiva Caipira Expulsar A Vilã e Se Apaixona!': '68G7-C9hMTI',
  'Bilionária Se Disfarça De Mendiga Para Testar Os Sogros e Rompe O Noivado!': 'a79hDl9mbwM',
  'Bilionário Volta e Vê A Esposa Vendendo Na Rua, Humilhada Por Parentes!': '1LPlcimJIdE',
  'Ele Achava a Esposa Sem Graça, Até Vê-la Deslumbrante no Dia do Divórcio!': '8_gzc3gmQC0',
  'Meu Companheiro é um Lícano de Rua': 'XGWScFNq6uc',
  'O Acordo Matrimonial do CEO': 'dJKN--qTdVA',
  'Herança e Vingança': 'AX2lAdnRwgM',
  'Após 10 anos amando o vizinho, ela foi desprezada! Um motoqueiro mais jovem a conquistou': '6SW6mTUtA3w',
  'Gênio Médica Não É Alguém Para Mexer': 'QoHgX6xdo_g',
  'Gênio Médica Não É Alguém Para Mexer (Cenas Destacadas)': 'Th4dBDxutfE'
};

// Expor globalmente para uso no script de busca
window.doramaVideos = doramaVideos;
window.showPlayer = showPlayer;

function showPlayer(title, videoId) {
  const existing = document.getElementById('playerOverlay');
  if (existing) existing.remove();

  const overlay = document.createElement('div');
  overlay.id = 'playerOverlay';
  overlay.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:#000;z-index:10000;display:flex;flex-direction:column;';

  overlay.innerHTML = `
    <div style="display:flex;align-items:center;padding:12px 16px;background:rgba(0,0,0,0.9);gap:12px;">
      <button id="backBtn" style="background:none;border:none;color:#fff;font-size:22px;cursor:pointer;padding:4px 10px;border-radius:6px;background:#333;">←</button>
      <h2 style="color:#fff;font-size:16px;margin:0;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${title}</h2>
    </div>
    <div style="flex:1;position:relative;background:#000;">
      <iframe
        src="https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0&modestbranding=1"
        style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;"
        allow="autoplay; fullscreen; accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  `;

  document.body.appendChild(overlay);
  document.body.style.overflow = 'hidden';

  document.getElementById('backBtn').addEventListener('click', function() {
    overlay.remove();
    document.body.style.overflow = '';
  });

  document.addEventListener('keydown', function handleEsc(e) {
    if (e.key === 'Escape') {
      overlay.remove();
      document.body.style.overflow = '';
      document.removeEventListener('keydown', handleEsc);
    }
  });
}

// Clicar nos cards
document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('button.group.relative.w-full');
  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      const titleEl = this.querySelector('h3');
      if (titleEl) {
        const title = titleEl.textContent.trim();
        const videoId = doramaVideos[title];
        if (videoId) {
          showPlayer(title, videoId);
        }
      }
    });
  });

  // Botão "Assistir" do banner hero
  const btnAssistir = document.getElementById('btnAssistir');
  if (btnAssistir) {
    btnAssistir.addEventListener('click', function() {
      const heroTitle = document.querySelector('#inicio h1');
      if (heroTitle) {
        const title = heroTitle.textContent.trim();
        const videoId = doramaVideos[title];
        if (videoId) showPlayer(title, videoId);
        else document.getElementById('populares')?.scrollIntoView({ behavior: 'smooth' });
      }
    });
  }

  // Botão "Ver catálogo"
  const btnCatalogo = document.getElementById('btnCatalogo');
  if (btnCatalogo) {
    btnCatalogo.addEventListener('click', function() {
      document.getElementById('catalogo')?.scrollIntoView({ behavior: 'smooth' });
    });
  }
});

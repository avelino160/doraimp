// Atualizar thumbnails dos cards para usar capas do YouTube
const doramaVideos = {
  'Herdeira de Bilhões': 'gEacqyHO1D4',
  'Vingança Bilionária': 'NRVCpQ8sxeA',
  'Ele a Procurou por Todo Esse Tempo': '0ycWcvAEe5M',
  'A Faxineira e o Bilionário': 'VeGy8mK-_MU',
  'Ela Salvou um Bilionário': 'D_RCAL23TVg',
  'A Irmã Gêmea': 'FLCqxrB3rOU',
  'Mimada como uma Rainha': 'izfqPk08Vkk',
  'O CEO Entregador': 'l6A_2fVMJPQ',
  'Vingança em Kung-Fu': 'J3DfQn1K6rg',
  'A Enfermeira e o CEO': 'awkcQu7OVZ8',
  'Uma Tigela de Chá': 'ym1e67vyBbQ',
  'A Confeiteira Traída': '9Y1ztjlbXUk',
  'Fuga do Casamento': 'aoAOkaLofAI',
  'Um Tapa no CEO': 'q2Ybp21Eing',
  'Atropelada e Casada num Flash': 'MnY3mzZeyv8',
  'A Mesa Errada': 'qROR2BTupVE',
  'A Mesa Errada (Parte 2)': 'FubJEZkBIew',
  'Salvo do Fogo': 'u3jmEqIoY3A',
  'A Mãe Escolhida': 'Ty5EdzgvcUA',
  'O CEO que Fingiu ser Cego': 'xDxGu3anP_M',
  'Um Favor de Bilhões': '68G7-C9hMTI',
  'Forçada a Casar com o CEO': 'a79hDl9mbwM',
  'Coach de Amor': '1LPlcimJIdE',
  'Belas Espiãs': '8_gzc3gmQC0',
  'Vendida para o Campo': 'XGWScFNq6uc',
  'A Garota do Taco': 'dJKN--qTdVA',
  'O Casamento Recusado': 'AX2lAdnRwgM',
  'A CEO Disfarçada de Estudante': '6SW6mTUtA3w',
  'A Esposa Ignorada': 'QoHgX6xdo_g',
  'Gênio Médica Não É Alguém Para Mexer (Cenas Destacadas)': 'Th4dBDxutfE'
};

document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('button.group.relative.w-full');
  
  cards.forEach(function(card) {
    const titleElement = card.querySelector('h3');
    const imgElement = card.querySelector('img');
    
    if (titleElement && imgElement) {
      const title = titleElement.textContent.trim();
      const videoId = doramaVideos[title];
      
      if (videoId) {
        // Usar thumbnail do YouTube em alta qualidade
        imgElement.src = `https://i.ytimg.com/vi/${videoId}/hqdefault.jpg`;
        imgElement.onerror = function() {
          // Fallback para qualidade média se alta não funcionar
          this.src = `https://i.ytimg.com/vi/${videoId}/mqdefault.jpg`;
        };
      }
    }
  });
});

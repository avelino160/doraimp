// Sistema de destaque semanal com imagens locais de alta resolução
(function() {
  const featuredDoramas = [
    {
      title: 'Ele a Procurou por Todo Esse Tempo',
      image: 'pics/yt_0ycWcvAEe5M.jpg',
      rating: '8.4',
      description: 'Ele a procurou por todo esse tempo, sem saber que ela sempre esteve em seus sonhos. Um reencontro que muda o destino de dois corações.'
    },
    {
      title: 'Herdeira de Bilhões',
      image: 'pics/yt_gEacqyHO1D4.jpg',
      rating: '8.5',
      description: 'Uma herdeira que perdeu tudo retorna para reconquistar seu império e descobrir a verdade sobre sua família.'
    },
    {
      title: 'Vingança Bilionária',
      image: 'pics/yt_NRVCpQ8sxeA.jpg',
      rating: '8.5',
      description: 'Traída pela própria família, ela volta mais forte para recuperar o que é seu e fazer justiça.'
    },
    {
      title: 'Uma Mecânica Indomável Conquistou o Coração de Um Herdeiro Bilionário',
      image: 'pics/yt_VeGy8mK-_MU.jpg',
      rating: '8.4',
      description: 'Uma jovem mecânica talentosa e cheia de atitude cruza o caminho de um herdeiro bilionário, dando início a uma paixão arrebatadora.'
    },
    {
      title: 'Ela Salvou um Bilionário',
      image: 'pics/yt_D_RCAL23TVg.jpg',
      rating: '8.4',
      description: 'Depois de salvar um estranho, ela descobre que ele é o CEO mais procurado do país.'
    }
  ];
  
  function init() {
    const now = new Date();
    const start = new Date(now.getFullYear(), 0, 0);
    const diff = now - start;
    const oneWeek = 1000 * 60 * 60 * 24 * 7;
    const weekNumber = Math.floor(diff / oneWeek);
    
    const index = weekNumber % featuredDoramas.length;
    const featured = featuredDoramas[index];
    
    const h1 = document.querySelector('#inicio h1');
    const img = document.querySelector('#inicio img');
    const desc = document.querySelector('#inicio .max-w-xl');
    
    if (h1) h1.textContent = featured.title;
    if (img) {
      img.src = featured.image;
      img.alt = 'Cena de ' + featured.title;
    }
    if (desc) desc.textContent = featured.description;
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

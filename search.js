document.addEventListener('DOMContentLoaded', function() {
  var searchInput = document.getElementById('searchInput');
  if (!searchInput) return;

  var heroBanner  = document.getElementById('inicio');
  var secPop      = document.getElementById('populares');
  var secCatalogo = document.getElementById('catalogo');

  searchInput.addEventListener('input', function(e) {
    var term = e.target.value.toLowerCase().trim();
    var cards = document.querySelectorAll('button.group.relative.w-full');

    if (term === '') {
      if (heroBanner)  heroBanner.style.display  = '';
      if (secPop)      secPop.style.display       = '';
      if (secCatalogo) secCatalogo.style.display  = '';
      var old = document.getElementById('searchResults');
      if (old) old.remove();
      cards.forEach(function(card) {
        card.parentElement.style.display = '';
      });
      return;
    }

    // Esconder secções principais
    if (heroBanner)  heroBanner.style.display  = 'none';
    if (secPop)      secPop.style.display       = 'none';
    if (secCatalogo) secCatalogo.style.display  = 'none';

    // Criar secção de resultados se não existir
    var resultsSection = document.getElementById('searchResults');
    if (!resultsSection) {
      resultsSection = document.createElement('section');
      resultsSection.id = 'searchResults';
      resultsSection.style.cssText = 'padding:24px 16px;max-width:1280px;margin:0 auto;';
      resultsSection.innerHTML = '<h2 style="font-size:20px;font-weight:700;margin-bottom:16px;color:#fff;">Resultados</h2><div id="searchGrid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;"></div>';
      var main = document.querySelector('main');
      main.insertBefore(resultsSection, main.firstChild);
    }

    var grid = document.getElementById('searchGrid');
    grid.innerHTML = '';

    cards.forEach(function(card) {
      var titleEl = card.querySelector('h3');
      if (!titleEl) return;
      var matches = titleEl.textContent.toLowerCase().includes(term);
      card.parentElement.style.display = 'none';

      if (matches) {
        var clone = card.cloneNode(true);
        clone.addEventListener('click', function() {
          var t = this.querySelector('h3');
          if (t && window.showPlayer && window.doramaVideos) {
            var vid = window.doramaVideos[t.textContent.trim()];
            if (vid) window.showPlayer(t.textContent.trim(), vid);
          }
        });
        var wrapper = document.createElement('div');
        wrapper.appendChild(clone);
        grid.appendChild(wrapper);
      }
    });
  });
});

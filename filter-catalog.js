// Script completo de pesquisa com visualização dedicada de resultados e filtros
(function() {
  function initSearchAndFilter() {
    const searchInput = document.getElementById('searchInput');
    const header = document.querySelector('header');
    const inicioSection = document.getElementById('inicio');
    const popularesSection = document.getElementById('populares');
    const catalogoSection = document.getElementById('catalogo');

    if (!catalogoSection) return;

    // Criar seção dedicada de Resultados de Busca
    let searchResultsSection = document.getElementById('searchResults');
    if (!searchResultsSection) {
      searchResultsSection = document.createElement('section');
      searchResultsSection.id = 'searchResults';
      // Espaçamento superior generoso (pt-32 / pt-36) para não ficar embaixo da barra fixa do cabeçalho
      searchResultsSection.className = 'mx-auto max-w-7xl px-4 pt-28 sm:pt-36 pb-20 sm:px-6 min-h-[80vh]';
      searchResultsSection.style.display = 'none';

      searchResultsSection.innerHTML = `
        <div class="mb-8 flex items-center justify-between gap-4 border-b border-border/40 pb-5">
          <div>
            <h2 class="font-display text-2xl font-bold sm:text-3xl text-foreground">Resultados da busca</h2>
            <p id="searchResultsInfo" class="text-sm text-muted-foreground mt-1"></p>
          </div>
          <button id="clearSearchBtn" class="text-xs text-primary font-medium hover:underline px-4 py-2 rounded-full border border-primary/30 hover:bg-primary/10 transition cursor-pointer">
            Limpar busca
          </button>
        </div>
        <div id="searchResultsGrid" class="grid grid-cols-2 gap-3 sm:grid-cols-3 sm:gap-4 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6"></div>
      `;

      // Inserir antes do catálogo ou no main
      catalogoSection.parentNode.insertBefore(searchResultsSection, catalogoSection);

      const clearBtn = document.getElementById('clearSearchBtn');
      if (clearBtn) {
        clearBtn.addEventListener('click', function() {
          if (searchInput) {
            searchInput.value = '';
            searchTerm = '';
            handleSearchState();
          }
        });
      }
    }

    const searchResultsGrid = document.getElementById('searchResultsGrid');
    const searchResultsInfo = document.getElementById('searchResultsInfo');

    // Botões de categoria do catálogo
    const filterButtons = catalogoSection.querySelectorAll('.no-scrollbar button, .flex.gap-2 button, .overflow-x-auto button');
    const catalogoCards = catalogoSection.querySelectorAll('button.group.relative.w-full');

    let activeCategory = 'Todos';
    let searchTerm = '';

    function normalize(str) {
      if (!str) return '';
      return str
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .toLowerCase()
        .trim();
    }

    // Coletar todos os doramas únicos do catálogo para a busca
    const allDoramas = [];
    const seenTitles = new Set();

    catalogoCards.forEach(function(card) {
      const titleEl = card.querySelector('h3');
      const descEl = card.querySelector('p');
      const title = titleEl ? titleEl.textContent.trim() : '';
      const desc = descEl ? descEl.textContent.trim() : '';

      if (title && !seenTitles.has(title)) {
        seenTitles.add(title);
        allDoramas.push({
          element: card.cloneNode(true),
          originalCard: card,
          title: title,
          desc: desc
        });
      }
    });

    // Função para aplicar filtragem de categorias no catálogo normal
    function applyCategoryFilter() {
      const normCategory = normalize(activeCategory);
      let count = 0;

      catalogoCards.forEach(function(card) {
        const titleEl = card.querySelector('h3');
        const descEl = card.querySelector('p');
        const title = titleEl ? titleEl.textContent : '';
        const desc = descEl ? descEl.textContent : '';

        const normTitle = normalize(title);
        const normDesc = normalize(desc);

        const matchesCategory = (normCategory === 'todos') || normDesc.includes(normCategory) || normTitle.includes(normCategory);

        if (matchesCategory) {
          card.style.display = '';
          count++;
        } else {
          card.style.display = 'none';
        }
      });

      const countEl = catalogoSection.querySelector('.text-muted-foreground');
      if (countEl) {
        if (normCategory === 'todos') {
          countEl.textContent = `${catalogoCards.length} doramas disponíveis`;
        } else {
          countEl.textContent = `${count} dorama(s) na categoria ${activeCategory}`;
        }
      }
    }

    // Função de controle de exibição de busca
    function handleSearchState() {
      const normSearch = normalize(searchTerm);

      if (normSearch.length > 0) {
        // MODO BUSCA ATIVO:
        // Oculta banner (inicio), populares e catalogo completo
        if (inicioSection) inicioSection.style.display = 'none';
        if (popularesSection) popularesSection.style.display = 'none';
        if (catalogoSection) catalogoSection.style.display = 'none';

        // Garante que o cabeçalho fique com fundo escuro sólido para melhor contraste
        if (header) {
          header.classList.add('bg-background/95', 'backdrop-blur');
        }

        // Mostra a seção dedicada de resultados com espaçamento adequado
        searchResultsSection.style.display = '';
        searchResultsGrid.innerHTML = '';

        let resultsCount = 0;

        allDoramas.forEach(function(item) {
          const normTitle = normalize(item.title);
          const normDesc = normalize(item.desc);

          if (normTitle.includes(normSearch) || normDesc.includes(normSearch)) {
            const cardClone = item.element.cloneNode(true);
            cardClone.style.display = '';

            // Manter clique para abrir o player
            cardClone.addEventListener('click', function() {
              item.originalCard.click();
            });

            searchResultsGrid.appendChild(cardClone);
            resultsCount++;
          }
        });

        if (searchResultsInfo) {
          searchResultsInfo.textContent = resultsCount === 1 
            ? `1 dorama encontrado para "${searchTerm}"`
            : `${resultsCount} doramas encontrados para "${searchTerm}"`;
        }

        if (resultsCount === 0) {
          searchResultsGrid.innerHTML = `
            <div class="col-span-full py-16 text-center text-muted-foreground">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="mx-auto mb-3 text-muted-foreground/60"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.34-4.34"></path></svg>
              <p class="text-base font-semibold text-foreground">Nenhum dorama encontrado para "${searchTerm}"</p>
              <p class="text-xs text-muted-foreground mt-1">Verifique a ortografia ou tente pesquisar por outra palavra-chave.</p>
            </div>
          `;
        }

        window.scrollTo({ top: 0, behavior: 'smooth' });

      } else {
        // MODO NORMAL (sem busca):
        // Reexibe banner, populares e catálogo
        if (inicioSection) inicioSection.style.display = '';
        if (popularesSection) popularesSection.style.display = '';
        if (catalogoSection) catalogoSection.style.display = '';

        if (header) {
          header.classList.remove('bg-background/95', 'backdrop-blur');
        }

        // Oculta a seção de resultados
        searchResultsSection.style.display = 'none';
        searchResultsGrid.innerHTML = '';
      }
    }

    // Configuração dos botões de categoria do catálogo
    const activeClasses = ['border-primary', 'bg-primary/10', 'text-primary'];
    const inactiveClasses = ['border-border', 'text-muted-foreground', 'hover:text-foreground'];

    filterButtons.forEach(function(btn) {
      btn.style.cursor = 'pointer';
      btn.addEventListener('click', function(e) {
        e.preventDefault();
        activeCategory = this.textContent.trim();

        filterButtons.forEach(b => {
          b.classList.remove(...activeClasses);
          b.classList.add(...inactiveClasses);
        });

        this.classList.remove(...inactiveClasses);
        this.classList.add(...activeClasses);

        applyCategoryFilter();
      });
    });

    // Escutar digitação no input de busca
    if (searchInput) {
      searchInput.addEventListener('input', function(e) {
        searchTerm = e.target.value;
        handleSearchState();
      });

      // Tecla Escape limpa a busca e volta à tela inicial
      searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
          this.value = '';
          searchTerm = '';
          handleSearchState();
        }
      });

      // Ícone da lupa
      const searchContainer = searchInput.parentElement;
      if (searchContainer) {
        const svgIcon = searchContainer.querySelector('svg');
        if (svgIcon) {
          svgIcon.style.cursor = 'pointer';
          svgIcon.classList.remove('pointer-events-none');
          svgIcon.addEventListener('click', function() {
            searchInput.focus();
          });
        }
      }
    }

    // Resetar busca se clicar no logo ou nos links de navegação "Início" / "Catálogo"
    const navLinks = document.querySelectorAll('header a[href="#inicio"], header a[href="#catalogo"], a[aria-label*="DoraLivre"]');
    navLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        if (searchInput && searchInput.value) {
          searchInput.value = '';
          searchTerm = '';
          handleSearchState();
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSearchAndFilter);
  } else {
    initSearchAndFilter();
  }
})();

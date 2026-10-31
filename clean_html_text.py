import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Replace corrupted characters in the categories
replacements = {
    '>Ao</button>': '>Ação</button>',
    '>Comdia</button>': '>Comédia</button>',
    '>Famlia</button>': '>Família</button>',
    '>Vingana</button>': '>Vingança</button>',
    '>Catlogo completo</h2>': '>Catálogo completo</h2>',
    'disponveis</p>': 'disponíveis</p>',
    'Pster de ': 'Pôster de ',
}

for k, v in replacements.items():
    text = text.replace(k, v)

# Also fix the genre separator in cards: "2026<!-- -->  <!-- -->Romance  Drama" -> "2026<!-- --> · <!-- -->Romance · Drama"
text = re.sub(r'<!-- -->\s*\s*<!-- -->', '<!-- --> · <!-- -->', text)
text = text.replace('  ', ' · ')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Sanitized categories and card genres in index.html')

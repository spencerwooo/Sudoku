module.exports = {
  title: 'Sudoku',
  description: '命令行交互的基础数独工具库',
  base: '',
  head: [
    ['link', {
      rel: 'icon',
      href: '/favicon.png'
    }],
    ['meta', {
      name: 'theme-color',
      content: '#00ABE9'
    }],
    ['meta', {
      name: 'apple-mobile-web-app-capable',
      content: 'yes'
    }],
    ['meta', {
      name: 'apple-mobile-web-app-status-bar-style',
      content: 'black'
    }],
    ['link', {
      rel: 'apple-touch-icon',
      href: '/favicon.png'
    }],
    ['meta', {
      name: 'msapplication-TileImage',
      content: '/favicon.png'
    }],
    ['meta', {
      name: 'msapplication-TileColor',
      content: '#06BDFF'
    }]
  ],
  themeConfig: {
    nav: [
      {
        text: 'GitHub',
        link: 'https://github.com/spencerwooo/Sudoku'
      },
    ],
    sidebar: {
      '/Progress/': [''],
      '/': ['']
    },
    lastUpdated: 'Last Updated'
  }
}
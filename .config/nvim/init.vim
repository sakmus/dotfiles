" Basic Settings
:set number
:set relativenumber
:set autoindent
:set tabstop=4
:set shiftwidth=4
:set smarttab
:set softtabstop=4
:set mouse=a
:set wrap

" Plugin Installations
call plug#begin()

Plug 'preservim/nerdtree'
Plug 'ap/vim-css-color'
Plug 'nordtheme/vim'
Plug 'ryanoasis/vim-devicons'
Plug 'preservim/tagbar'
Plug 'nvim-lualine/lualine.nvim'
Plug 'numToStr/Comment.nvim'

Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdline'
Plug 'hrsh7th/nvim-cmp'

set encoding=UTF-8
call plug#end()

lua require('lualine').setup()
lua require('plugins.cmp')
lua require('plugins.lsp')

" Nerdtree
nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable="+"
let g:NERDTreeDirArrowCollapsible="-"

" Tagbar
nmap <F8> :TagbarToggle<CR>

colorscheme nord
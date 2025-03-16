-- Basic options

vim.wo.number = true
vim.wo.relativenumber = true
vim.wo.cursorline = true
vim.wo.wrap = true
vim.o.mouse = 'a'


-- Vim Plug

local vim = vim
local Plug = vim.fn['plug#']

vim.call('plug#begin')

Plug('nvim-lualine/lualine.nvim')
Plug('nvim-tree/nvim-web-devicons')
Plug('cocopon/iceberg.vim')
Plug('nvim-tree/nvim-tree.lua')
Plug('preservim/nerdtree')
Plug('iamcco/markdown-preview.nvim')
Plug('MeanderingProgrammer/render-markdown.nvim')
Plug('nvim-treesitter/nvim-treesitter')
Plug("RedsXDD/neopywal.nvim")
Plug('neoclide/coc.nvim')
Plug('norcalli/nvim-colorizer.lua')

vim.call('plug#end')


require("nvim-tree").setup()


-- Lua Line

require('lualine').setup {
	options = { theme = 'pywal', },
}


-- Nerd Tree
vim.keymap.set('n', '<C-t>', ':NERDTreeToggle<CR>', { noremap = true, silent = true })
vim.g.NERDTreeDirArrowExpandable = '+'
vim.g.NERDTreeDirArrowCollapsible = '-'


vim.cmd('set termguicolors')
require'colorizer'.setup()

vim.cmd('colorscheme neopywal-dark')


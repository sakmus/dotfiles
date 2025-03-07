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

vim.call('plug#end')


-- Lua Line

require('lualine').setup {
	options = { theme = 'iceberg_dark', },
}

-- Nerd Tree
vim.keymap.set('n', '<C-t>', ':NERDTreeToggle<CR>', { noremap = true, silent = true })
-- vim.api.nvim_create_autocmd('VimEnter', {
--   callback = function()
--     vim.cmd('NERDTree')
--     vim.cmd('wincmd p')
--   end
-- })
-- vim.api.nvim_create_autocmd('BufEnter', {
--   callback = function()
--     if vim.fn.tabpagenr('$') == 1 and vim.fn.winnr('$') == 1 and vim.b.NERDTree and vim.b.NERDTree.isTabTree() then
--       vim.fn.feedkeys(":quit<CR>:<BS>")
--     end
--   end
-- })
-- vim.api.nvim_create_autocmd('BufEnter', {
--   callback = function()
--     if vim.fn.winnr('$') == 1 and vim.b.NERDTree and vim.b.NERDTree.isTabTree() then
--       vim.fn.feedkeys(":quit<CR>:<BS>")
--     end
--   end
-- })
vim.g.NERDTreeDirArrowExpandable = '+'
vim.g.NERDTreeDirArrowCollapsible = '-'



vim.cmd('colorscheme iceberg')

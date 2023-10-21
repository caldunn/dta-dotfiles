local fn = vim.fn

local lazypath = fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
	fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable", -- latest stable release
		lazypath,
	})
end
vim.opt.rtp:prepend(lazypath)

-- Use a protected call so we don't error out on first use
local status_ok, lazy = pcall(require, "lazy")
if not status_ok then
	return
end

-- Install your plugins here
return lazy.setup({
	"nvim-lua/plenary.nvim", -- Useful lua functions used by lots of plugins

	-- Colour schemes
	"folke/tokyonight.nvim",

	-- LSP
	{
		"neovim/nvim-lspconfig",
		dependencies = {
			"williamboman/mason.nvim",
			"williamboman/mason-lspconfig.nvim",
		},
	},

	-- Completions
	{
		"hrsh7th/nvim-cmp",
		dependencies = {
			"hrsh7th/cmp-buffer", -- buffer completions
			"hrsh7th/cmp-path", -- path completions
			"saadparwaiz1/cmp_luasnip", -- snippet completions
			"hrsh7th/cmp-nvim-lsp",
			"hrsh7th/cmp-nvim-lua",
		},
	},

	-- Snippets
	"L3MON4D3/LuaSnip", --snippet engine
	"rafamadriz/friendly-snippets", -- a bunch of snippets to

	"jose-elias-alvarez/null-ls.nvim",
	"RRethy/vim-illuminate",

	"nvim-telescope/telescope.nvim",

	-- ts
	{ "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
	-- "p00f/nvim-ts-rainbow",

	-- Autopairs closes braces
	"windwp/nvim-autopairs",

	-- git annotations
	"lewis6991/gitsigns.nvim",

	-- nvim-tree
	"kyazdani42/nvim-web-devicons",
	"kyazdani42/nvim-tree.lua",

	-- bufferline
	"ThePrimeagen/harpoon",

	-- lualine
	"nvim-lualine/lualine.nvim",

	"folke/which-key.nvim",

	"MunifTanjim/prettier.nvim",

	-- folding
	{ "kevinhwang91/nvim-ufo", dependencies = "kevinhwang91/promise-async" },

	-- html tag closing
	"windwp/nvim-ts-autotag",
})
